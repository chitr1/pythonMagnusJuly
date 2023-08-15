a=[10,11,121,13,15,18,19]
index=0
a[index],a[-index-1]=a[-index-1],a[index]
print(a[index],a[-index-1])

A=["Data","Hero","Hello","Welcome","Where"]
index=0
A[index],A[index-1]=A[index-1],A[index]
print(A[index],A[-index-1])

A=["Data","Hero","Hello","Welcome","Where","When"]
for index in range (len(A)//2):
    A[index],A[-index-1]=A[-index-1],A[index]
    print(A)

a=[10,11,121,13,15,18,19,38]
for index in range(len(a)//2):
    a[index],a[-index-1]=a[-index-1],a[index]
    print(a)

a=[10,20,50,40,60,79]
a.append(80)
print(a)

A=["Data","Hero","Hello","Welcome","Where","When"]
A.insert(4,"Rithwik")
print(A)

a=[10,20,50,40,60,79]
a.pop(2)
print(a)





