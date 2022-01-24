import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
c=("yellow","red","purple","cyan","light green","blue")
for i in range(150):
    t.pencolor(c[i%6])
    t.circle(190-1/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)
s.exitonclick()