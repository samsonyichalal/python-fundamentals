# practice file handling with try/except 
"""
we will try to access a file and if doesn't exist 
that file the program will creat it automatically

"""
try:
    with open("users.txt", "r") as file:
        content = file.read()
        print("User database found:")
        print(content)

except FileNotFoundError:
    print("No users found. Creating new database...")

    with open("users.txt", "w") as file:
        file.write("User database initialized\n")
