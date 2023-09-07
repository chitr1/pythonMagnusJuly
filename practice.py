from mysql import connector
myDbconnection = connector.connect(host='localhost',user='root',password='root',database='family')
c1=myDbconnection.cursor()
c1.execute("insert into emp values(101,'Chad',12000")
c1.execute("insert into emp values(201,'Mark',20000")
c1.execute("inset into emp values(150,'Ben',17000")
myDbconnection.commit()
myDbconnection.close()
