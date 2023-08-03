class Teacher:
    def English(self):
        print("English subject")

class Student1(Teacher):
    pass

class Student2(Teacher):
    pass

obj1=Student1()
obj2=Student2()
obj1.English()
obj2.English()
