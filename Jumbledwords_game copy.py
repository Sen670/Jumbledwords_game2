from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.geometry("500x500")

answers = ["tractor","donkey","hamburger","school","kitten","water","nocturnal","magatsuhi","snowglobe","card","cap","house"]
words = ["rtotarc","nkdoey","mabhrgure","hosolc","tentki","twrae","nctortunla","gmatausih","goswonble","radc","cpa","oshue"]

answer = StringVar()
number = random.randrange(0,len(words),1)
c = 0
d = 0
s = 0
L = Label(root)

def default():
    global words,answers,number
    label2.config(text=words[number])

def reset():
    global words,answers,number
    number = random.randrange(0,len(words),1)
    label2.config(text=words[number])
    entry1.delete(0,END)

def check_answer():
    global words,answers,number,c,d,s,L
    d = int(d) + 1
    var = entry1.get()
    if var == answers[number]:
        messagebox.showinfo("Congratulations!","Correct answer!")
        c = int(c) + 1 

    else:
        messagebox.showerror("Sorry","Incorrect answer...")

    s = "score" + str(c) + "/" + str(d)
    L.forget()
    L = Label(root,font=("Ariel",20),text=s)
    L.place(x=175,y=400)
    reset()

heading = Label(root,text="Jumbled word game",font=("Ariel",25))
heading.place(x=100,y=50)
label1 = Label(root,text="What is the word?",font=("Ariel",20))
label1.place(x=130,y=200)
label2 = Label(root)
label2.place(x=200,y=125)



entry1 = Entry(root,width=10)
entry1.place(x=210,y=275)

button1 = Button(root,text="Check",width=20,height=2,command=check_answer)
button1.place(x=50,y=350)
button2 = Button(root,text="Reset",width=20,height=2,command=reset)
button2.place(x=275,y=350)
    
default()
































root.mainloop()