# Clase 4 - Dashboard SaaS completo

Proyecto completo con:
- Flask + Blueprints
- PostgreSQL + SQLAlchemy ORM
- Login seguro
- Importacion CSV
- APIs para filtros y paneles
- 3 dashboards: Ejecutivo, Clientes y Productos/OLAP
- Chart.js + DataTables + UI responsive

## Puesta en marcha
```bash
pip install -r requirements.txt
copy .env.example .env
flask db upgrade
flask create-admin
flask import-csv --path dataset_cafe_andino.csv
python run.py
```
