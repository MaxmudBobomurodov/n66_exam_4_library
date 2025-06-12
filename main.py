from core.table_quiries import initialize_tables
from crud.login import register, login
from crud.admin_functions import add_books_author , edit_books_author, delete_books
from crud.user_functions import show_books, search_books_by_author, rent_book, return_book, view_rented_books


def auth_menu():
    print("""
    1.Register
    2.Login
    3.exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        user = login()
        if user:
            main_menu(user)
    elif choice == "3":
        print("exit")
        return

def main_menu(user):
    username = user['username']
    is_admin = (username == "admin")

    if is_admin:
        print("""
        ADMIN MENU:
        1.show books
        2.Add new book and author
        3.Editing books
        4.Delete books
        5.Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            show_books()
        elif choice == "2":
            add_books_author()
        elif choice == "3":
            edit_books_author()
        elif choice == "4":
            delete_books()
        elif choice == "5":
            print("exit")
            return
        else:
            print("Invalid choice")
        main_menu(user)
    elif username:
        print("""
        USER MENU:
        1.Show list of books
        2.Search for books by author
        3.Rent a book
        4.Return book
        5.View your rentals
        6.Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            show_books()
        elif choice == "2":
            search_books_by_author()
        elif choice == "3":
            rent_book(user['id'])
        elif choice == "4":
            return_book(user['id'])
        elif choice == "5":
            view_rented_books(user['id'])
        elif choice == "6":
            print("exit")
            return
        main_menu(user)



if __name__ == '__main__':
    initialize_tables()
    auth_menu()