from mysql import connector
myDbconnection=connector.connect(host="localhost",user="root",password="root",database="pythonmagnus")
c1=myDbconnection.cursor()

class Table:
    def create(self):
        c1.execute("create Table students (name varchar(20),class int,marks int)")
        myDbconnection.commit()
        myDbconnection.close()
        print(myDbconnection)


