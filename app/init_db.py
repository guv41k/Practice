from app.db.db import engine, Base, SessionLocal
from app.db.models import Book, Category
from app.db.crud import create_category, create_book

# Создаём таблицы
Base.metadata.create_all(bind=engine)

session = SessionLocal()

# Две категории
cat1 = create_category(session, "Программирование")
cat2 = create_category(session, "Фантастика")

# 2-4 книги в каждую
create_book(session, "Python для начинающих", "Основы Python", 590.0, "", cat1.id)
create_book(session, "Clean Code", "Чистый код Роберта Мартина", 750.0, "", cat1.id)
create_book(session, "Дюна", "Классика научной фантастики", 450.0, "", cat2.id)
create_book(session, "Марсианин", "Выживание на Марсе", 380.0, "", cat2.id)

print("База данных заполнена!")
session.close()
