# Clase 2 - PostgreSQL + SQLAlchemy ORM + Migraciones

## Objetivo
Conectar Flask con PostgreSQL, definir modelos y crear tablas mediante migraciones.

## Pasos sugeridos
```bash
python -m venv venv
pip install -r requirements.txt
copy .env.example .env
flask db upgrade
flask create-admin
python run.py
```

## Que incluye
- Modelos `Usuario`, `Venta`, `BitacoraAcceso`
- Login contra PostgreSQL
- Migracion inicial
