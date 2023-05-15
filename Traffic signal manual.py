from tkinter import *

def red():
    canvas1.create_oval(120,120,50,50, fill='red', outline='white',width=3)
    canvas2.create_oval(120,120,50,50, fill='white', outline='white',width=3)
    canvas3.create_oval(120,120,50,50, fill='white', outline='white',width=3)

def orange():
    canvas1.create_oval(120,120,50,50, fill='white', outline='white',width=3)
    canvas2.create_oval(120,120,50,50, fill='orange', outline='white',width=3)
    canvas3.create_oval(120,120,50,50, fill='white', outline='white',width=3)
    
def green():
    canvas1.create_oval(120,120,50,50, fill='white', outline='white', width=3)
    canvas2.create_oval(120,120,50,50, fill='white', outline='white', width=3)
    canvas3.create_oval(120,120,50,50, fill='green', outline='white', width=3)
    



play = Tk()
play.geometry('500x500')
play.title("Traffic signal-manual")
play.configure(bg = 'lightgray')

Button(play, font=('calibri',15),command=red, bg='red', fg='white', width='10', height='2').grid(row=1,column=1) 
Button(play, font=('calibri',15), command=orange, bg='orange', fg='white', width='10', height='2').grid(row=2,column=1) 
Button(play, font=('calibri',15), command=green, bg='green', fg='white', width='10', height='2').grid(row=3,column=1)


canvas1 = Canvas(play, height=130, bg= 'black')
canvas1.grid(row=1, column=2)
canvas2 = Canvas(play, height=130, bg= 'black')
canvas2.grid(row=2, column=2)
canvas3 = Canvas(play, height=130, bg= 'black')
canvas3.grid(row=3, column=2)

play.mainloop()
