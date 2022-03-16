class Student(object):

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # function to print name and roll number
    def display(self):
        print('Name: ', self.name)
        print('Roll No: ', self.roll_no)
    # #To get name
    # def getName(self):
    #     return self.name
    #
    # #TO get rolllNo
    # def getRollNo(self):
    #     return self.roll_no


# Inherited or subclass of Student
class Exam(Student):

    # Constructor
    def __init__(self, m1, m2, m3, m4, m5, m6):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.m6 = m6

    # function to print marks scored in six subject
    def displayMarks(self):
        print('--Marks scored in six subject--')
        print('Subject-1: ', self.m1)
        print('Subject-2: ', self.m2)
        print('Subject-3: ', self.m3)
        print('Subject-4: ', self.m4)
        print('Subject-5: ', self.m5)
        print('Subject-6: ', self.m6)


# subclass of Exam class
class Result(Exam):

    def result(self):
        total_marks = self.m1 + self.m2 + self.m3 + self.m4 + self.m5 + self.m6
        print('Total marks: ', total_marks)


obj1 = Student("Yashvi", 45)  # An object of Student
print(obj1.display())

obj2 = Exam(80, 85, 90, 92, 95, 75)
print(obj2.displayMarks())

obj3 = Result()
print(obj3.result)
