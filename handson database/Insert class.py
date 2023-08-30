from mysql import connector
myDbconnection=connector.connect(host="localhost",user="root",password="root",database="pythonmagnus")
c1=myDbconnection.cursor()
     def insert(self):
        c1.execute("insert into student1 values('wik',12,90)")
        c1.execute("insert into student1 values('Sam',13,92)")
        myDbconnection.commit()
        myDbconnection.close()
obj1=Table()
obj1.insert()


