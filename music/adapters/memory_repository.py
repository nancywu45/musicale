from typing import List

from music.adapters.repository import AbstractRepository
from music.domainmodel.model import Album, Review
from music.domainmodel.model import Artist
from music.domainmodel.model import Genre
from music.domainmodel.model import Track
from music.domainmodel.model import User


class MemoryRepository(AbstractRepository):
    def __init__(self) -> None:
        self.__users: List[User] = list()
        self.__tracks: List[Track] = list()
        self.__genres: List[Genre] = list()
        self.__albums: List[Album] = list()
        self.__artist: List[Artist] = list()
        self.__reviews: List[Review] = list()

    def add_user(self, user: User) -> None:
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next(
            (user for user in self.__users if user.user_name == user_name), None
        )

    def get_users(self) -> List[User]:
        return self.__users

    def add_track(self, track: Track) -> None:
        self.__tracks.append(track)

    def get_tracks(self) -> List[Track]:
        return self.__tracks

    def get_track(self, id: int) -> Track:
        return next((track for track in self.__tracks if track.track_id == id), None)

    def add_genre(self, genre: Genre) -> None:
        self.__genres.append(genre)

    def get_genres(self) -> List[Genre]:
        return self.__genres

    def get_genre(self, genre_id: int) -> Genre:
        return next(
            (genre for genre in self.__genres if genre.genre_id == genre_id), None
        )

    def add_album(self, album: Album) -> None:
        self.__albums.append(album)

    def get_albums(self) -> List[Album]:
        return self.__albums

    def get_album(self, album_id: int) -> Album:
        return next(
            (album for album in self.__albums if album.album_id == album_id), None
        )

    def get_artists(self) -> List[Artist]:
        return self.__artist

    def add_artist(self, artist: Artist) -> None:
        self.__artist.append(artist)

    def get_artist(self, artist_id: int) -> Artist:
        return next(
            (artist for artist in self.__artist if artist.artist_id == artist_id), None
        )

    def get_reviews(self) -> List[Review]:
        return self.__reviews

    def add_review(self, review: Review) -> None:
        self.__reviews.append(review)

    def update_track(self, track: Track) -> None:
        pass

    def update_user(self, user: User) -> None:
        pass
