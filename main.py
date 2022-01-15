from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(width = 600, height = 600)     #for screen of 600x600
screen.bgcolor('black')                      #bg color pink
screen.bgpic("grass.png")
screen.title("Snake")                       #game name
screen.tracer(0)                            #will trace the animation

snake = Snake()                             #snake object from Snake class
food = Food()
scoreboard = Scoreboard()

            #KEY BINDINGS
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

            #KEY BINDINGS END
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()                            #calling the move object from snake
    if snake.head.distance(food) < 18:
        food.random_pos()
        scoreboard.score_plus()
        #detects walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()




screen.exitonclick()



