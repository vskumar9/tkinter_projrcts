from tkinter import * #This is importing all in tkinter

def getvalues(selected):
    dropdownmenu2['menu'].delete(0, 'end')  # clear existing options
    if selected != '-----Select-----':  # if a state is selected
        for district in option2[selected]:  # add district options
            dropdownmenu2['menu'].add_command(label=district, command=lambda district=district: dropvar2.set(district))
        dropvar2.set(option2[selected][0])  # set the default district
    else:
        dropvar2.set('------select------')  # set default message if no state is selected


obj = Tk() #this is built-in class in a tkinter
obj.geometry('1000x800') #this is a application dimension
obj.title('DropDownList') # this is a title of the our application
obj.configure(bg = 'aqua') #this is a background color our application


Label(obj, text = 'Select State: ', font = ('calibri', 15), bg = 'aqua').grid(row=1, column=1) #this is a add label my application

option1 = ['Andhra pradesh', 'Goa', 'Karnataka', 'Kerala', 'Tamilnadu'] #This is my option 
dropvar1 = StringVar() # this is my option datatype

dropdownmenu1 = OptionMenu(obj, dropvar1, '-----Select-----', *option1, command = getvalues)#this is add option in my application
dropdownmenu1.grid(row = 1, column = 2) #this is optio of the selection list option


Label(obj, text = 'Select District: ', font = ('calibri', 15), bg = 'aqua').grid(row=2, column=1) #this is a another option menu label

option2 = { 'Andhra pradesh' : ['Kadapa', 'Chittor', 'Nellore', 'Guntur', 'Ananthapur'],
            'Goa' : ['North Goa', 'South Goa'],
            'Karnataka' : ['Kolar', 'Mysore'],
            'Kerala' : ['Kolam'],
            'Tamilnadu' : ['Chennai', 'Salem']} #this is we have first option select to second option menu open this is a downdownList menu

dropvar2 = StringVar()

dropdownmenu2 = OptionMenu(obj, dropvar2, '------select------')
dropdownmenu2.grid(row = 2, column = 2)
            


obj.mainloop() #this is main function in a tkinter

