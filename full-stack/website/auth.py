from flask import Blueprint, render_template, redirect, url_for, request, flash
from .forms import SignUp, Login
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, current_user, login_required, logout_user
from .token import generation_confirmation_token, confirm_token

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('views.homepage', user=current_user))
            else:
                flash("Nome utente o password errati. Si prega di verificare e riprovare.")
        else:
            flash("Nome utente o password errati. Si prega di verificare e riprovare.")

    return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()

    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data, method='pbkdf2:sha256'),
            confirmed=False
            )
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)

        return redirect(url_for('views.homepage', user=current_user))


    return render_template('auth/signup.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.homepage'))

@auth.route('/activate')
def activate():

    # Create a token when a user complete the registration form
    token = generation_confirmation_token(current_user.email)
    confirm_url = url_for('auth.confirm_email', token=token, _external=True)
    print(token)
    return render_template('auth/activate.html', confirm_url=confirm_url)

@auth.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        print('Errore')
    user = User.query.filter_by(email=email).first()

    if user.confirmed:
        print('Account già confermato')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
    return redirect(url_for('views.homepage'))