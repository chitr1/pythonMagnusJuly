from mysql import connector
myDbconnection=connector.connect(host="localhost",user="root",password="root",database="pythonmagnus")
c1=myDbconnection.cursor()
#c1.execute('create table emp(empno int,ename varchar(20),deptno int)')
#c1.execute("insert into emp values (10,'Wik',100)")
#c1.execute("insert into emp values(20,'Sam',120)")
#c1.execute("insert into emp values(30,'Rik',140)")
sql="insert into emp values(%s,%s,%s)"
data=(40,'Dan',125)
c1.execute(sql,data)
myDbconnection.commit()
myDbconnection.close()






