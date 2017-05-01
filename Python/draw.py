import turtle

def square(a_turtle):
    for i in range(1, 5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    line = turtle.Turtle()
    line.shape("turtle")
    line.color("blue")
    line.speed(2)
    for i in range(1, 37):
        square(line)
        line.right(10)

    '''jen = turtle.Turtle()
    jen.shape("arrow")
    jen.color("gold")
    jen.circle(50)'''

    window.exitonclick()

draw()
