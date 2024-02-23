from flask import Blueprint, render_template, jsonify
from .decorators import confirm_required
from flask_login import current_user, login_required
from datetime import datetime, timedelta
from .forms import ReviewForm
from .models import Review

user = Blueprint('user', __name__)

@user.route('/bookings')
@login_required
# @confirm_required
def bookings():
    return render_template('user/bookings.html', user=current_user)

@user.route('/available_days', methods=['GET', 'POST'])
def available_days():
    # days = []
    # months = []
    days = {}
    today = datetime.now()
    tomorrow = datetime.now()
    today_str = today.strftime('%d-%m-%Y')
    for i in range(1, 22):
        next_day = today + timedelta(i)
        next_day = next_day.strftime('%d-%m-%Y')
        month = int(next_day.split('-')[1])
        if month not in days:
            days[month] = [next_day]
        else:
            days[month].append(next_day)
    print(days)

    return jsonify(data=days)

@user.route('/write_review', methods=['GET', 'POST'])
def write_review():
    form = ReviewForm()

    if form.validate_on_submit():
        new_review = Review(
            value=form.value.data,
            description=form.description.data,
            user_id=current_user.id
        )

    return render_template('user/write_review.html', form=form)