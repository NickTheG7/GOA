from turtle import*
#i want to make a house
speed(40)

width(7)
color("green")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roof
penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window1
penup()
goto(200, 200)
forward(75)
pendown()
width(7)
color("blue")
begin_fill()
right(60)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)





end_fill()

#window2
penup()
goto(0, 200)
left(45)
forward(90)
right(45)
width(7)
color("blue")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()
pendown()




















exitonclick()


