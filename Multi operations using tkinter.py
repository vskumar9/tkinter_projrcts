from tkinter import * #import all

#now i'm write a function addition
def oper():
    num1=number1.get()
    num2=number2.get()
    num3=number3.get()
    operator = dropvar1.get() # get the selected operator
    if operator == '+':
        data = num1 + num2 + num3
    elif operator == '-':
        data = num1 - num2 - num3
    elif operator == '*':
        data = num1 * num2 * num3
    elif operator == '/':
        data = num1 / num2 / num3
    elif operator == '%':
        data = num1 % num2 % num3
    result.configure(text='Result: %d' %data) # configure the result label






obj = Tk() #this is a tkinter
obj.geometry('800x800') #dimensions of the window application
obj.title('OPERATIONS') #This is a title of the application
obj.configure(bg = 'aqua') #application background color

Label(obj, text='Enter value A:', font=('calibri',15), bg='aqua').grid(row=1, column=1) #this is a label insert my application this font style calibri and size is 15,
#background color aqua, grid this to arrange the position of the label
Label(obj, text='Enter value B:', font=('calibri',15), bg='aqua').grid(row=2, column=1)
Label(obj, text='Enter value C:', font=('calibri',15), bg='aqua').grid(row=3, column=1)

number1 = IntVar() #this is a value type assign a variable
number2 = IntVar()
number3 = IntVar()


option1 = ['+', '-', '*', '/', '%'] #This is my option 
dropvar1 = StringVar() # this is my option datatype

dropdownmenu1 = OptionMenu(obj, dropvar1, '-----Select-----', *option1,)#this is add option in my application
dropdownmenu1.grid(row = 4, column = 2) #this is optio of the selection list option




Entry(obj, textvariable=number1, font=('calibri',13)).grid(row=1, column=2)# This is a enter option insert or adding my application
Entry(obj, textvariable=number2, font=('calibri',13)).grid(row=2, column=2)
Entry(obj, textvariable=number3, font=('calibri',13)).grid(row=3, column=2)

Button(obj, text='ADD', command=oper, font=('calibri',13), bg='gray', fg='white', width='10', height='1').grid(row=5, column=2)#This is button add my application

result=Label(obj, font=('calibri',15), bg='aqua', fg='red')
result.grid(row=6, column=2)


obj.mainloop() #This is a main fuction 

