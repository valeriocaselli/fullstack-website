from flask import Blueprint, render_template, url_for
from flask_login import current_user
from .models import Review
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/homepage')
def homepage():
    reviews = Review.query.filter(Review.value >= 4).all()
    return render_template('homepage.html', user=current_user, reviews=reviews)

@views.route('/reviews')
def reviews():
    reviews = Review.query.all()
    print(reviews)
    return render_template('reviews.html', reviews=reviews, user=current_user)