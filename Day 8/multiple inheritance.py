class Father:
    def Home(self):
        print("2 apartments")
class Mother:
    def Car(self):
        print("2cars")

    def Cash(self):
        print("$100000" )

class Son(Father,Mother):
    pass

obj1=Son()
obj1.Home()
obj1.Car()
obj1.Cash()


