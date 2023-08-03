class Grandparent:
    def a1(self):
        print("2 assets")

class Parents(Grandparent):
    def a2(self):
        print("3assets")

class Son(Parents,Grandparent):
    def a3(self):
        print("1 asset")

obj1=Son()
obj1.a1()
obj1.a2()
obj1.a3()
