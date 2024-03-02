from turtle import *

#we want to paint a house

# draw a squarestep 1:
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of  the door

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(15, 160)
pendown()
begin_fill()
color("red")
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

penup()
goto(180, 160)
pendown()
begin_fill()
color("red")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()


exitonclick()