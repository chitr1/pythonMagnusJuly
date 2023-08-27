from mysql import connector
myDbconnection=connector.connect(host="localhost",user="root",password="root",database="pythonmagnus")
c1=myDbconnection.cursor()
c1.execute("select*from emp")
result=c1.fetchmany(size=2)
print(result)
myDbconnection.close()
