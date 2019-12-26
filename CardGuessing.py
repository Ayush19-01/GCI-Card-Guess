from tkinter import *
from tkinter import messagebox
a=0
time=15
l=[["cat.png","A pet and animal","cat","Card 1"],
       ["die.png","Used to make moves in board games","dice","Card 2"],
       ["buck.png","Water storage","bucket","Card 3"],
       ["bell.png","Used as a physical notification\Catches attention when ringed","bell","Card 4"],
       ["ball.png","Used to play games with","ball","Card 5"],
       ["hglass.png","Used as a timer in old times","hourglass","Card 6"],
       ["bulb.png","Used as a source of light","bulb","card 7"],
       ["gavel.png", "Used by judges in the court", "gavel", "Card 8"],
       ["saw.png","Used in cutting things","saw","Card 9"],
       ["cross.png","Definately not a single letter","cross","card 10"]]
def main1():
    global root1
    global Username
    root1=Tk()
    root1.resizable(0,0)
    Username = StringVar()
    root1.geometry("500x220")
    root1.config(bg="#220047")
    root1.title("Welcome")
    label_1 = Label(root1,text="Card Guessing Game",font=("roboto",30),bg="#220047",fg="#CE9141")
    label_1.place(x=70,y=10)
    label_2 = Label(root1,text="Enter the your name:",font=("roboto",19),bg="#220047",fg="#CE9141")
    label_2.place(x=30,y=90)
    entry1= Entry(root1,textvar=Username,width=30)
    entry1.place(x=270,y=100)
    button1 = Button(root1,text="Play",font=("roboto",20),bg="#CE9141",fg="#220047",activeforeground="#CE9141",activebackground="#220047")
    button1.bind("<Button-1>",startgame)
    button1.place(x=215,y=150)
    root1.mainloop()
def startgame(event):
    global root2
    global AT
    root1.destroy()
    root2 = Tk()
    root2.resizable(0, 0)
    root2.geometry("600x400")
    gamegui()

def gamegui():
    global a
    if a>9:
        AT = Username.get()
        label4= Label(root2, text="Game Over!", font=("roboto", 30), bg="#220047",
                       fg="#CE9141")
        label4.place(x=200, y=100)
        label5= Label(root2, text=AT+" Wins!", font=("roboto", 30), bg="#220047",
                       fg="#CE9141")
        label5.place(x=200, y=200)
        return None


    global tmpl
    global answer
    global label1
    global label2
    global label3
    global button2
    global button3
    global entry2
    global image1
    answer=StringVar()
    root2.config(bg="#220047")
    tmpl=l[a]
    tmpd=tmpl[0]
    tmpc=tmpl[3]
    label1 = Label(root2, text="Guess the card given below:", font=("roboto", 20), bg="#220047", fg="#CE9141")
    label1.place(x=120, y=10)
    button2 = Button(root2, text="Hint", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button2.bind("<Button-1>", hint)
    button2.place(x=20, y=20)
    label2 = Label(root2, text=tmpc, font=("roboto", 15), bg="#220047",
                   fg="#CE9141")
    label2.place(x=260, y=60)
    label3= Label(root2, text="Enter your answer here:", font=("roboto", 15), bg="#220047",
                   fg="#CE9141")
    label3.place(x=120, y=312)
    entry2 = Entry(root2, textvar=answer, width=20)
    entry2.place(x=360, y=320)
    button3 = Button(root2, text="Submit", font=("roboto", 15), bg="#CE9141", fg="#220047", activeforeground="#CE9141",
                     activebackground="#220047")
    button3.bind("<Button-1>", check)
    button3.place(x=270, y=350)
    filename = PhotoImage(file=tmpd)
    image1= Label(image=filename)
    image1.place(x=150, y=90, relwidth=.5, relheight=.5)
    timer()
    root2.mainloop()
def timer():
    global time
    global labeltmp
    if len(str(time))==1:
        x="0"+str(time)
    else:
        x=str(time)
    if time!=0:
        labeltmp=Label(root2, text="Time left: "+x, font=("roboto", 15), bg="#220047",fg="#CE9141")
        labeltmp.place(x=10, y=70)
        time-=1
        root2.after(1000,timer)
    if time==0:
        messagebox.showinfo("Lost","Time ran out,you lose!")
        root2.destroy()
        return None
def hint(event):
    tmpstr=tmpl[1]
    messagebox.showinfo("Hint",tmpstr)
def check(event):
    global a
    global time
    tmpstr=answer.get()
    if tmpstr==tmpl[2]:
        if a==9:
            messagebox.showinfo("Correct","That is the correct answer!")
            a+=1
        else:
            messagebox.showinfo("Correct", "That is the correct answer, you have advanced to the next level!")
            a+= 1
    elif tmpstr!=tmpl[2]:
        messagebox.showinfo("Wrong", "That is the incorrect answer, answer correctly to advance to the next level!")
    label1.place_forget()
    label2.place_forget()
    label3.place_forget()
    button2.place_forget()
    button3.place_forget()
    entry2.place_forget()
    image1.place_forget()
    labeltmp.place_forget()
    time=15
    gamegui()

main1()
