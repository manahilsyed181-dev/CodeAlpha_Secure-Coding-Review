import hashlib

stored_username = "admin"
stored_password = hashlib.sha256("12345".encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and hashlib.sha256(password.encode()).hexdigest() == stored_password:
    print("Login successful")
else:
    print("Login failed")