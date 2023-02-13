from tkinter import *

class Ball:
    def __init__(self, canvas, dimension_x, dimension_y):
        pass




main = Tk()
main.geometry('550x570+700+200')
main.resizable(width=False, height=False)
main.title('Bouncing Ball Game')
main.wm_attributes('-topmost',1)

canvas = Canvas(main, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)

score = Label(height=50, width=80, text="Score: 00", font="Calibri 14 italic")
score.pack(side="left", pady=5)

main.mainloop()