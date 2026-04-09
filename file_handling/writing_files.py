# a small program that stores daily tasks and prints them.

# Write tasks to the file
with open("tasks.txt", "w") as task_file:
    task_file.write("Study Python\n")
    task_file.write("Build backend project\n")
    task_file.write("Apply for jobs\n")


# Read tasks from the file
with open("tasks.txt", "r") as file:
    tasks = file.readlines()

print("Today's tasks:")

for task in tasks:
    print(task.strip())