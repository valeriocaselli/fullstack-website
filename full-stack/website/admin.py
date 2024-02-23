from flask import Blueprint, render_template, request, make_response
from .decorators import admin_login_required
from .forms import AdminLogin

admin = Blueprint('admin', __name__)

@admin.route('/login', methods=['GET', 'POST'])
def admin_login():

    form = AdminLogin()

    if form.validate_on_submit():
        print('Admin')

    return render_template('admin/admin_login.html', form=form)