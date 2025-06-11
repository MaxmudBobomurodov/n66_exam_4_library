from core.table_quiries import initialize_tables
from crud.login import register, login
from crud.admin_functions import add_books_author , edit_books_author, delete_books
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
        1.Add new book and author
        2.Editing books
        3.Delete books
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_books_author()
        elif choice == "2":
            edit_books_author()
        elif choice == "3":
            delete_books()
        else:
            print("Invalid choice")
        auth_menu()
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
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("exit")
            return




if __name__ == '__main__':
    initialize_tables()
    auth_menu()