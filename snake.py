import turtle

SNAKE_BODY = [(0,0),(-20,0),(-40,0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_body()
        self.head = self.segments[0]



    def snake_body(self):
        for every_element in SNAKE_BODY:
            snake = turtle.Turtle("circle")
            snake.color("#654321")
            snake.penup()
            snake.goto(every_element)
            self.segments.append(snake)
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
