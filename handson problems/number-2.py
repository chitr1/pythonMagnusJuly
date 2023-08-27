N=["Ameya",23,40,"HEllo","Welcome",48,90,25]

print(N[1])

print(N[5:])

a=int(input("enter the list of values:"))
list=[]
for i in range(a):
    b=input("Enter the value into the list:")
    list.append(b)
    print(list [:3]+list [-3:])
