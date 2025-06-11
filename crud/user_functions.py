from core.database_settings import execute_query
from datetime import datetime
def show_books():

    query = """SELECT b.id , b.title, a.full_name as author, b.puplished_at, b.total_count, b.available_count
                FROM books b join authors a on b.author_id=a.id;
"""
    books = execute_query(query, fetch="all")

    if not books:
        print("books not available .")
        return
    for book in books:
        print(f"""
        Id : {book[0]}
        Title: {book[1]}
        Author: {book[2]}
        published_at: {book[3]}
        total_count: {book[4]}
        available_count: {book[5]}
        """)

def search_books_by_author():
    author_name = input("Enter author name: ").strip()

    query = """SELECT b.id, b.title, a.full_name as author, b.puplished_at, b.total_count, b.available_count
    FROM books b JOIN authors a on b.author_id=a.id
    where a.full_name=%s;"""
    params = (author_name,)
    books = execute_query(query, params, "all")
    if not books:
        print("books not available .")
        return

    for book in books:
        print(f"""
        Id : {book[0]}
        Title: {book[1]}
        Author: {book[2]}
        published_at: {book[3]}
        total_count: {book[4]}
        available_count: {book[5]}
        """)

def rent_book(user_id):
    book_id = int(input("Enter book id: "))
    existing = execute_query(f"SELECT id FROM books WHERE id=%s AND available_count>0",(book_id,) ,fetch="one")
    if not existing:
        print("book not available .")
        return
    query = """INSERT INTO borrows (user_id, book_id, borrowed_at) VALUES (%s, %s, %s);"""
    params = (user_id , book_id, datetime.now())
    execute_query(query, params)

    execute_query("UPDATE books SET available_count=available_count-1 WHERE id=%s",(book_id,))
    for row in existing:
        print(f"you have successfully rented this book.")