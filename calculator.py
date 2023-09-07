from tkinter import*
root=Tk()
root.geometry("300x300")
root.resizable(0,0)
root.title("Calculator")
def button_click(value):
    global data
    data=data+str(value)
    itext.set(data)
data=""

def button_clear():
    global data
    data=""
    itext.set(data)

def button_equal():
    global data
    result=str(eval(data))
    itext.set(result)
data=""
itext=StringVar()
inputFrame=Frame(root,bg="red",width=300,height=50)
inputFrame.pack(side=TOP)

inputText=Entry(inputFrame, textvariable=itext, width=48, font=('Roman',20,'bold'),justify=RIGHT)
inputText.grid(row=0,column=0)
inputText.pack()

buttonFrame=Frame(root,bg="Blue",width=300,height=250)
buttonFrame.pack()

nine=Button(buttonFrame,text="7",width=9,height=3,command=lambda :button_click(7)).grid(row=1,column=0)
eight=Button(buttonFrame,text="8",width=9,height=3,command=lambda :button_click(8)).grid(row=1,column=1)
seven=Button(buttonFrame,text="9",width=9,height=3,command=lambda :button_click(9)).grid(row=1,column=2)
plus=Button(buttonFrame,text="+",width=9,height=3,command=lambda :button_click("+")).grid(row=1,column=3)

four=Button(buttonFrame,text="4",width=9,height=3,command=lambda :button_click(4)).grid(row=2,column=0)
five=Button(buttonFrame,text="5",width=9,height=3,command=lambda :button_click(5)).grid(row=2,column=1)
six=Button(buttonFrame,text="6",width=9,height=3,command=lambda :button_click(6)).grid(row=2,column=2)
sub=Button(buttonFrame,text="-",width=9,height=3,command=lambda :button_click("-")).grid(row=2,column=3)

one=Button(buttonFrame,text="1",width=9,height=3,command=lambda :button_click(1)).grid(row=3,column=0)
two=Button(buttonFrame,text="2",width=9,height=3,command=lambda :button_click(2)).grid(row=3,column=1)
three=Button(buttonFrame,text="3",width=9,height=3,command=lambda :button_click(3)).grid(row=3,column=2)
multi=Button(buttonFrame,text="*",width=9,height=3,command=lambda :button_click("*")).grid(row=3,column=3)

clear=Button(buttonFrame,text="C",width=9,height=3,command=lambda :button_clear()).grid(row=4,column=0)
zero=Button(buttonFrame,text="0",width=9,height=3,command=lambda :button_click(0)).grid(row=4,column=1)
equal=Button(buttonFrame,text="=",width=9,height=3,command=lambda :button_equal()).grid(row=4,column=2)
div=Button(buttonFrame,text="/",width=9,height=3,command=lambda :button_click("/")).grid(row=4,column=3)

root.mainloop()
