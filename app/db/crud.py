from app.db.models import Book, Category

# ===== CATEGORIES =====

def create_category(session, title):
    category = Category(title=title)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_categories(session):
    return session.query(Category).all()

def get_category(session, category_id):
    return session.query(Category).filter(Category.id == category_id).first()

def update_category(session, category_id, title):
    category = get_category(session, category_id)
    if category:
        category.title = title
        session.commit()
        session.refresh(category)
    return category

def delete_category(session, category_id):
    category = get_category(session, category_id)
    if category:
        session.delete(category)
        session.commit()
    return category

# ===== BOOKS =====

def create_book(session, title, description, price, url, category_id):
    book = Book(title=title, description=description,
                price=price, url=url, category_id=category_id)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def get_books(session):
    return session.query(Book).all()

def get_book(session, book_id):
    return session.query(Book).filter(Book.id == book_id).first()

def update_book(session, book_id, **kwargs):
    book = get_book(session, book_id)
    if book:
        for key, value in kwargs.items():
            setattr(book, key, value)
        session.commit()
        session.refresh(book)
    return book

def delete_book(session, book_id):
    book = get_book(session, book_id)
    if book:
        session.delete(book)
        session.commit()
    return book
