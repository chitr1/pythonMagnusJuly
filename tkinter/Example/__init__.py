from tkinter import *
root=Tk()
root.geometry('300x300')
lb=Button(root,text="LEFT",fg="red")
lb.pack(side=LEFT)
rb=Button(root,text="RIGHT",fg="green")
rb.pack(side=RIGHT)
tb=Button(root,text="TOP",fg="blue")
tb.pack(side=TOP)
bb=Button(root,text="BOTTOM",fg="yellow")
bb.pack(side=BOTTOM)


root.mainloop()

