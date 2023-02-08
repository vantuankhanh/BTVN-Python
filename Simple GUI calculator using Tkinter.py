from tkinter import *

main = Tk()
main.title('Calculator')
main.geometry('378x220+700+400')

def add_button(n):
    current = e.get()
    e.delete(0, END)
    e.insert(0, string=current + str(n))

def minus():
    current = e.get()
    if int(current)>=0:
        e.insert(0,'-')
    else:
        e.delete(0)

def clear():
    e.delete(0, END)

def equal():
    global cal
    global f_num
    s_num = int(e.get())
    e.delete(0, END)
    if cal == 'add':
        e.insert(0, str(f_num+s_num))
    elif cal == 'sub':
        e.insert(0, str(f_num-s_num))
    elif cal == 'mul':
        e.insert(0, str(f_num*s_num))
    elif cal == 'div':
        try:
            e.insert(0, str(f_num/s_num))
        except:
            e.insert(0, 'Syntax Error')

def push_calculate(calculation):
    global cal
    global f_num
    cal = calculation
    f_num = int(e.get())
    clear()

e = Entry(main, width=40)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

b1 = Button(main, text='1', padx=40, pady=10, command=lambda: add_button(1))
b2 = Button(main, text='2', padx=40, pady=10, command=lambda: add_button(2))
b3 = Button(main, text='3', padx=40, pady=10, command=lambda: add_button(3))
b4 = Button(main, text='4', padx=40, pady=10, command=lambda: add_button(4))
b5 = Button(main, text='5', padx=40, pady=10, command=lambda: add_button(5))
b6 = Button(main, text='6', padx=40, pady=10, command=lambda: add_button(6))
b7 = Button(main, text='7', padx=40, pady=10, command=lambda: add_button(7))
b8 = Button(main, text='8', padx=40, pady=10, command=lambda: add_button(8))
b9 = Button(main, text='9', padx=40, pady=10, command=lambda: add_button(9))

bminus = Button(main, text='+/-', padx=34, pady=10, command=minus)
b0 = Button(main, text='0', padx=40, pady=10, command=lambda: add_button(0))

cal = ''
b_add = Button(main, text='+', padx=39, pady=10, command=lambda: push_calculate('add'))
b_sub = Button(main, text='-', padx=39, pady=10, command=lambda: push_calculate('sub'))
b_mul = Button(main, text='x', padx=39, pady=10, command=lambda: push_calculate('mul'))
b_div = Button(main, text='/', padx=39, pady=10, command=lambda: push_calculate('div'))
b_equal = Button(main, text='=', padx=39, pady=10, command=equal)

b_clear = Button(main, text='Clear', padx=30, pady=10, command=clear)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

bminus.grid(row=4, column=0)
b0.grid(row=4, column=1)

b_add.grid(row=1, column=4)
b_sub.grid(row=2, column=4)
b_mul.grid(row=3, column=4)
b_div.grid(row=4, column=4)
b_equal.grid(row=4, column=2)

b_clear.grid(row=0, column=4)

mainloop()