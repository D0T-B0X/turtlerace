from turtle import Turtle, Screen
from random import randint


colours = ["red", "green", "purple", "blue", "yellow", "maroon"]
screen = Screen()
screen.setup(800, 600)
user_input = screen.textinput(title="Turtle Race", prompt="Pick your color : ")
turtle_names = []
is_Race_On = False

for turtles in range(6):
    turt = Turtle(shape="turtle")
    turt.color(colours[turtles])
    turt.penup()
    turt.turtlesize(3)
    turt.goto(-360, -230+(92*turtles))
    turtle_names.append(turt)

if user_input:
    is_Race_On = True


while is_Race_On:
    for turtles in turtle_names:
        turtles.forward(randint(0, 10))
        if turtles.xcor() > 370:
            winningTurtle = turtles.pencolor()
            if winningTurtle == user_input:
                print(f"The winner is {winningTurtle}, You Won!!")
            else:
                print(f"The winner is {winningTurtle}, You Lost!")
            is_Race_On = False

screen.exitonclick()
