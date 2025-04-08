Una REST API per la gestione di articoli, sviluppata con FastAPI, SQLAlchemy e PostgresSQL. 
Supporta operazioni CRUD: create, get, put e delete di articoli.

Requisiti:
- Python 3.10+
- PostgreSQL

Clona il progetto:

git clone https://github.com/ChiocciolaVicenzo/FastAPI-PostgreSQL-CRUD-API.git
cd FastAPI-PostgreSQL-CRUD-API

Crea un Venv sul terminale:
python -m venv venv

Installa le dipendenze:
pip install -r requirements.txt

Crea un file .env con la connessione al DB:
DATABASE_URL=postgresql://user:password@localhost:5432/tuo_database

Avvio dell'applicazione:
uvicorn main:app --reload
