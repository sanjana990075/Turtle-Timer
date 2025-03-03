import turtle
import time
hr=int(turtle.numinput("timer","Hour"))
min=int(turtle.numinput("timer","minute"))
sec=int(turtle.numinput("timer","second"))
s=turtle.Turtle()
t=turtle.Turtle()
s.speed(0)
turtle.bgcolor("black")
s.color("white")
s.hideturtle()
s.pensize(2)
s.penup()
s.goto(-200,-50)
s.pendown()
s.forward(400)
s.left(90)
s.forward(100)
s.left(90)
s.forward(400)
s.left(90)
s.forward(100)
t.color("white")
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-115,-35)
t.pendown()
while(1):
    t.write(str(hr).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2),font=("Arial", 60, "normal"))
    time.sleep(1)
    sec-=1
    if sec==-1:
        sec=59
        min-=1
    if min==-1:
        min=59
        hr-=1
    if hr==0 and min==0 and sec==0:
        break
    t.undo()
t.penup()
t.goto(-180,100)
t.pendown()
t.color("red")
t.write("Alert! Timer up",font=(("Arial", 40, "normal")))
turtle.mainloop()