from functools import wraps
from flask_login import current_user
from flask import redirect, url_for

# Decorator for routes that require the account confirmation by user
def confirm_required(f):
    wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.confirmed:
            return redirect(url_for('auth.activate'))
        else: 
            pass
        return f(*args, **kwargs)
    return wrapper

# Decorator for routes that require an admin login, these routes are not available for common users
def admin_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if current_user.email:
            if current_user.email == 'admin':
                return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper