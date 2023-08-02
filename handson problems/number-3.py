class Sample():
    a=10
    b=30

    def m1(self):
        print("M1 Function")


def m1(self):
    print('m1function')

obj=Sample()
print(obj.a)
obj.m1()

