from flask import Blueprint, render_template, request, redirect, url_for, session
import music.adapters.repository as repo
from music.tracks.services import get_user
from music.playlist.services import (
    delete_track_from_playlist,
    get_playlist_tracks,
    get_genres,
)
from music.authentication.authentication import login_required

playlist_blueprint: Blueprint = Blueprint("playlist_bp", __name__)

genres = get_genres(repo.repo_instance)


@playlist_blueprint.route("/playlist", methods=["GET"])
@login_required
def playlist() -> str:
    user = get_user(repo.repo_instance, session["user_name"])
    tracks = get_playlist_tracks(user)

    playlist_track_id = request.args.get("delete_track_id", type=int)
    if playlist_track_id:
        delete_track_from_playlist(repo.repo_instance, user, playlist_track_id)

    return render_template("playlist/playlist.html", tracks=tracks[:30])
