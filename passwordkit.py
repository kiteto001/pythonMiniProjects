password = ""

while password != "1234":
    password = input("Enter the password: ")
    if password == "1234":
        print("correct password. Access granted.")
    else:
        print("Incorrect password. Try again.")