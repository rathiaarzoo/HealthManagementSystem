# Health Management System
# 3 clients- A,B,C
# 3 files to log their food
# 3 files to log their excercise
# Write a function that when executed takes as input client name
# one more fn to retrieve exercise or food for any client
# Make a Health Management System

def getdate():
    import datetime
    return datetime.datetime.now()


def food():
    client_food = input("Which food do you want to add to the list")
    return client_food


def exercise():
    client_exercise = input("Which exercise do you want to add to the list")
    return client_exercise


print("For whom do you want to make changes in the file?")
client_name = int(input("Enter '1' for Aarzoo / '2' for Naina / '3' for Nikita: \n"))

print("What do you want to record?")
client_record = int(input("Enter '1' for food / '2' for Exercise:\n"))

if client_name == 1:
    if client_record == 1:
        f = open('Aarzoo-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food)
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('Aarzoo-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

if client_name == 2:
    if client_record == 1:
        f = open('Naina-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food)
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('Naina-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

if client_name == 3:
    if client_record == 1:
        f = open('Nikita-food.txt', "a")
        f_food = food()
        f_date = str(getdate())
        f.write("[" + f_date + "]   " + f_food)
        print('Thank-You for adding', f_food, "to the list\n")
        f.close()
    elif client_record == 2:
        f = open('Nikita-exercise.txt', "a")
        f_date = str(getdate())
        f_exercise = exercise()
        f.write("[" + f_date + "]   " + f_exercise)
        print('Thank-You for adding', f_exercise, "to the list\n")
        f.close()
    else:
        print("please enter a valid record")

