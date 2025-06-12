from core.database_settings import execute_query
from crud.user_functions import show_books

def add_books_author():
    author_name = input("Enter author full name: ")
    query = "INSERT INTO authors (full_name) VALUES (%s) RETURNING id;"
    params = (author_name,)
    author_result = execute_query(query, params, fetch='one')
    author_id = author_result['id']

    title = input("Enter book title: ")
    puplished_at = input("Enter published date (yyyy-mm-dd): ")
    total_count = int(input("Enter total count of books: "))
    available_count = int(input("Enter available count of books: "))
    books_query = "INSERT INTO books (title,author_id, puplished_at, total_count, available_count) VALUES (%s, %s, %s, %s, %s)"
    params = (title, author_id, puplished_at, total_count, available_count)
    execute_query(books_query, params)
    print("Successfully added books and author .")

def edit_books_author():
    show_books()
    book_id = int(input("Enter book id: "))
    book_existing = execute_query("SELECT * FROM books WHERE id = %s", (book_id,), fetch='one')
    if not book_existing:
        print("There is no this kind of book.")
        return


    print("""
    1.Change author name
    2.Change title
    3.Change puplished date
    4.Change total count
    5.Change available count
    6.Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        author_name = input("Enter author full name: ")
        author_data = execute_query("SELECT author_id FROM books WHERE id = %s", (book_id,), fetch='one')
        if not author_data or not author_data['author_id']:
            print("Book not found")
            return
        author_id = author_data['author_id']

        query = "UPDATE authors SET full_name = %s WHERE id = %s;"
        params = (author_name, author_id)
        execute_query(query, params)
        print("Successfully changed author name.")

    elif choice == "2":
        new_title = input("Enter new book title: ")
        query = "UPDATE books SET title = %s WHERE id = %s;"
        params = (new_title, book_id)
        execute_query(query, params)
        print("Successfully changed book title.")


    elif choice == "3":
        new_published_at = input("Enter published date (yyyy-mm-dd): ")
        query = "UPDATE books SET puplished_at = %s WHERE id = %s;"
        params = (new_published_at, book_id)
        execute_query(query, params)
        print("Successfully changed published date.")


    elif choice == "4":
        new_total_count = input("Enter new total count of books: ")
        available_count = execute_query("SELECT available_count FROM books WHERE id = %s", (book_id,), fetch='one')

        if int(new_total_count) > int(available_count['available_count']):
            query = "UPDATE books SET total_count = %s WHERE id = %s;"
            params = (new_total_count, book_id)
            execute_query(query, params)
            print("Successfully changed total count.")
        else:
            print("You cannot change total count if it is smaller than available count.")
            return


    elif choice == "5":
        new_available_count = input("Enter new available count of books: ")
        total_count = execute_query("SELECT total_count FROM books WHERE id = %s", (book_id,), fetch='one')


        if int(new_available_count) < int(total_count['total_count']):
            query = "UPDATE books SET available_count = %s WHERE id = %s;"
            params = (new_available_count, book_id)
            execute_query(query, params)
            print("Successfully changed available count.")
        else:
            print("You cannot change available count if it is bigger than total count.")
            return


    elif choice == "6":
        print("exit")
        return


def delete_books():
    book_id = int(input("Enter book id: "))
    query = "DELETE FROM books WHERE id = %s;"
    params = (book_id,)
    execute_query(query, params)
    print("Successfully deleted books.")



