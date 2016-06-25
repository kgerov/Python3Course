import turtle
side=40
xcord = 0
ycord = 0

turtle.speed('fastest');
turtle.penup()
turtle.goto(-180, -300)
turtle.pendown()

for j  in range(8):
    if j != 0:
        turtle.penup()
        turtle.goto(xcord, ycord)
        turtle.pendown()

    for i in range(8):
        if ((i % 2==0) and (j % 2 == 0)) or ((i % 2==1) and (j % 2 == 1)):
            turtle.begin_fill()

        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)

        if i == 0:
            xcord = turtle.xcor();
            ycord = turtle.ycor();

        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
turtle.exitonclick()