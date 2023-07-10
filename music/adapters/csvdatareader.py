import os
import csv
import ast
from pathlib import Path
from typing import List
from music.adapters.repository import AbstractRepository
from werkzeug.security import generate_password_hash


from music.domainmodel.model import Artist
from music.domainmodel.model import Album
from music.domainmodel.model import Track
from music.domainmodel.model import Genre
from music.domainmodel.model import User


def read_csv_file(filename: str):
    rows = []
    # encoding of unicode_escape is required to decode successfully
    with open(filename, encoding="unicode_escape") as track_csv:
        reader = csv.DictReader(track_csv)
        for track_row in reader:
            rows.append(track_row)
    return rows


def create_track_object(track_row, repo: AbstractRepository):
    if repo.get_track(int(track_row["track_id"])) is None:
        track = Track(int(track_row["track_id"]), track_row["track_title"])
        repo.add_track(track)
        track.track_url = track_row["track_url"]
        track_duration = (
            round(float(track_row["track_duration"]))
            if track_row["track_duration"] is not None
            else None
        )
        if type(track_duration) is int:
            track.track_duration = track_duration

        if len(track_row["track_image_file"].split("albums/")) == 2:
            track.track_image_url = (
                "https://freemusicarchive.org/image/?file=images%2Falbums%2F"
                + track_row["track_image_file"].split("albums/")[1]
                + "&width=290&height=290&type=image"
            )
        else:
            track.track_image_url = None

        if track_row["track_file"] != "":
            track.track_audio_url = (
                "https://files.freemusicarchive.org/storage-freemusicarchive-org/"
                + track_row["track_file"]
            )
        else:
            track.track_audio_url = None
    return track


def create_artist_object(track_row, repo: AbstractRepository):
    artist = None
    artist_id = int(track_row["artist_id"])
    if repo.get_artist(artist_id) is None:
        artist = Artist(artist_id, track_row["artist_name"])
    return artist


def create_album_object(row, artists: List[Artist], repo: AbstractRepository):
    album_id = int(row["album_id"])
    if repo.get_album(album_id) is None:
        album = Album(album_id, row["album_title"])
        album.album_url = row["album_url"]
        album.album_type = row["album_type"]
        artist = next(
            (artist for artist in artists if artist.full_name == row["artist_name"]),
            None,
        )
        album.artist = artist
        if len(row["album_image_file"].split("albums/")) == 2:
            album.album_image_url = (
                "https://freemusicarchive.org/image/?file=images%2Falbums%2F"
                + row["album_image_file"].split("albums/")[1]
                + "&width=290&height=290&type=image"
            )

        else:
            album.track_image_url = None

        album.release_year = (
            int(row["album_year_released"])
            if row["album_year_released"].isdigit()
            else None
        )
        if artist:
            artist.add_album(album)

    return album


def extract_genres(track_row: dict, repo: AbstractRepository) -> List[Genre]:
    # List of dictionaries inside the string.
    track_genres_raw = track_row["track_genres"]
    # Populate genres. track_genres can be empty (None)
    genres = []
    if track_genres_raw:
        try:
            genre_dicts = (
                ast.literal_eval(track_genres_raw) if track_genres_raw != "" else []
            )

            for genre_dict in genre_dicts:
                if repo.get_genre(int(genre_dict["genre_id"])) is None:
                    genre = Genre(
                        int(genre_dict["genre_id"]), genre_dict["genre_title"]
                    )
                    repo.add_genre(genre)
                    genres.append(genre)

        except Exception as e:
            print(track_genres_raw)
            print(f"Exception occurred while parsing genres: {e}")

    return genres


def load_albums(data_path: Path, repo: AbstractRepository, artists: List[Artist]):
    albums = []
    for row in read_csv_file(str(data_path / "albums.csv")):
        album_id = (
            int(row["album_id"]) if row["album_id"].isdigit() else row["album_id"]
        )
        if type(album_id) is not int:
            print(f"Invalid album_id: {album_id}")
            print(row)
            continue
        album = create_album_object(row, artists, repo)
        if album:
            albums.append(album)
            repo.add_album(album)
    return albums


def load_artists(data_path: Path, repo: AbstractRepository):
    tracks_filename = str(Path(data_path) / "tracks.csv")
    artists = []
    for data_row in read_csv_file(tracks_filename):
        artist = create_artist_object(data_row, repo)
        if artist:
            artists.append(artist)
            repo.add_artist(artist)
    return artists


def load_tracks_and_genres(
    data_path: Path,
    repo: AbstractRepository,
    artists: List[Artist],
    albums: List[Album],
):
    track_filename = str(data_path / "tracks.csv")
    for data_row in read_csv_file(track_filename):
        track = create_track_object(data_row, repo)
        if track is not None:
            genres = extract_genres(data_row, repo)
            album = next(
                (
                    album
                    for album in albums
                    if data_row["album_id"] != ""
                    and album.album_id == int(data_row["album_id"])
                ),
                None,
            )
            artist = next(
                (
                    artist
                    for artist in artists
                    if artist.artist_id == int(data_row["artist_id"])
                ),
                None,
            )

            if artist:
                artist.add_track(track)
                track.artist = artist
            if album:
                album.add_track(track)
                track.album = album
            for genre in genres:
                track.add_genre(genre)
                genre.add_track_genre(track)


def load_users(data_path: Path, repo: AbstractRepository):
    users_filename = str(Path(data_path) / "users.csv")
    for data_row in read_csv_file(users_filename):
        user = User(
            user_id=int(data_row["id"]),
            user_name=data_row["username"],
            password=generate_password_hash(data_row["password"]),
        )
        repo.add_user(user)
