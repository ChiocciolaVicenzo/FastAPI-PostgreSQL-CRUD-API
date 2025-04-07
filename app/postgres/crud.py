from sqlalchemy.orm import Session
import app.postgres.schemas as schemas, app.postgres.models as models

def create_articles(db: Session, article: schemas.ArticlesCreate):
    db_article = models.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_id_article(db:Session, article_id:int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def get_all_articles(db: Session):
    return db.query(models.Article).all()

def update_article(db: Session, article_id: int, article: schemas.ArticlesCreate):
    db_article = get_id_article(db, article_id)
    if db_article:
        for key, value in article.model_dump().items():
            setattr(db_article, key, value)
        db.commit()
        db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = get_id_article(db, article_id)
    if db_article:
        db.delete(db_article)
        db.commit()
    return db_article