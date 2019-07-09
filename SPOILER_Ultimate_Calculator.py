from tkinter.ttk import *
from tkinter import *


def open_length_page():

    def submit():
        unit1 = ' '
        unit2 = ' '
        var1 = int(entryOne.get())
        
        calcDict = {
            #Nautical Mile Conversion
            'nminmi': var1*1,
            'nmimi': 1,
            'nmikm': 1,
            'nmim': 1,
            'nmiyd': 1,
            'nmift': 1,
            'nmiin': 1,
            'nmicm': 1,
            'nmimm': 1,
            'nmium': 1,
            'nminm': 1,

            #Mile Conversion
            'minmi': 1,
            'mimi': var1*1,
            'mikm': 1,
            'mim': 1,
            'miyd': 1,
            'mift': 1,
            'mift': 1,
            'miin': 1,
            'micm': 1,
            'mimm' : 1,
            'mium': 1,
            'minm': 1
        }
        
        #topResult = topCombo.get()
        #topLabel.configure(text=topResult)

        #bottomResult = bottomCombo.get()
        #bottomLabel.configure(text=bottomResult)

        unit1 = topCombo.get()
        unit2 = bottomCombo.get()

        #var1 = entryOne.get()
        calc = unit1 + unit2
        answer = calcDict.get(calc)
        
        print('Unit1 =', unit1)
        print('Unit2 =', unit2)
        print('Calc = ', calc)
        print('Var1 =', var1)
        print(answer)
        
    
    lengthPage = Toplevel(window)
    lengthPage.title("Length Calculator")
    lengthPage.geometry('300x200')
    lengthPage.resizable(False, False)

    topCombo = ttk.Combobox(lengthPage)
    topCombo['values']= ('nmi', 'mi', 'km', 'm', 'yd', 'ft', 'in', 'cm', 'mm', 'un', 'nm')
    topCombo.current(1)
    topCombo.grid(column=0, row=0)
    
    entryOne = Entry(lengthPage, width=20)
    entryOne.grid(column=0, row=1, padx=5, pady=5)

    bottomCombo = ttk.Combobox(lengthPage)
    bottomCombo['values']= ('nmi', 'mi', 'km', 'm', 'yd', 'ft', 'in', 'cm', 'mm', 'un', 'nm')
    bottomCombo.current(1)
    bottomCombo.grid(column=0, row=2)

    submitButton = Button(lengthPage, text="Submit", width=10, height=1, command=submit)
    submitButton.grid(column=0, row=4)

    topLabel= Label(lengthPage, text=" ", )
    topLabel.grid(column=1, row=0)

    bottomLabel = Label(lengthPage, text=" ", )
    bottomLabel.grid(column=1, row=2)

    lengthPage.mainloop()













window = Tk()
 
window.title("The Ultimate Calculator: Control Panel")
window.geometry('500x200')
window.resizable(False, False)

titleLabel = Label(window, text="Select your calculation!", )
titleLabel.grid(column=0, row=0)

lengthButton = Button(window, text="Length", width=10, height=1, command=open_length_page)
lengthButton.grid(column=0, row=1)

weightButton = Button(window, text="Weight", width=10, height=1)
weightButton.grid(column=1, row=1)

window.mainloop()
