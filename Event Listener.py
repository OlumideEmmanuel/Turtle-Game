from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_right():
    timmy.right(10)

def move_left():
    timmy.left(10)

def clear():
    timmy.clear()
    timmy.hideturtle()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    timmy.showturtle()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "a")
screen.onkey(move_left, "d")
screen.onkey(clear, "c")



screen.exitonclick()