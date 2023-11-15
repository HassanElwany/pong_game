from turtle import Screen, Turtle

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

padle = Turtle("square")
padle.color("white")
padle.penup()
padle.shapesize(stretch_wid=5, stretch_len=1)
padle.goto(350,0)

def go_up():
    new_y = padle.ycor() + 20
    padle.goto(padle.xcor(), new_y)


def go_down():
    new_x = padle.ycor() - 20
    padle.goto(padle.xcor(), new_x)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
