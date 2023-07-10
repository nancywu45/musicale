from datetime import date

from flask import Blueprint, redirect, session
from flask_wtf import FlaskForm
from flask import request, render_template, url_for
from wtforms import TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

from music.domainmodel.model import Review
from music.domainmodel.model import User

from .services import add_review, get_reviews, get_track, get_user
import music.adapters.repository as repo
from music.authentication.authentication import login_required

# Configure Blueprint.
review_blueprint = Blueprint("review_bp", __name__)


@review_blueprint.route("/details", methods=["GET", "POST"])
@login_required
def review():
    track_id = request.args.get("track_id", 1, type=int)
    track = get_track(track_id, repo.repo_instance)

    form = ReviewForm()
    if form.validate_on_submit():
        review_text = form.review_text.data
        rating = form.rating.data
        user: User = get_user(repo.repo_instance, session["user_name"])
        review: Review = Review(track, review_text, rating, user)
        add_review(repo.repo_instance, review, track)
        user.add_review(review)

    reviews = get_reviews(track)
    return render_template(
        "review/review.html",
        track=track,
        form=form,
        reviews=reviews,
        handler_url=url_for("review_bp.review", track_id=track_id),
    )


class ReviewForm(FlaskForm):
    review_text = TextAreaField(
        "Review", [DataRequired(message="Please enter a review")]
    )
    rating = IntegerField(
        "Rating",
        [
            DataRequired("Please enter a rating"),
            NumberRange(min=1, max=5, message="Please enter a rating between 1 and 5"),
        ],
    )
    submit = SubmitField("Submit")
