from tkinter import *

main = Tk()
main.geometry('500x150+700+400')
main.resizable(0,0)

def convert():
    global weight
    kg = float(weight.get())
    t_gram.delete('1.0',END)
    t_gram.insert('1.0', str(round(kg*1000,2)))
    t_pound.delete('1.0',END)
    t_pound.insert('1.0', str(round(kg*2.20462,2)))
    t_ounce.delete('1.0',END)
    t_ounce.insert('1.0', str(round(kg*35.274,2)))

weight = StringVar()

l1 = Label(main, text='Enter the weight in Kg', padx=10, pady=10)
l_gram = Label(main, text='Gram', padx=20, pady=10)
l_pound = Label(main, text='Pounds', padx=20, pady=10)
l_ounce = Label(main, text='Ounce', padx=20, pady=10)

e1 = Entry(main, textvariable=weight, width=30)

b1 = Button(main, text='Convert', padx=2, pady=2, command=convert)

t_gram = Text(main, width=10, height=1)
t_pound = Text(main, width=10, height=1)
t_ounce = Text(main, width=10, height=1)

l1.grid(row=0, column=0)
l_gram.grid(row=1, column=0)
l_pound.grid(row=1, column=1)
l_ounce.grid(row=1, column=2)

e1.grid(row=0, column=1, padx=10)

b1.grid(row=0, column=2, padx=40)

t_gram.grid(row=2, column=0)
t_pound.grid(row=2, column=1)
t_ounce.grid(row=2, column=2)

main.mainloop()