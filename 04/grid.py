import turtle

size = 0

while(size < 6):
    turtle.penup()
    turtle.goto(-300, -300 + 100 * size)
    turtle.pendown()
    turtle.forward(500)
    size+=1

size = 0
turtle.left(90)

while(size < 6):
    turtle.penup()
    turtle.goto(-300 + 100 * size, -300)
    turtle.pendown()
    turtle.forward(500)
    size+=1

turtle.exitonclick()
