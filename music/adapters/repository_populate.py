from pathlib import Path
from music.adapters.csvdatareader import (
    load_albums,
    load_artists,
    load_tracks_and_genres,
    load_users,
)
from music.adapters.repository import AbstractRepository


def populate(data_path: Path, repo: AbstractRepository):
    artists = load_artists(data_path, repo)
    albums = load_albums(data_path, repo, artists)
    load_tracks_and_genres(data_path, repo, artists, albums)
    load_users(data_path, repo)
