from typing import List, Iterable

from music.adapters.repository import AbstractRepository
from music.domainmodel.model import Review
from music.domainmodel.model import Track
from music.domainmodel.model import User


def get_track(track_id: int, repo: AbstractRepository):
    track = repo.get_track(track_id)
    return track


def add_review(repo: AbstractRepository, review: Review, track: Track):
    track.add_review(review)
    repo.add_review(review)


def get_reviews(track: Track) -> List[Review]:
    return track.reviews


def get_user(repo: AbstractRepository, username: str) -> User:
    return repo.get_user(username)
