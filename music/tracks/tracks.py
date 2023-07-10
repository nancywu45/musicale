from flask import Blueprint, render_template, request, redirect, url_for, session
import music.adapters.repository as repo
from music.tracks.services import (
    get_tracks,
    get_genres,
    get_user,
    add_track_to_playlist,
)
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf import FlaskForm
from music.authentication.authentication import login_required

tracks_blueprint: Blueprint = Blueprint("tracks_bp", __name__)
tracks = get_tracks(repo.repo_instance)
genres = get_genres(repo.repo_instance)


@tracks_blueprint.route("/tracks", methods=["GET"])
@login_required
def tracks_list() -> str:
    number_of_tracks_to_show = request.args.get("number_of_tracks", default=8, type=int)
    selected_genre_id = request.args.get("genre_id", default=0, type=int)
    playlist_track_id = request.args.get("playlist_track_id", type=int)
    user = get_user(repo.repo_instance, session["user_name"])
    if playlist_track_id:
        add_track_to_playlist(repo.repo_instance, user, playlist_track_id)

    if selected_genre_id != 0:
        tracks_to_show = []
        for track in tracks:
            if track.genres and track.genres[0].genre_id == selected_genre_id:
                tracks_to_show.append(track)
    else:
        tracks_to_show = tracks

    form = TrackNumberForm()

    if form.validate_on_submit():
        number_of_tracks_to_show = form.number_of_tracks.data
        return redirect(
            url_for("tracks_bp.home", number_of_tracks=number_of_tracks_to_show)
        )
    return render_template(
        "tracks/tracks.html",
        tracks=tracks_to_show[:number_of_tracks_to_show],
        form=form,
        genres=genres,
        selected_genre_id=selected_genre_id,
    )


class TrackNumberForm(FlaskForm):
    number_of_tracks = IntegerField(
        "Number of tracks to show",
        [
            DataRequired(message="Please enter a number"),
            NumberRange(
                min=8,
                max=len(tracks),
                message=f"Please enter a number between 8 and {len(tracks)}",
            ),
        ],
    )
    submit = SubmitField("Change")
