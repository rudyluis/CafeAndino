# Clase 2 - PostgreSQL + SQLAlchemy ORM + Migraciones

## Objetivo
Conectar Flask con PostgreSQL, definir modelos y crear tablas mediante migraciones.

## Pasos sugeridos
## MIGRACION
```bash

flask db init
flask db migrate -m "inicial"
flask db upgrade 


python -m venv venv
pip install -r requirements.txt
copy .env.example .env
flask db upgrade
flask db migrate -m "initial"   (recuerda que el nombre de la migracion debe ser unico)
flask create-admin
python run.py

Para crear un usuario
flask create-user --username juan --email juan@correo.com --password 123456 --full-name "Juan Perez" --rol usuario


```

## Que incluye
- Modelos `Usuario`, `Venta`, `BitacoraAcceso`
- Login contra PostgreSQL
- Migracion inicial
