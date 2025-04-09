from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.postgres import schemas, crud
from app.postgres.utils.db import get_db

router = APIRouter(prefix="/articles", tags=["Articles"])

@router.post("/", response_model=schemas.ArticlesOut)
def create_article(articles: schemas.ArticlesCreate, db: Session = Depends(get_db)):
    return crud.create_articles(db, articles)

@router.get("/{article_id}", response_model=schemas.ArticlesOut)
def get_id_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_id_article(db, article_id)
    if not db_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return db_article

@router.get("/", response_model=list[schemas.ArticlesOut])
def get_all_articles(db: Session = Depends(get_db)):
    db_articles = crud.get_all_articles(db)
    if not db_articles:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return db_articles

@router.put("/{article_id}", response_model=schemas.ArticlesOut)
def update_article(article_id: int, article: schemas.ArticlesCreate, db:Session = Depends(get_db)):
    db_article = crud.update_article(db, article_id, article)
    if not db_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return db_article

@router.delete("/{article_id}", response_model=schemas.ArticlesOut)
def delete_article(article_id: int, db:Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id)
    if not db_article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")