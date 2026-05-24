# Clase 3 - CSV + Services + Consultas OLAP

## Objetivo
Importar el dataset CSV, separar la logica en services y construir consultas agregadas con SQLAlchemy.

## Flujo sugerido
```bash
pip install -r requirements.txt
copy .env.example .env
flask db upgrade
flask create-admin
flask import-csv --path dataset_cafe_andino.csv
python run.py
```

Tambien se puede importar desde `/data/importar` iniciando sesion como admin.
