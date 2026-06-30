from fastapi import APIRouter, HTTPException
from app.db.db import SessionLocal
from app.db import crud
from app.schemas import CategoryCreate, CategoryResponse
from typing import List

router = APIRouter(prefix="/categories", tags=["Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends

@router.get("/", response_model=List[CategoryResponse])
def list_categories(db=Depends(get_db)):
    return crud.get_categories(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db=Depends(get_db)):
    cat = crud.get_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return cat

@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(data: CategoryCreate, db=Depends(get_db)):
    return crud.create_category(db, data.title)

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryCreate, db=Depends(get_db)):
    cat = crud.update_category(db, category_id, data.title)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return cat

@router.delete("/{category_id}")
def delete_category(category_id: int, db=Depends(get_db)):
    cat = crud.delete_category(db, category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return {"detail": "Удалено"}
