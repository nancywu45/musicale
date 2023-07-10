import abc
from typing import List
from datetime import date
from music.domainmodel.model import Album, Review
from music.domainmodel.model import Artist
from music.domainmodel.model import Genre
from music.domainmodel.model import Track

from music.domainmodel.model import User

repo_instance = None


class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User) -> None:
        """Adds a User to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str) -> User:
        """Returns a User with the given username, or None if no such User."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self) -> List[User]:
        """Returns the list of Users in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks(self) -> List[Track]:
        """Returns the list of Tracks in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_track(self, track: Track) -> None:
        """Adds a Track to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self, genre: Genre) -> List[Genre]:
        """Returns the list of Genres in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_genre(self, genre_id: int) -> Genre:
        """Returns the Genre with the given id, or None if no such Genre."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre) -> None:
        """Adds a Genre to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_album(self, album: Album) -> None:
        """Adds an Album to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_albums(self) -> List[Album]:
        """Returns the list of Albums in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_album(self, album_id: int) -> Album:
        """Returns an Album with the given id, or None if no such Album."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_track(self, track_id: int) -> Track:
        """Returns the Track with the given id, or None if no such Track."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_artists(self) -> List[Artist]:
        """Returns the list of Artists in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_artist(self, artist: Artist) -> None:
        """Adds an Artist to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_artist(self, artist_id: int) -> Artist:
        """Returns the Artist with the given id, or None if no such Artist."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_reviews(self) -> List[Review]:
        """Returns the list of Comments in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review) -> None:
        """Adds a Comment to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def update_track(self, track: Track) -> None:
        """Updates a Track in the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user: User) -> None:
        """Updates a User in the repository."""
        raise NotImplementedError
