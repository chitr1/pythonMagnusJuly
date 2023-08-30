from tkinter import*
root = Tk()
root.geometry('300x300')
username=Label(root,text="USERNAME").grid(row=0,column=0)
t1= Entry(root).grid(row=0,column=1)
password=Label(root,text="PASSWORD").grid(row=2,column=0)
t2=Entry(root).grid(row=2,column=1)
b1=Button(root,text="LOGIN").grid(row=4,column=0)

root.mainloop()
