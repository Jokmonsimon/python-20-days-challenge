import getpass

database = {"afandeojok": "pass123456", "jokmon": "password123"}
username = input("Enter Your Username: ")
password = getpass.getpass("Enter Your Password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again: ")
        break
print("Congratulations! Username and Password Verified Successfully!")
