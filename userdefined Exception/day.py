class EligibleError(Exception):
    pass
class Sample:
    def Eligible(self,age,percentage):
        if age<18 and percentage<70:
            raise EligibleError("not eligible for registeration")
        else:
            print("Registeration is success")

obj1=Sample()
try:
    obj1.Eligible(17,70)
except EligibleError as e:
    print(e)
