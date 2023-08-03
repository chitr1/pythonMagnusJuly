class English :
    def E1(self):
        print("Alphabets as E1")

class Students(English):
    def E2(self):
        print("Chapter as E2")

Grade1= Students()
Grade1.E1()
Grade1.E2()
