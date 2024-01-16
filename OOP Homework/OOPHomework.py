class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print(f"The person's name is {self.name} and is {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id, gender):
        super().__init__(name, age)
        self.student_id = student_id
        self.gender = gender

    def describe(self):
        super().describe()
        print(f"The person's name is {self.name}, is {self.age} years old, {self.gender}, student id: {self.student_id}.")

class Course:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        for student in self.students:
            print(student.name)

student1 = Student("Harry", 10, 101, "male")
student2 = Student("Anai", 12, 102, "nonbinary")

course = Course("Bootcamp Data Science", "Alejandro Valejo", [])
course.add_student(student1)
course.add_student(student2)

course.list_students()