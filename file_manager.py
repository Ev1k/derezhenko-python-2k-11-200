import os

def pwd():
    print(os.getcwd())


def cd(dirname):
    try:
        os.chdir(dirname)
    except:
        print("Directory not found")


def touch(filename):
    try:
        open(filename, 'a').close()
    except:
        print("Error creating file")


def cat(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except:
        print("Error reading file")


def ls():
    for file in os.listdir():
        print(file)


def rm(filename):
    try:
        os.remove(filename)
    except:
        print("Error removinf file")


while True:
    command = input().split()

    if command[0] == "pwd":
        pwd()
    elif command[0] == "cd":
        cd(command[1])
    elif command[0] == "touch":
        touch(command[1])
    elif command[0] == "cat":
        cat(command[1])
    elif command[0] == "ls":
        ls()
    elif command[0] == "rm":
        rm(command[1])
    elif command[0] == "exit":
        break
    else:
        print("Command not found")