import turtle
import random
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())

def draw_line(p):
    turtle.pendown()
    turtle.goto(p)

def draw_k(a, b, n):
    for i in range(0, 360 * n, 8):
        t = math.radians(i)
        x = abs(a - b) * math.cos(t) + b * math.cos(t * (a / b - 1))
        y = abs(a - b) * math.sin(t) - b * math.sin(t * (a / b - 1))
        draw_point((x, y))
    pass

def draw_butterfly():
    for i in range(0, 360 * 12, 4):
        t = math.radians(i)
        x = math.sin(t) * ((math.exp(math.cos(t))) - 2 * math.cos(4 * t) - (math.sin(t/12) ** 5))
        y = math.cos(t) * ((math.exp(math.cos(t))) - 2 * math.cos(4 * t) - (math.sin(t/12) ** 5))
        draw_point((x * 100, y * 100))
    pass

def draw_jk(a, b, c, d, j, k):
    for i in range(0, 36000 * 28, 1):
        t = math.radians(i / 100)
        x = math.cos(a * t) - (math.cos(b * t) ** j)
        y = math.sin(c * t) - (math.sin(d * t) ** k)
        draw_line((x * 100, y * 100))
    pass

prepare_turtle_canvas()

# draw_line_basic(p1, p2)

n = 20
a = 65
b = 100

draw_k(a, b, n)
# draw_butterfly()
# draw_jk(2, 200, 200, 1, 3, 4)

turtle.done()