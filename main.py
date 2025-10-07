from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()

tammy = Turtle()
tammy.shape("turtle")
tammy.color("orange")
tammy.penup()

tommy = Turtle()
tommy.shape("turtle")
tommy.color("yellow")
tommy.penup()

ninja = Turtle()
ninja.shape("turtle")
ninja.color("violet")
ninja.penup()

terry = Turtle()
terry.shape("turtle")
terry.color("green")
terry.penup()

teddy = Turtle()
teddy.shape("turtle")
teddy.color("blue")
teddy.penup()

screen = Screen()
screen.setup(width=500, height=450)

turtles = [timmy, tammy, tommy, ninja, terry, teddy]
turtle_strings = ["timmy", "tammy", "tommy", "ninja", "terry", "teddy"]
turtle_xcor = {}


def turtle_race():
    go_turtle = random.choice(turtles)
    go_turtle.forward(random.randint(1, 20))
    return go_turtle.xcor()

def find_winner():
    for turtle in turtles:
        def get_turtle_xcor(turtle):
            return turtle.xcor()
        xcor = get_turtle_xcor(turtle)
        turtle_xcor[turtle_strings[turtles.index(turtle)]] = xcor
    winner = max(turtle_xcor, key=turtle_xcor.get)
    return winner


player_msg = "Select your turtle name:\n Timmy = Red, Tammy = Orange, " \
      "Tommy = Yellow, Ninja = violet, Terry = Green, Teddy = Blue"
player_turtle = screen.textinput(title="Choose your turtle", prompt=player_msg).lower()


timmy.goto(x=-230, y=180)
tammy.goto(x=-230, y=110)
tommy.goto(x=-230, y=40)
ninja.goto(x=-230, y=-40)
terry.goto(x=-230, y=-110)
teddy.goto(x=-230, y=-180)


race_on = True


while race_on == True:
    turtle_pos = turtle_race()
    if turtle_pos >= 220:
        race_on = False

winning_turtle = find_winner()

if player_turtle == winning_turtle:
    print(f"Congratulations!! Your turtle - {player_turtle} was the winner!!")
else:
    print(f"Hard luck!! Your turtle - {player_turtle} did not win this time. The winner was {winning_turtle}")


screen.exitonclick()