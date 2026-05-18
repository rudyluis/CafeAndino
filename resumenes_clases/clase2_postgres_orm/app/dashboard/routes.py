from __future__ import annotations
from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import func
from app import db
from app.models import Usuario, Venta

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/ejecutivo')
@login_required
def ejecutivo():
    total_usuarios = db.session.query(func.count(Usuario.id)).scalar() or 0
    total_ventas = db.session.query(func.count(Venta.id)).scalar() or 0
    kpis = [
        {'title': 'Usuarios', 'value': str(total_usuarios), 'icon': 'fa-users', 'tone': 'gold'},
        {'title': 'Ventas cargadas', 'value': str(total_ventas), 'icon': 'fa-database', 'tone': 'coffee'},
        {'title': 'Modelo Usuario', 'value': 'OK', 'icon': 'fa-table', 'tone': 'olive'},
        {'title': 'Migraciones', 'value': 'Activas', 'icon': 'fa-code-branch', 'tone': 'caramel'},
    ]
    return render_template('dashboard1.html', title='Clase 2 - ORM', dashboard='ejecutivo', kpis=kpis)
