import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.scorebar()

screen.listen()
screen.onkey(turtle.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            scoreboard.game_over()
        
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.score_up()



screen.exitonclick()
