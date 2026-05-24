from __future__ import annotations
from dataclasses import dataclass
from flask import Flask, redirect, url_for
from flask_login import LoginManager, UserMixin
from flask_wtf import CSRFProtect
from app.config import Config

login_manager = LoginManager()
csrf = CSRFProtect()

@dataclass
class DemoUser(UserMixin):
    id: int
    username: str
    nombre_completo: str
    rol: str = 'admin'
    estado: str = 'activo'

    @property
    def is_active(self):
        return self.estado == 'activo'


def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Inicia sesion para continuar.'
    login_manager.login_message_category = 'warning'

    @login_manager.user_loader
    def load_user(user_id: str):
        if user_id == '1':
            return DemoUser(id=1, username=app.config['DEMO_USER'], nombre_completo=app.config['DEMO_FULL_NAME'])
        return None

    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    @app.route('/')
    def index():
        return redirect(url_for('dashboard.ejecutivo'))

    return app
