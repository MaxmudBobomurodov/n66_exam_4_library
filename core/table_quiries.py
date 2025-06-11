from core.database_settings import execute_query



authors = """
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL
);
"""
books = """
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER REFERENCES authors(id),
    puplished_at TIMESTAMP,
    total_count INTEGER,
    available_count INTEGER
);"""


users = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""

borrows = """
CREATE TABLE IF NOT EXISTS borrows (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    book_id INTEGER REFERENCES books(id),
    borrowed_at TIMESTAMP,
    returned_at TIMESTAMP
);
"""

def initialize_tables():
    execute_query(query=authors)
    execute_query(query=books)
    execute_query(query=users)
    execute_query(query=borrows)