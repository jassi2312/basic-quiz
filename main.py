from tkinter import *
from tkinter import ttk

y=0
a=ttk.Notebook()
frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)
frame6=ttk.Frame(a)
frame7=ttk.Frame(a)

root = ttk.Frame(a)
def quiz(y, count=0, tot=0):
    a.add(frame1,text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")
    a.add(frame6, text="Q6")
    a.add(frame7, text="Total Marks")

    Label(frame1,text="which is a keyword?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame1, text="def",font=("Arial",20,"bold"),bg="light blue",command=a_right).grid(row=3,column=1)
    Button(frame1, text="temp", font=("Arial", 20, "bold"), bg="light blue",command=a_wrong).grid(row=4, column=1)
    Button(frame1, text="ttk", font=("Arial", 20, "bold"), bg="light blue",command=a_wrong).grid(row=5, column=1)


    Label(frame2,text="output of 2**3 is?",font=("Arial",30,"bold")).grid(row=2,column=2)
    Button(frame2, text="6", font=("Arial", 20, "bold"), bg="light blue",command=a2_wrong).grid(row=3, column=1)
    Button(frame2, text="8", font=("Arial", 20, "bold"), bg="light blue",command=a2_correct).grid(row=4, column=1)
    Button(frame2, text="9", font=("Arial", 20, "bold"), bg="light blue",command=a2_wrong).grid(row=5, column=1)

    Label(frame3, text="output of np.arrange(1,5) is?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame3, text="1,2,3,4", font=("Arial", 20, "bold"), bg="light blue",command=a3_wrong).grid(row=3, column=1)
    Button(frame3, text="0,1,2,3,4", font=("Arial", 20, "bold"), bg="light blue",command=a3_wrong).grid(row=4, column=1)
    Button(frame3, text="1,2,3,4,5", font=("Arial", 20, "bold"), bg="light blue",command=a3_correct).grid(row=5, column=1)

    Label(frame4, text="keyword used to declare a function?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame4, text="define", font=("Arial", 20, "bold"), bg="light blue",command=a4_wrong).grid(row=3, column=1)
    Button(frame4, text="def", font=("Arial", 20, "bold"), bg="light blue",command=a4_correct).grid(row=4, column=1)
    Button(frame4, text="none", font=("Arial", 20, "bold"), bg="light blue",command=a4_wrong).grid(row=5, column=1)

    Label(frame5, text="output of 2*12", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame5, text="24", font=("Arial", 20, "bold"), bg="light blue",command=a5_correct).grid(row=3, column=1)
    Button(frame5, text="28", font=("Arial", 20, "bold"), bg="light blue",command=a5_wrong).grid(row=4, column=1)
    Button(frame5, text="32", font=("Arial", 20, "bold"), bg="light blue", command=a5_wrong).grid(row=5,column=1)

    Label(frame6, text="what is my name", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(frame6, text="dan", font=("Arial", 20, "bold"), bg="light blue", command=a6_wrong).grid(row=3, column=1)
    Button(frame6, text="su", font=("Arial", 20, "bold"), bg="light blue",command=a6_wrong).grid(row=4, column=1)
    Button(frame6, text="jas", font=("Arial", 20, "bold"), bg="light blue", command=a6_correct, ).grid(row=5, column=1)



def a_right():
    Label(frame1,text="correct", font=("Arial",40,"bold"),background="green", fg="yellow").grid(row=5, column=2)
    Label(frame1,text="marks = 1",font=("Arial",40,"bold"),background="black", fg="white").grid(row=6, column=2)

def a_wrong():
    Label(frame1, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame1, text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)


def a2_correct():
    Label(frame2, text="correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(frame2, text="marks = 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)

def a2_wrong():
    Label(frame2, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame2, text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)
def a3_correct():
    Label(frame3, text="correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(frame3, text="marks = 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)

def a3_wrong():
    Label(frame3, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame3,text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)
def a4_correct():
    Label(frame4, text="correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(frame4, text="marks = 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)

def a4_wrong():
    Label(frame4, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame4,text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)
def a5_correct():
    Label(frame5, text="correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(frame5, text="marks = 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)

def a5_wrong():
    Label(frame5, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame5, text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)
def a6_correct():
    Label(frame6, text="correct", font=("Arial", 40, "bold"), background="green", fg="yellow").grid(row=5, column=2)
    Label(frame6, text="marks = 1", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)

def a6_wrong():
    Label(frame6, text="incorrect", font=("Arial", 40, "bold"), background="red", fg="yellow").grid(row=5, column=2)
    Label(frame6, text="marks = 0", font=("Arial", 40, "bold"), background="black", fg="white").grid(row=6, column=2)




quiz(y)
a.pack()
a.mainloop()
