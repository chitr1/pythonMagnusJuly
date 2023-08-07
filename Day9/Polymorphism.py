class Car_2022:
    def Roof(self):
        print("Sunroof")
    def Wheels(self):
        print("Normal alloy wheels")
    def Music(self):
        print("7 music touch player")
class car_2023(Car_2022):
    def Roof(self):
        #print("Panaromic sunroof")
        super().Roof()
    def Wheels(self):
        print("Normal alloy wheels")
    def Music(self):
        print("7 music touch player")

obj1 = car_2023()
obj1.Roof()
obj1.Wheels()
obj1.Music()












