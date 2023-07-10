from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import mapper, relationship, synonym

from music.domainmodel.model import Artist
from music.domainmodel.model import Album
from music.domainmodel.model import Genre
from music.domainmodel.model import Track
from music.domainmodel.model import Review
from music.domainmodel.model import Track
from music.domainmodel.model import User


metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
)

artists_table = Table(
    "artists",
    metadata,
    Column("artist_id", Integer, primary_key=True, autoincrement=True),
    Column("full_name", String(255), nullable=False),
)

albums_table = Table(
    "albums",
    metadata,
    Column("album_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), nullable=True),
    Column("release_year", Integer, nullable=True),
    Column("album_url", String(255), nullable=True),
    Column("album_type", String(255), nullable=True),
    Column("album_image_url", String(255), nullable=True),
    Column("artist_id", ForeignKey("artists.artist_id"), nullable=True),
)

genres_table = Table(
    "genres",
    metadata,
    Column("genre_id", Integer, primary_key=True, autoincrement=True),
    Column("genre_name", String(255), nullable=True),
)

tracks_table = Table(
    "tracks",
    metadata,
    Column("track_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), nullable=True),
    Column("track_url", String(255), nullable=True),
    Column("track_duration", Integer, nullable=True),
    Column("track_image_url", String(255), nullable=True),
    Column("track_audio_url", String(255), nullable=True),
    Column("album_id", Integer, ForeignKey("albums.album_id"), nullable=True),
    Column("artist_id", Integer, ForeignKey("artists.artist_id"), nullable=True),
)

tracks_genre_table = Table(
    "tracks_genre",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("track_id", Integer, ForeignKey("tracks.track_id")),
    Column("genre_id", Integer, ForeignKey("genres.genre_id")),
)

users_track_table = Table(
    "users_track",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.user_id")),
    Column("track_id", Integer, ForeignKey("tracks.track_id")),
)

reviews_table = Table(
    "reviews",
    metadata,
    Column("review_id", Integer, primary_key=True, autoincrement=True),
    Column("review_text", String(255), nullable=True),
    Column("track_id", Integer, ForeignKey("tracks.track_id")),
    Column("rating", Integer, nullable=True),
    Column("timestamp", DateTime, nullable=True),
    Column("user_id", Integer, ForeignKey("users.user_id")),
)


def map_model_to_tables():

    mapper(
        User,
        users_table,
        properties={
            "_User__user_id": users_table.c.user_id,
            "_User__user_name": users_table.c.user_name,
            "_User__password": users_table.c.password,
            "_User__reviews": relationship(Review, backref="_Review__user"),
            "_User__tracks": relationship(
                Track, secondary=users_track_table, back_populates="_Track__users"
            ),
        },
    ),

    mapper(
        Review,
        reviews_table,
        properties={
            "_Review__review_text": reviews_table.c.review_text,
            "_Review__rating": reviews_table.c.rating,
            "_Review__timestamp": reviews_table.c.timestamp,
        },
    ),

    mapper(
        Artist,
        artists_table,
        properties={
            "_Artist__artist_id": artists_table.c.artist_id,
            "_Artist__full_name": artists_table.c.full_name,
            "_Artist__albums": relationship(Album, backref="_Album__artist"),
            "_Artist__tracks": relationship(Track, backref="_Track__artist"),
        },
    )

    mapper(
        Album,
        albums_table,
        properties={
            "_Album__album_id": albums_table.c.album_id,
            "_Album__title": albums_table.c.title,
            "_Album__release_year": albums_table.c.release_year,
            "_Album__album_url": albums_table.c.album_url,
            "_Album__album_type": albums_table.c.album_type,
            "_Album__album_image_url": albums_table.c.album_image_url,
            "_Album__tracks": relationship(Track, backref="_Track__album"),
        },
    )

    mapper(
        Genre,
        genres_table,
        properties={
            "_Genre__genre_id": genres_table.c.genre_id,
            "_Genre__name": genres_table.c.genre_name,
            "_Genre__genre_tracks": relationship(
                Track,
                secondary=tracks_genre_table,
                back_populates="_Track__genres",
            ),
        },
    )

    mapper(
        Track,
        tracks_table,
        properties={
            "_Track__track_id": tracks_table.c.track_id,
            "_Track__title": tracks_table.c.title,
            "_Track__track_url": tracks_table.c.track_url,
            "_Track__track_duration": tracks_table.c.track_duration,
            "_Track__track_image_url": tracks_table.c.track_image_url,
            "_Track__track_audio_url": tracks_table.c.track_audio_url,
            "_Track__genres": relationship(
                Genre,
                secondary=tracks_genre_table,
                back_populates="_Genre__genre_tracks",
            ),
            "_Track__reviews": relationship(Review, backref="_Review__track"),
            "_Track__users": relationship(
                User, secondary=users_track_table, back_populates="_User__tracks"
            ),
        },
    )
