from tkinter import*
root = Tk()
root.geometry('300x300')
username=Label(root,text="USERNAME").place(x=30,y=50)
t1= Entry(root).place(x=100,y=50)
password=Label(root,text="PASSWORD").place(x=30,y=100)
t2=Entry(root).place(x=100,y=100)
b1=Button(root,text="LOGIN").place(x=30,y=150)

root.mainloop()
