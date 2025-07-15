from src.auth import login_user


# run this as enrty point
if __name__ == "__main__":
    email = "andrus@gmail.com"
    password = '123'

    login_user(email, password)
