from turtle import Turtle, Screen

turt = Turtle()


def clear():
    turt.clear()


def move_forward():
    turt.forward(20)


def move_backwards():
    turt.backward(20)


def turn_right():
    turt.right(10)


def turn_left():
    turt.left(10)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
