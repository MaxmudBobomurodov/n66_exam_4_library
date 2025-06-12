from core.database_settings import execute_query

def register():
    full_name = input("Enter your full name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    existing_user = execute_query(
        "SELECT * FROM users WHERE username = %s", (username,), fetch="one"
    )
    if existing_user:
        print("Username already exists.")
        return

    query = "INSERT INTO users (full_name, username, password) VALUES (%s, %s, %s)"
    execute_query(query, (full_name, username, password))
    print("Registered successfully! Please login again.")

def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")

    user = execute_query(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, password),
        fetch="one"
    )
    if user:
        if user['username'] == 'admin':
            print("you are logged in as admin.")
        else:
            print(f"Welcome, {user['full_name']}")
        return user
    else:
        print("Login failed.")
        return None