# a small a program that reads a list of usernames and prints them

# Read usernames from the file
users_file = open("user_log.txt", "r")
content = users_file.readlines()

print("Registered users:")
for line in content:
    print(line.strip())

users_file.close()