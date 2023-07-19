users = [
    {"name": "NodeA", "password": "1234", "PORT": 5000},
    {"name": "NodeB", "password": "1234", "PORT": 6000},
    {"name": "NodeC", "password": "1234", "PORT": 7000},
    {"name": "NodeD", "password": "1234", "PORT": 8000},
    {"name": "NodeE", "password": "1234", "PORT": 9000},
    {"name": "NodeF", "password": "1234", "PORT": 10000},
    {"name": "NodeG", "password": "1234", "PORT": 11000},
    {"name": "NodeH", "password": "1234", "PORT": 12000},
    {"name": "NodeI", "password": "1234", "PORT": 13000},
    {"name": "NodeJ", "password": "1234", "PORT": 14000},
]


def check_user(username, password):
    for user in users:
        if user["name"] == username and user["password"] == password:
            return user
    return False


def login():
    # Identify the sender
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if not check_user(username, password):
        print("Wrong username or password")
        return False
    return check_user(username, password)


def get_user(username):
    for user in users:
        if user["name"] == username:
            return user
    return None
