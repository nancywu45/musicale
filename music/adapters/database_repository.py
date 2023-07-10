from typing import List
from sqlalchemy.orm import scoped_session, joinedload
from music.adapters.repository import AbstractRepository
from music.domainmodel.model import Artist, Review
from music.domainmodel.model import Genre
from music.domainmodel.model import Track
from music.domainmodel.model import User
from music.domainmodel.model import Album
from sqlalchemy.orm.exc import NoResultFound


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = (
                self._session_cm.session.query(User)
                .filter(User._User__user_name == user_name)
                .one()
            )
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return user

    def get_users(self) -> List[User]:
        with self._session_cm as scm:
            return scm.session.query(User).all()

    def add_track(self, track: Track):
        with self._session_cm as scm:
            scm.session.add(track)
            scm.commit()

    def get_tracks(self) -> List[Track]:
        with self._session_cm as scm:
            return scm.session.query(Track).all()

    def get_track(self, track_id: int) -> Track:
        track = None
        try:
            track = (
                self._session_cm.session.query(Track)
                .filter(Track._Track__track_id == track_id)
                .one()
            )
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return track

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def get_genres(self) -> List[Genre]:
        return self._session_cm.session.query(Genre).all()

    def get_genre(self, genre_id: int) -> Genre:
        genre = None
        try:
            genre = (
                self._session_cm.session.query(Genre)
                .filter(Genre._Genre__genre_id == genre_id)
                .one()
            )
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return genre

    def add_album(self, album: Album):
        with self._session_cm as scm:
            scm.session.add(album)
            scm.commit()

    def get_albums(self) -> List[Album]:
        with self._session_cm as scm:
            return scm.session.query(Album).all()

    def get_album(self, album_id: int) -> Album:
        album = None
        try:
            album = (
                self._session_cm.session.query(Album)
                .filter(Album._Album__album_id == album_id)
                .one()
            )
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return album

    def add_artist(self, artist: Artist):
        with self._session_cm as scm:
            scm.session.add(artist)
            scm.commit()

    def get_artists(self):
        with self._session_cm as scm:
            return scm.session.query(Artist).all()

    def get_artist(self, artist_id: int) -> Artist:
        artist = None
        try:
            artist = (
                self._session_cm.session.query(Artist)
                .filter(Artist._Artist__artist_id == artist_id)
                .one()
            )
        except NoResultFound:
            # Ignore any exception and return None.
            pass
        return artist

    def get_reviews(self) -> List[Review]:
        with self._session_cm as scm:
            return scm.session.query(Review).all()

    def add_review(self, review: Review):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def update_track(self, track: Track):
        with self._session_cm as scm:
            scm.session.merge(track)
            scm.commit()

    def update_user(self, user: User):
        with self._session_cm as scm:
            scm.session.merge(user)
            scm.commit()
