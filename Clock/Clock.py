import turtle
import datetime

screen = turtle.Screen()
screen.setup(1500,800)
screen.setworldcoordinates(-1500, -800, 1500, 800)
screen.bgpic('beach.gif')
screen.tracer(0,0)

class clock:    
    def __init__(self,hour,minute,second):
        self.hour, self.minute, self.second = hour, minute, second
        self.hand = turtle.Turtle()
        self.face = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()
    
    def draw_face(self):
        self.face.hideturtle()
        #draw clock's edge
        self.face.penup()
        self.face.goto(0,-500)
        self.face.color('#745E11')
        self.face.pensize(3)
        self.face.pendown()
        self.face.begin_fill()
        self.face.circle(500)
        self.face.end_fill()
        self.face.penup()
        #draw number of hour
        number_r = 430
        number_size = 30
        angle = [i for i in range(360,0,-6)]
        self.face.goto(0,number_r-1.5*number_size)
        self.face.setheading(180)
        self.face.pencolor('#EBC028')
        for i in angle:            
            if angle.index(i)%5==0:
                number = '12' if angle.index(i)==0 else str(angle.index(i)//5)
                self.face.write(number,align='center',font=('Arial',number_size,'bold'))
                self.face.circle(number_r,-6)
            else:
                self.face.circle(number_r,-6)
        #center dot    
        self.face.goto(0,0)
        self.face.dot(10)
        #edge minute
        self.face.setheading(90)
        for i in angle:
            self.face.penup()
            self.face.forward(480)
            self.face.pendown()
            if i%5==0:
                self.face.pensize(4.5)
            else:
                self.face.pensize(2)
            self.face.forward(10)
            self.face.penup()
            self.face.goto(0,0)
            self.face.right(6)
        
    def draw_hand(self):
        self.hand.hideturtle()
        #hour hand
        self.hand.clear()       
        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-((self.hour%12)*60*60+self.minute*60+self.second)/3600*30)
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(200)
        #minute hand
        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-(self.minute*60+self.second)/60*6)
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(300)
        #second hand
        self.hand.up()
        self.hand.color('red')
        self.hand.goto(0,0)
        self.hand.dot(5)
        self.hand.seth(90-self.second*6)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(400)

def running():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second = d.hour, d.minute, d.second
    c.draw_hand()
    screen.update()
    screen.ontimer(running,1000)
    
d = datetime.datetime.now()
c = clock(d.hour,d.minute,d.second)
c.draw_face()
screen.update()
running()
turtle.exitonclick()