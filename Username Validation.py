username = input("Enter username: ")

if len(username) < 5:
    print("Invalid username: Username must contain at least 5 characters.")

elif username.isspace():
    print("Invalid username: Username must not contain only spaces.")

elif username.lower() == "admin":
    print("Invalid username: Username cannot be 'admin'.")

else:
    print("Valid username.")