from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from flask_login import LoginManager
from secrets import SystemRandom

db = SQLAlchemy()
DIRNAME = Path.cwd()

# Generation of security_password_salt
# result = SystemRandom().getrandbits(128)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'supersafekey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DIRNAME}/database.db'
    app.config['SECURITY_PASSWORD_SALT'] = '49500638755478474074859624111180149435'

    db.init_app(app)


    from .user import user
    from .views import views
    from .auth import auth
    from .admin import admin
    app.register_blueprint(user, url_prefix='/user/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin/')

    from .models import User
    from .models import Review
    from .models import Staff

    # Handling errors
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    with app.app_context():
        # db.drop_all()
        db.create_all()
        # from .fake_data import add_fake_data
        # add_fake_data()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Si prega di effettuare l\'accesso prima di continuare.'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()

    return app