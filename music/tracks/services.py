from typing import List
from music.adapters.repository import AbstractRepository
from music.domainmodel.model import Track
from music.domainmodel.model import Genre
from music.domainmodel.model import User


def get_tracks(repo: AbstractRepository) -> List[Track]:
    return repo.get_tracks()


def get_genres(repo: AbstractRepository) -> List[Genre]:
    return repo.get_genres()


def get_user(repo: AbstractRepository, username: str) -> User:
    return repo.get_user(username)


def add_track_to_playlist(repo: AbstractRepository, user: User, track_id: int) -> None:
    track = repo.get_track(track_id)
    user.add_track(track)
    track.add_user(user)
    repo.update_user(user)
    repo.update_track(track)


def get_track(repo: AbstractRepository, track_id: int) -> Track:
    return repo.get_track(track_id)
