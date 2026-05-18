from flask import Blueprint, redirect, url_for

data_bp = Blueprint('data', __name__)

@data_bp.route('/importar')
def importar():
    return redirect(url_for('dashboard.ejecutivo'))
