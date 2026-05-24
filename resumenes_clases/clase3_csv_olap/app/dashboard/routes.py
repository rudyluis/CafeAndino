from __future__ import annotations
from decimal import Decimal
from flask import Blueprint, render_template
from flask_login import login_required
from sqlalchemy import desc, func
from app import db
from app.models import Venta

dashboard_bp = Blueprint('dashboard', __name__)

def to_float(value):
    if value is None:
        return 0.0
    if isinstance(value, Decimal):
        return float(value)
    return float(value)

@dashboard_bp.route('/ejecutivo')
@login_required
def ejecutivo():
    total_neto = db.session.query(func.sum(Venta.total_neto)).scalar() or 0
    total_bruto = db.session.query(func.sum(Venta.total_bruto)).scalar() or 0
    total_registros = db.session.query(func.count(Venta.id)).scalar() or 0
    top_categoria = (
        db.session.query(Venta.categoria_producto, func.sum(Venta.total_neto).label('total'))
        .group_by(Venta.categoria_producto)
        .order_by(desc('total'))
        .first()
    )
    resumen = (
        db.session.query(Venta.categoria_producto, func.sum(Venta.total_neto).label('total'))
        .group_by(Venta.categoria_producto)
        .order_by(desc('total'))
        .limit(8)
        .all()
    )
    kpis = [
        {'title': 'Ventas netas', 'value': f"Bs {to_float(total_neto):,.2f}", 'icon': 'fa-chart-line', 'tone': 'gold'},
        {'title': 'Ventas brutas', 'value': f"Bs {to_float(total_bruto):,.2f}", 'icon': 'fa-cash-register', 'tone': 'coffee'},
        {'title': 'Registros', 'value': f"{int(total_registros):,}", 'icon': 'fa-table', 'tone': 'olive'},
        {'title': 'Categoria top', 'value': top_categoria[0] if top_categoria else 'Sin datos', 'icon': 'fa-crown', 'tone': 'caramel'},
    ]
    return render_template('dashboard1.html', title='Clase 3 - CSV y OLAP', dashboard='ejecutivo', kpis=kpis, resumen=resumen)
