from turtle import *

speed(100)
width(6.4)
penup()

right(90)
forward(300)

pendown()

right(90)
forward(300)
right(180)
forward(565)
left(90)
forward(400)
left(90)
forward(565)
left(90)
forward(400)

left(180)
forward(400)
color("red")
right(45)
begin_fill()
forward(200)
right(90)
forward(200)
left(90)
forward(200)
right(90)
forward(200)
end_fill()


penup()
goto(0, -300)
pendown()

color("black")

left(-135)
forward(150)


back(60)
color("brown")
begin_fill()
right(90)
forward(150)
right(90)
forward(120)
right(90)
forward(150)
end_fill()

penup()

back(250)
left(90)
forward(237)
pendown()


exitonclick()