from __future__ import annotations
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app import DemoUser
from app.forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.ejecutivo'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data
        if username == current_app.config['DEMO_USER'] and password == current_app.config['DEMO_PASSWORD']:
            user = DemoUser(id=1, username=username, nombre_completo=current_app.config['DEMO_FULL_NAME'])
            login_user(user, remember=form.remember.data)
            flash('Bienvenido al panel comercial.', 'success')
            next_url = request.args.get('next')
            return redirect(next_url or url_for('dashboard.ejecutivo'))
        flash('Credenciales invalidas.', 'danger')

    return render_template('login.html', form=form, title='Login')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesion cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))
