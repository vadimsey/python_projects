import json

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def create_student():
    print('===ADD STUDENT===')
    while True:
        name = input('Enter student name: ').strip()
        try:
            age = int(input('Enter student age: '))
        except:
            print('Enter valid age')
        else:
            break

    students = {}

    try:
        with open('students.json','r') as f:
            students = json.load(f)
    except:
        students = {}

    students[name] = age

    with open("students.json","w") as file:
        json.dump(students,file)



def view_students():
    try:
        with open("students.json","r") as file:
            students = json.load(file)
    except:
        students = {}

    for i, n in enumerate(students.items()):
        print(f"{i + 1}. {n[0]} - {n[1]}")



def choiced():
    print('=====MENU=====')
    while True:
        print("1. Add a new student")
        print("2. View students")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("===Enter a number===")
        else:
            break


    if choice == 1:
        create_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        exit()

    else:
        print("===Enter a valid choice===")

def main():
    while True:
        choiced()


if __name__ == '__main__':
    main()