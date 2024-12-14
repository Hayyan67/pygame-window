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
b1 =Button(root, text='Submit', bg='red', fg='white')
b1.pack()
root.mainloop()
