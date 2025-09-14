import random

class Task():
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

t1 = Task(name="Do physics assignment",deadline=6)
# print(f"Task: {t1.name}\tDeadline: {t1.deadline}")
tasks = []

def SORT (taskList: list):
    # for(i=0; i<len(taskList)-1; i++):
    for i in range(len(taskList)-1):
        for j in range(len(taskList)-i-1):
            if(taskList[j].deadline > taskList[j+1].deadline):
                taskList[j], taskList[j+1] = taskList[j+1], taskList[j]
    return taskList

def MPT(tasks: list):
    result = SORT(tasks)
    print("Most prior task: ")
    print(f"Task: {result[0].name}  |   Deadline: {result[0].deadline}")

def LPT(tasks: list):
    result = SORT(tasks)
    print("Least prior task: ")
    print(f"Task: {result[len(tasks)-1].name}  |   Deadline: {result[len(tasks)-1].deadline}")

def ART(tasks: list):
    result = random.choice(tasks)
    print("Randomly Assigned task: ")
    print(f"Task: {result.name}  |   Deadline: {result.deadline}")
        

while True:
    
    while True:
        ch = input("Do you want to enter task (y/n): ")
        if ch.lower() == 'n':
            break
        t = Task(input("Enter task: "),int(input("Enter deadline: ")))
        tasks.append(t)
    
    print("""Enter following number to perform operation:
          1: Most prior task
          2: Least prior task
          3: Assign random task
          0: Exit !""")
    num = int(input("Enter your choice: "))

    match num:
        case 1:
            MPT(tasks)
        case 2:
            LPT(tasks)
        case 3:
            ART(tasks)
        case 0:
            break
        case _:
            print("Invalid number entered !\nTry again !!")

"""
concept:
I made user-defined functions like MPT, LPT, ART, SORT, but these could be done in few line of codes and do the work.

most_prior = min(tasks, key=lambda t: t.deadline)   # smallest deadline | MPT
least_prior = max(tasks, key=lambda t: t.deadline)  # largest deadline | LPT
and no need to sort.
and if i had to sort, it could have been done by

sorted(taskList, key=lambda t: t.deadline)

I did it the long way because, i didn't know inbuild functions like these exist in python.

"""