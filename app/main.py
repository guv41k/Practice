from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

session = SessionLocal()

print("=== КАТЕГОРИИ ===")
for cat in get_categories(session):
    print(f"  [{cat.id}] {cat.title}")

print("\n=== КНИГИ ===")
for book in get_books(session):
    print(f"  [{book.id}] {book.title} | {book.price} руб. | Категория ID: {book.category_id}")

session.close()
