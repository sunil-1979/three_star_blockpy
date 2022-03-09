import turtle
turtle.fillcolor('yellow')
# first star
turtle.begin_fill()
turtle.right(36)
for i in range(5):
    turtle.pencolor('black')
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()

turtle.left(36)
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.right(36)

#second star
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.pendown()
for i in range(5):
    turtle.pencolor('black')
    turtle.forward(75)
    turtle.left(144)
turtle.end_fill()

turtle.left(36)
turtle.forward(75)
turtle.penup()
turtle.forward(25)
turtle.right(36)

#third star
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.pendown()
for i in range(5):
    turtle.pencolor('black')
    turtle.forward(100)
    turtle.left(144)
turtle.end_fill()

turtle.left(36)
turtle.forward(100)
turtle.penup()
turtle.forward(25)
turtle.right(36)




