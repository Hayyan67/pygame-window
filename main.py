from tkinter import *

root = Tk()
root.title('My window')
root.geometry('300x300')
root.config(background="yellow")

L1 = Label(root,text="Registration Form", bg="light blue", fg="red", font=('Arial', 30), padx=10, pady=10)
L1.pack()
L2 = L1 = Label(root,text="Enter your name", bg="light green", fg="blue", font=('Arial', 12), padx=10, pady=10)
L2.pack()
e1=Entry(root)
e1.pack()
def msg():
    a1=e1.get()
    m1="Hey "+ a1+ "\n Welcome to my window"
    L3 = Label(root, text=m1)
    L3.pack()
radio=IntVar()
L4 = Label(root,text="Select your gender: ")
r1 = RADIOBUTTON(root, text="Male",Variable=radio, value=1)
r1.pack()
r2 = RADIOBUTTON(root, text="Female",Variable=radio, value=2)
r2.pack()
b1 =Button(root, text='Submit', bg='red', fg='white')
b1.pack()
root.mainloop()
