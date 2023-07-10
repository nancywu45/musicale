from music.adapters.database_repository import SqlAlchemyRepository
from music.domainmodel.model import User


def test_repository_can_add_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = User(5, "Dave", "123456789")
    repo.add_user(user)

    repo.add_user(User(6, "Martin", "123456789"))

    user2 = repo.get_user("Dave")

    assert user2 == user and user2 is user


def test_repository_can_retrieve_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)
    user = repo.get_user("fmercury")
    assert user == User(2, "fmercury", "8734gfe2058v")


def test_repository_does_not_retrieve_a_non_existent_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = repo.get_user("prince")
    assert user is None


def test_repository_does_not_retrieve_a_non_existent_track(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_track(2500)
    assert track is None
