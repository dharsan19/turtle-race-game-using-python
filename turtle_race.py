from turtle import *
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Place your bet !!", prompt="Which Turtle will win? Type the color (red, blue, green, orange, purple, cyan)")
is_game_on = False

all_turtles = []
colors = ["red", "blue", "green", "orange", "purple", "cyan"]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y = -80 + i*30)
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winner_turtle = turtle.pencolor()
            
            writer = Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(0, 150)  # Position at the top center
            writer.write(f"The winner is {winner_turtle} turtle!",
                         align="center", font=("Arial", 18, "bold"))

            if user_bet == winner_turtle:
                writer.goto(0, 120)
                writer.write("🎉 You WON the bet! 🎉", align="center", font=("Arial", 16, "normal"))
            else:
                writer.goto(0, 120)
                writer.write("😢 You LOST the bet!", align="center", font=("Arial", 16, "normal"))

        speed = random.randint(0,10)
        turtle.forward(speed)

screen.exitonclick()