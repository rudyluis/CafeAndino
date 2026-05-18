from __future__ import annotations
from flask import Blueprint, render_template
from flask_login import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/ejecutivo')
@login_required
def ejecutivo():
    kpis = [
        {'title': 'Ventas netas', 'value': 'Bs 0.00', 'icon': 'fa-chart-line', 'tone': 'gold'},
        {'title': 'Clientes', 'value': '0', 'icon': 'fa-users', 'tone': 'olive'},
        {'title': 'Productos', 'value': '0', 'icon': 'fa-boxes-stacked', 'tone': 'coffee'},
        {'title': 'Ticket promedio', 'value': 'Bs 0.00', 'icon': 'fa-receipt', 'tone': 'caramel'},
    ]
    return render_template('dashboard1.html', title='Dashboard Base', dashboard='ejecutivo', kpis=kpis)
