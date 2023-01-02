import turtle
a=turtle.Turtle()
r=100
d=0
t=30
c=['red','yellow','orange','blue','green']
turtle.bgcolor('black')
while d<t:
    a.color(c[d%5])
    for i in range(2):
        a.circle(r,90)
        a.circle(r/2,90)
    a.left(360/t)
    d+=1
t.done