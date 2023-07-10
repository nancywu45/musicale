"""Initialize Flask app."""

from pathlib import Path
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool
from music.adapters.database_repository import SqlAlchemyRepository

import music.adapters.repository as repo
from music.adapters.memory_repository import MemoryRepository
from music.adapters.repository_populate import populate
from music.adapters.orm import metadata, map_model_to_tables


def create_app(test_config=None):
    app = Flask(__name__)
    # Configure the app from configuration-file settings.
    app.config.from_object("config.Config")
    data_path = Path("music") / "adapters" / "data"

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()

    if test_config is not None:
        # Load test data.
        app.config.from_mapping(test_config)
        # data_path = app.config["TEST_DATA_PATH"]

    if app.config["REPOSITORY"] == "memory":
        repo.repo_instance = MemoryRepository()
        populate(data_path, repo.repo_instance)

    elif app.config["REPOSITORY"] == "database":
        database_uri = app.config["SQLALCHEMY_DATABASE_URI"]

        database_echo = app.config["SQLALCHEMY_ECHO"]
        # Please do not change the settings for connect_args and poolclass!
        database_engine = create_engine(
            database_uri,
            connect_args={"check_same_thread": False},
            poolclass=NullPool,
            echo=database_echo,
        )

        session_factory = sessionmaker(
            autocommit=False, autoflush=True, bind=database_engine
        )
        repo.repo_instance = SqlAlchemyRepository(session_factory)

        if app.config["TESTING"] == "True" or len(database_engine.table_names()) == 0:
            clear_mappers()
            metadata.create_all(database_engine)
            for table in reversed(metadata.sorted_tables):
                database_engine.execute(table.delete())

            map_model_to_tables()

            populate(data_path, repo.repo_instance)
        else:
            map_model_to_tables()

    with app.app_context():
        # Import and register the blueprints here
        from .home import home

        app.register_blueprint(home.home_blueprint)

        from .review import review

        app.register_blueprint(review.review_blueprint)

        from .playlist import playlist

        app.register_blueprint(playlist.playlist_blueprint)

        from .tracks import tracks

        app.register_blueprint(tracks.tracks_blueprint)

        from .authentication import authentication

        app.register_blueprint(authentication.authentication_blueprint)

        # @app.before_request
        # def before_flask_http_request_function():
        #     if isinstance(repo.repo_instance, SqlAlchemyRepository):
        #         repo.repo_instance.reset_session()

        # @app.teardown_appcontext
        # def shutdown_session(exception=None):
        #     if isinstance(repo.repo_instance, SqlAlchemyRepository):
        #         repo.repo_instance.close_session()

    return app
