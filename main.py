from turtle import Turtle, Screen

screen = Screen()

screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong-Game')


paddle = Turtle('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)


screen.exitonclick()