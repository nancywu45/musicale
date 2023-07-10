from music.domainmodel.model import Review, Track, User


def insert_user(empty_session, values=None):
    new_name = "Andrew"
    new_password = "1234"

    if values is not None:
        new_name = values[0]
        new_password = values[1]

    empty_session.execute(
        "INSERT INTO users (user_name, password) VALUES (:user_name, :password)",
        {"user_name": new_name, "password": new_password},
    )
    row = empty_session.execute(
        "SELECT id from users where user_name = :user_name", {"user_name": new_name}
    ).fetchone()
    return row[0]


def insert_users(empty_session, values):
    for value in values:
        empty_session.execute(
            "INSERT INTO users (user_name, password) VALUES (:user_name, :password)",
            {"user_name": value[0], "password": value[1]},
        )
    rows = list(empty_session.execute("SELECT id from users"))
    keys = tuple(row[0] for row in rows)
    return keys


def make_user():
    user = User(1, "Andrew", "111")
    return user


def make_track():
    track = Track(1, "hello")
    return track


def make_review(track: Track, user: User):
    review = Review(track, "test", 5, user)
    return review
