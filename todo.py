import sys

def list_tasks():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
        index = 1
        for todo in todos:
            print(f"{index} - {todo.split(",")[0]}")
            index += 1
        if len(todos) == 0:
            print("No todos for today :)")
            
def add_task(task):
    with open("todos.txt", "a") as file:
        file.write(f"{task},0\n")

def decide_action(args):
    print(args)
    help = """Command Line To Do Application

==============================


Command-line arguments:

-l Lists all the tasks

-a Adds a new task

-r Removes a task

-c Completes a task

    """
    if len(args) == 1:
        print(help)
    elif args[1] == "-a":
        if len(args) != 3:
            print("Unable to add: no task provided")
        else: 
            add_task(args[2])
    elif args[1] == "-l":
        list_tasks()


decide_action(sys.argv)


    