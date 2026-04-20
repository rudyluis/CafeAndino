# Cafe Andino Analytics

Aplicacion web Flask para analitica comercial de una empresa de cafe. Incluye login, roles, importacion CSV a PostgreSQL, consultas ORM agregadas, dashboards Chart.js y tablas DataTables.

## Requisitos

- Python 3.11+
- PostgreSQL
- Base de datos creada, por ejemplo `cafe_andino`

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edita `.env` y configura `DATABASE_URL`, `SECRET_KEY` y las credenciales `ADMIN_*`.

## Base de datos

Aplica la migracion inicial incluida y crea tablas:

```powershell
$env:FLASK_APP="run.py"
flask db upgrade
```

Cuando cambies modelos despues, genera nuevas revisiones con `flask db migrate -m "descripcion"` y aplica con `flask db upgrade`.

## Usuario administrador

```powershell
flask create-admin
```

El comando crea o actualiza el administrador usando las variables del archivo `.env`. La contrasena se almacena con hash de Werkzeug.

## Importar ventas

Importacion inicial desde CLI:

```powershell
flask import-csv --path dataset_cafe_andino.csv
```

La importacion valida columnas, convierte tipos, inserta con SQLAlchemy ORM y omite duplicados por `id_venta_csv`.

Tambien puedes cargar CSV desde la interfaz en `/data/importar` con un usuario `admin`.

## Ejecutar

```powershell
flask run
```

Abre `http://127.0.0.1:5000/login`.

## Dashboards

- Ejecutivo: `/dashboard/ejecutivo`
- Clientes: `/dashboard/clientes`
- Productos / OLAP: `/dashboard/productos`

Cada dashboard incluye filtros dinamicos, KPIs, cuatro graficos Chart.js y una tabla DataTables con busqueda, paginacion, ordenamiento y exportacion.

## Seguridad

- Login con Flask-Login.
- CSRF con Flask-WTF.
- Password hashing con Werkzeug.
- Rutas protegidas con `login_required`.
- Acceso admin para importacion CSV.
- Variables sensibles en `.env`.
- Consultas de datos mediante SQLAlchemy ORM.
