from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.db.db import SessionLocal
from app.db import crud
from app.schemas import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[BookResponse])
def list_books(category_id: Optional[int] = None, db=Depends(get_db)):
    books = crud.get_books(db)
    if category_id:
        books = [b for b in books if b.category_id == category_id]
    return books

@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db=Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(data: BookCreate, db=Depends(get_db)):
    cat = crud.get_category(db, data.category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return crud.create_book(db, data.title, data.description,
                            data.price, data.url, data.category_id)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, data: BookCreate, db=Depends(get_db)):
    book = crud.update_book(db, book_id, **data.model_dump())
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db=Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"detail": "Удалено"}
