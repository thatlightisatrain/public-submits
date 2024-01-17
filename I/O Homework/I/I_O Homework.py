class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class Bootcamp:
    def __init__(self):
        self.students =[]
    
    def add_student(self, name, age, email):
        student = Student(name, age, email)
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            self.students.remove(student)

    def search_student(self, name):
        for student in self.students:
            if student.name == name:
                print(f"student found in database: Name: {student.name}, Age: {student.age}, Email: {student.email}")
                return
        print(f"no student like that.")

    def display_students(self):
        for student in self.students:
            print(f"name: {student.name},Age: {student.age}, Email: {student.email}")

    def readfile(self):
        with open('students.txt', 'r') as f:
            data = f.read()
            print(data)

    def writefile(self):
        with open('students.txt', 'w') as f:
            for student in self.students:
                f.write(f'{student.name} {student.age} {student.email}\n')

def interface():
    bootcamp = Bootcamp()
    while True:
        print("1. Add Student")
        print("2 remove a student")
        print("3 search by name")
        print("4. Show all Students")
        print("5. Quit")

        prompt = input("What would you like to do? (1/2/4/5): ")
        if prompt == '1':
            name = input("what is the name of the Sudent?: ")
            age = input("how old is the student?: ")
            email = input("what is the students Email?: ")
            bootcamp.add_student(name, age, email)
        elif prompt == '2':
            name = input("who do you wanna remove?: ")
            bootcamp.remove_student(name)
        elif prompt == '3':
            name = input("what is the name of the student your looking for?: ")
            bootcamp.search_student(name)
        elif prompt == '4':
            bootcamp.display_students()
        elif prompt == '5':
            print("Shutting down!")
            break
        else: print ("wrong Input!")

if __name__ == "__main__":
    interface()