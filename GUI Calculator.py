from tkinter.ttk import *
from tkinter import *


def open_length_page():

    def submit():
        unit1 = ' '
        unit2 = ' '
        var1 = int(entryOne.get())
        
        calcDict = {
            # Nautical Mile Conversion
            'nminmi': var1*1,
            'nmimi': ans = float(num1) * 1.151,
            'nmikm': ans = float(num1) * 1.852,
            'nmim': ans = float(num1) * 1852,
            'nmiyd': ans = float(num1) * 2025.372,
            'nmift': ans = float(num1) * 6076.115,
            'nmiin': ans = float(num1) * 72913.386,
            'nmicm': ans = float(num1) * 185200,
            'nmimm': ans = float(num1) * (1.852*(10**6)),
            'nmium': ans = float(num1) * (1.852*(10**9)),
            'nminm': ans = float(num1) * (1.852*(10**12)),

            # Mile Conversion
            'minmi': ans = float(num1) / 1.151,
            'mimi': var1*1,
            'mikm': ans = float(num1) * 1.609,
            'mim': ans = float(num1) * 1609.344,
            'miyd': ans = float(num1) * 1760,
            'mift': ans = float(num1) * 5280,
            'miin': ans = float(num1) * 63360,
            'micm': ans = float(num1) * 160934.4,
            'mimm' : ans = float(num1) * (1.609*(10**6)),
            'mium': ans = float(num1) * (1.609*(10**9)),
            'minm': ans = float(num1) * (1.609*(10**12)),

            # Kilometre Conversion
            'kmkm': var1 * 1
            'kmcm': ans = float(num1) * 100000
            'kmmm': ans = float(num1) * (1*(10**6))
            'kmum': ans = float(num1) * (1*(10**9))
            'kmnm': ans = float(num1) * (1*(10**12))
            'kmmi': ans = float(num1) / 1.609
            'kmyd': ans = float(num1) * 1093.613
            'kmft': ans = float(num1) * 3280.84
            'kmin': ans = float(num1) * 39370.079
            'kmnmi': ans = float(num1) / 1.852
            'kmm': ans = float(num1) * 1000
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
