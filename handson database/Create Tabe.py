from mysql import connector

class Table:
    global myDbConnection
    myDbconnection=connector.connect(host="localhost",user="root",password="root",database="pythonmagnus")
    global c1
    c1=myDbconnection.cursor()
    def create(self):
        c1.execute("create Table student1 (name varchar(20),class int,marks int)")
     def insert(self):
        c1.execute("insert into student1 values('wik',12,90)")
        c1.execute("insert into student1 values('Sam',13,92)")
        myDbconnection.commit()
        myDbconnection.close()


    def select(self):
        c1.excecute("select*from students")
        result=fetchall()
        print(result)


obj1 = Table()
obj1.create()
obj1.insert()



