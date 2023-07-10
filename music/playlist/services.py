from typing import List
from music.adapters.repository import AbstractRepository
from music.domainmodel.model import Genre
from music.domainmodel.model import Track
from music.domainmodel.model import User


def get_playlist_tracks(user: User) -> List[Track]:
    return user.tracks


def get_genres(repo: AbstractRepository) -> List[Genre]:
    return repo.get_genres()


def delete_track_from_playlist(
    repo: AbstractRepository, user: User, track_id: int
) -> None:
    track = repo.get_track(track_id)
    user.remove_track(track)
    track.remove_user(user)
    repo.update_user(user)
    repo.update_track(track)


def get_user(repo: AbstractRepository, username) -> List[Genre]:
    return repo.get_user(username)
