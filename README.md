Una REST API per la gestione di articoli, sviluppata con FastAPI, SQLAlchemy e PostgresSQL. 
Supporta operazioni CRUD: create, get, put e delete di articoli.

Requisiti:

- Python 3.10+
- PostgreSQL installato e in esecuzione

Clona il progetto:

git clone https://github.com/ChiocciolaVicenzo/FastAPI-PostgreSQL-CRUD-API.git

Crea un Venv sul terminale:

python -m venv venv

Installa le dipendenze:

pip install -r requirements.txt

Fare l'injection e nell'Environment Variables mettere la variabile del DATABASE_URL:

- Su Pycharm: 
Andare su Run->Edit Configurations...->Aggiungi Python e mettere script (main.py), la directory e alla fine le variabili del DATABASE_URL: postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE}

- Su VSCode:
Andare su Run->Add Configuration...->python->aggiungere "env":{"DATABASE_URL" : "postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE}"} 

Avvio dell'applicazione:

- Su Pycharm:
    Basta startare lo script che hai aggiunto tramite injection

- Su vscode (sul terminale):
    $env:DATABASE_URL="postgresql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE}"; python main.py

Come vedere la documentazione Swagger:

http://127.0.0.1:8000/docs
