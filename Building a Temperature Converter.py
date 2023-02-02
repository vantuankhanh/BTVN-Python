from tkinter import *
from tkinter.ttk import *

main = Tk()
main.geometry('250x100+700+400')
main.title('C to F')
main.resizable(width=False, height=False)

def CtoF():
    C = int(degreeC.get())
    F = round((9/5 * C + 32),2)
    resultC['text'] = str(F)+' \N{DEGREE FAHRENHEIT}'

def FtoC():
    F = int(degreeF.get())
    C = round((5/9 * (F - 32)),2)
    resultF['text'] = str(C)+' \N{DEGREE CELSIUS}'
    
degreeC = StringVar()
degreeF = StringVar()

entryC = Entry(main, textvariable= degreeC, width=10)
entryC.place(x=30, y=15)
lbC = Label(main, text='\N{DEGREE CELSIUS}')
lbC.place(x=100, y=15)
btC = Button(main, text='\N{RIGHTWARDS BLACK ARROW}', width=5, command=CtoF)
btC.place(x=120, y=15)
resultC = Label(main, text='\N{DEGREE FAHRENHEIT}', width=10, anchor='e')
resultC.place(x=160,y=15)

entryF = Entry(main, textvariable= degreeF, width=10)
entryF.place(x=30, y=45)
lbF = Label(main, text='\N{DEGREE FAHRENHEIT}')
lbF.place(x=100, y=45)
btF = Button(main, text='\N{RIGHTWARDS BLACK ARROW}', width=5, command=FtoC)
btF.place(x=120, y=45)
resultF = Label(main, text='\N{DEGREE CELSIUS}', width=10, anchor='e')
resultF.place(x=160,y=45)

main.mainloop()