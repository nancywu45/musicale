from datetime import datetime
from typing import List


class Track:
    def __init__(self, track_id: int, track_title: str):
        if type(track_id) is not int or track_id < 0:
            raise ValueError
        self.__track_id = track_id

        self.__title: str | None = None
        if type(track_title) is str:
            self.__title = track_title.strip()

        self.__artist: Artist | None = None
        self.__album: Album | None = None
        self.__track_url: str | None = None
        # duration in seconds
        self.__track_duration: int | None = None
        self.__genres: List[Genre] = []
        self.__track_image_url: str | None = None
        self.__track_audio_url: str | None = None
        self.__reviews: List[Review] = []
        self.__users: List[User] = []

    @property
    def track_id(self) -> int:
        return self.__track_id

    @property
    def title(self) -> str | None:
        return self.__title

    @title.setter
    def title(self, book_title: str):
        self.__title = None
        if type(book_title) is str and book_title.strip() != "":
            self.__title = book_title.strip()

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, new_artist):
        if isinstance(new_artist, Artist):
            self.__artist = new_artist
        else:
            self.__artist = None

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, new_album):
        if isinstance(new_album, Album):
            self.__album = new_album
        else:
            self.__album = None

    @property
    def track_url(self) -> str | None:
        return self.__track_url

    @track_url.setter
    def track_url(self, new_track_url: str):
        if type(new_track_url) is str:
            self.__track_url = new_track_url.strip()
        else:
            self.__track_url = None

    @property
    def track_duration(self) -> int | None:
        return self.__track_duration

    @track_duration.setter
    def track_duration(self, new_duration: int):
        self.__track_duration = None
        if type(new_duration) is int and new_duration >= 0:
            self.__track_duration = new_duration
        else:
            raise ValueError

    @property
    def track_image_url(self) -> str | None:
        return self.__track_image_url

    @track_image_url.setter
    def track_image_url(self, new_track_image_url: str):
        if type(new_track_image_url) is str:
            self.__track_image_url = new_track_image_url.strip()
        else:
            self.__track_image_url = None

    @property
    def track_audio_url(self) -> str | None:
        return self.__track_audio_url

    @track_audio_url.setter
    def track_audio_url(self, new_track_audio_url: str):
        if type(new_track_audio_url) is str:
            self.__track_audio_url = new_track_audio_url.strip()
        else:
            self.__track_audio_url = None

    @property
    def genres(self) -> list:
        return self.__genres

    def add_genre(self, new_genre):
        if not isinstance(new_genre, Genre) or new_genre in self.__genres:
            return
        self.__genres.append(new_genre)

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, new_reviews):
        self.__reviews = new_reviews

    @property
    def users(self):
        return self.__users

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)

    def add_review(self, review):
        self.__reviews.append(review)

    def __repr__(self):
        return f"<Track {self.title}, track id = {self.track_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.track_id == other.track_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.track_id < other.track_id

    def __hash__(self):
        return hash(self.track_id)

    def add_review(self, review):
        self.__reviews.append(review)


class Album:
    def __init__(self, album_id: int, title: str):
        if type(album_id) is not int or album_id < 0:
            raise ValueError("Album ID should be a non negative integer!")
        self.__album_id: int = album_id

        self.__title: str | None = None
        if type(title) is str and title.strip() != "":
            self.__title = title.strip()

        self.__album_url: str | None = None
        self.__album_type: str | None = None
        self.__release_year: int | None = None
        self.__album_image_url: str | None = None
        self.__tracks: List[Track] = []
        self.__artist: Artist | None = None

    @property
    def album_id(self) -> int:
        return self.__album_id

    @property
    def title(self) -> str | None:
        return self.__title

    @title.setter
    def title(self, new_title):
        if type(new_title) is str and new_title.strip() != "":
            self.__title = new_title.strip()
        else:
            self.__title = None

    @property
    def album_url(self) -> str | None:
        return self.__album_url

    @album_url.setter
    def album_url(self, new_album_url: str):
        if type(new_album_url) is str:
            self.__album_url = new_album_url.strip()
        else:
            self.__album_url = None

    @property
    def album_type(self) -> str | None:
        return self.__album_type

    @album_type.setter
    def album_type(self, new_album_type: str):
        if type(new_album_type) is str:
            self.__album_type = new_album_type.strip()
        else:
            self.__album_type = None

    @property
    def album_image_url(self) -> str | None:
        return self.__album_image_url

    @album_image_url.setter
    def album_image_url(self, string) -> str | None:
        if type(string) is str:
            self.__album_image_url = string.strip()
        else:
            self.__album_image_url = Non

    @property
    def release_year(self) -> int | None:
        return self.__release_year

    @release_year.setter
    def release_year(self, new_release_year: int):
        if type(new_release_year) is int and new_release_year >= 0:
            self.__release_year = new_release_year
        else:
            self.__release_year = None

    @property
    def tracks(self) -> List[Track]:
        return self.__tracks

    @tracks.setter
    def tracks(self, new_tracks: List[Track]):
        self.__tracks = new_tracks

    def add_track(self, new_track: Track):
        if not isinstance(new_track, Track) or new_track in self.__tracks:
            return
        self.__tracks.append(new_track)

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, new_artist):
        self.__artist = new_artist

    def __repr__(self) -> str:
        return f"<Album {self.title}, album id = {self.album_id}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.album_id == other.album_id

    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return True
        return self.album_id < other.album_id

    def __hash__(self):
        return hash(self.album_id)


class Review:
    def __init__(self, track: Track, review_text: str, rating: int, user):
        self.__track = None
        self.__user = user

        if isinstance(track, Track):
            self.__track = track

        self.__review_text = "N/A"
        if isinstance(review_text, str):
            self.__review_text = review_text.strip()

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating: int | None = rating
        else:
            raise ValueError("Invalid value for the rating.")

        self.__timestamp = datetime.now()

    @property
    def track(self) -> Track | None:
        return self.__track

    @property
    def review_text(self) -> str:
        return self.__review_text

    @review_text.setter
    def review_text(self, new_text):
        if type(new_text) is str:
            self.__review_text = new_text.strip()
        else:
            self.__review_text = None

    @property
    def rating(self) -> int | None:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self.__rating = new_rating
        else:
            self.__rating = None
            raise ValueError("Wrong value for the rating")

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user):
        self.__user = new_user

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
            other.track == self.track
            and other.review_text == self.review_text
            and other.rating == self.rating
            and other.timestamp == self.timestamp
        )

    def __repr__(self):
        return f"<Review of track {self.track}, rating = {self.rating}, review_text = {self.review_text}>"


class User:
    def __init__(self, user_id: int, user_name: str, password: str):
        if type(user_id) is not int or user_id < 0:
            raise ValueError("User ID should be a non negative integer.")
        self.__user_id = user_id

        self.__user_name: str | None = None
        if type(user_name) is str:
            self.__user_name = user_name.lower().strip()

        self.__password: str | None = None
        if isinstance(password, str) and len(password) >= 7:
            self.__password = password

        self.__reviews: list[Review] = []
        self.__liked_tracks: list[Track] = []
        self.__tracks: list[Track] = []

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def user_name(self) -> str | None:
        return self.__user_name

    @property
    def password(self) -> str | None:
        return self.__password

    @property
    def reviews(self) -> list:
        return self.__reviews

    def add_review(self, new_review: Review):
        if not isinstance(new_review, Review) or new_review in self.__reviews:
            return
        self.__reviews.append(new_review)

    def remove_review(self, review: Review):
        if not isinstance(review, Review) or review not in self.__reviews:
            return
        self.__reviews.remove(review)

    @property
    def liked_tracks(self) -> list:
        return self.__liked_tracks

    @property
    def tracks(self) -> Track:
        return self.__tracks

    def add_track(self, track: Track):
        if track not in self.__tracks:
            self.__tracks.append(track)
        else:
            pass

    def remove_track(self, track: Track):
        if track in self.__tracks:
            self.__tracks.remove(track)
        else:
            pass

    def __repr__(self):
        return f"<User {self.user_name}, user id = {self.user_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.user_id == other.user_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.user_id < other.user_id

    def __hash__(self):
        return hash(self.user_id)


class Genre:
    def __init__(self, genre_id: int, genre_name: str):
        if type(genre_id) is not int or genre_id < 0:
            raise ValueError("Genre ID should be an integer!")
        self.__genre_id = genre_id

        self.__name: str | None = None

        self.__genre_tracks: list[Track] = []

        if type(genre_name) is str:
            self.__name = genre_name.strip()

    @property
    def genre_id(self) -> int:
        return self.__genre_id

    @property
    def name(self) -> str | None:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = None
        if type(name) is str:
            name = name.strip()
            if name != "":
                self.__name = name

    @property
    def track_genres(self) -> list:
        return self.__genre_tracks

    def add_track_genre(self, track: Track):
        if not isinstance(track, Track) or track in self.__genre_tracks:
            return
        self.__genre_tracks.append(track)

    def __repr__(self) -> str:
        return f"<Genre {self.name}, genre id = {self.genre_id}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.genre_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.genre_id < other.genre_id

    def __hash__(self):
        return hash(self.genre_id)


class Artist:
    def __init__(self, artist_id: int, full_name: str):
        if type(artist_id) is not int or artist_id < 0:
            raise ValueError("Arist ID should be a non negative integer!")
        self.__artist_id: int = artist_id

        self.__full_name: str | None = None
        if type(full_name) is str:
            self.__full_name = full_name.strip()

        self.__albums: list[Album] = []
        self.__tracks: list[Track] = []

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str | None:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = None

        if type(new_full_name) is str:
            new_full_name = new_full_name.strip()
            if new_full_name != "":
                self.__full_name = new_full_name

    @property
    def albums(self) -> list:
        return self.__albums

    @property
    def tracks(self) -> list:
        return self.__tracks

    @albums.setter
    def albums(self, new_albums: list):
        if type(new_albums) is not list:
            return
        self.__albums = new_albums

    @tracks.setter
    def tracks(self, new_tracks: list):
        if type(new_tracks) is not list:
            return
        self.__tracks = new_tracks

    def add_album(self, album: Album):
        if not isinstance(album, Album) or album in self.__albums:
            return
        self.__albums.append(album)

    def add_track(self, track: Track):
        if not isinstance(track, Track) or track in self.__tracks:
            return
        self.__tracks.append(track)

    def __repr__(self):
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.artist_id < other.artist_id

    def __hash__(self):
        return hash(self.__artist_id)
