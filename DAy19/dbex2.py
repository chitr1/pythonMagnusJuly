from mysql import connector
myDbconnection= connector.connect(host='localhost',user='root',password='root',database='pythonmagnus')
c1=myDbconnection.cursor()
vempno=int(input("enter the value of empno :"))
vename=input("enter the ename")
vdeptno=int(input("enter the deptno :"))
c1.execute("insert into emp(empno,ename,deptno) values (%s,%s,%s)"),(vempno,vename,vdeptno)
myDbconnection.commit()
myDbconnection.close()


