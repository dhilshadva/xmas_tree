from turtle import*
speed(0)

penup()
goto(0,-250)
pendown()
color("black")
begin_fill()
circle(250)
end_fill()
#trunk
penup()
goto(-15,-50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

#leaf
y=-50
width=240
height=25

while width > 20:
    width = width-30
    x=0-width/2
    color("green")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y=y+height

#star
penup()
goto(-15,150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

penup()
goto(-190,-130)
color("white")
write("MERRY CHRISTMAS & HAPPY NEWYEAR",font=("Albertus extra bold",15,"bold"))
end_fill()
#MSG
penup()
goto(60,-150)
color("white")
write("- DHILSHAD VA",font=("Albertus extra bold",15,"bold"))
end_fill()
#DECOR
penup()
goto(-40,91)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(10)
    right(-5)
    left(0)
hideturtle()

#2
penup()
goto(20,65)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(8)
    right(5)
    left(0)
hideturtle()

#1ball

import turtle
penup()
goto(-40,83)
pendown()
color("blue")
begin_fill()
circle(5)
end_fill()

#2ball

import turtle
penup()
goto(62,65)
pendown()
color("red")
begin_fill()
circle(5)
end_fill()

#2line
penup()
goto(-70,55)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(10)
    right(-5)
    left(0)
hideturtle()

#3ball
import turtle
penup()
goto(-70,45)
pendown()
color("yellow")
begin_fill()
circle(5)
end_fill()

#3line

penup()
goto(40,30)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(8)
    right(5)
    left(0)
hideturtle()

#4ball

import turtle
penup()
goto(80,30)
pendown()
color("magenta")
begin_fill()
circle(5)
end_fill()

#5th line

penup()
goto(-90,20)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(10)
    right(-5)
    left(0)
hideturtle()

#5thball


import turtle
penup()
goto(-90,10)
pendown()
color("cyan")
begin_fill()
circle(5)
end_fill()

#6th line

penup()
goto(60,5)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(8)
    right(5)
    left(0)
hideturtle()

#6th ball

import turtle
penup()
goto(98,3)
pendown()
color("orange")
begin_fill()
circle(5)
end_fill()

#7th line

penup()
goto(70,-20)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(10)
    right(-5)
    left(0)
hideturtle()

#7th ball

import turtle
penup()
goto(117,-20)
pendown()
color("cyan")
begin_fill()
circle(5)
end_fill()

#8th line

penup()
goto(-110,-20)
pendown()
color("red")
begin_fill()
for i in range(5):
    forward(8)
    right(5)
    left(0)
hideturtle()

#8th ball

import turtle
penup()
goto(-110,-25)
pendown()
color("red")
begin_fill()
circle(5)
end_fill()
