class Settings:
    DB_USER = "postgres"
    DB_PASSWORD = "1234"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "postgres"

    database_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
