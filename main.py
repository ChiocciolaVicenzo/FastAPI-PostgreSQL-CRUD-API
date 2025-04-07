from fastapi import FastAPI
from app.postgres.utils.db import Base, engine
from app.routes.articles import router as articles

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(articles)