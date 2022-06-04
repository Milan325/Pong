# Pong game
This game is classic Pong game for two players. Players hit the ball with paddle, goal being to make the other player miss the ball.

## Rules
Two paddles for two players are set. Left paddle is controlled by "W" and "S" keys, and the right one is controlled by "Up" and "Down" keys. Players hit the ball, and if a player misses it, then the other player gets a point. Winner is player that first reaches 10 points.

## Modules, functions and classes
Module used for GUI of this game is `turtle` module. 

### `paddle.py`
This module defines `Paddle(Turtle)` subclass of Turtle superclass and `middle_line()` function.
`Paddle(Turtle)` requires `position` argument in the form of a tuple, and this argument differentiates between two players. Turtle object is created that is white, square-shaped, stretched for 5px and placed in wanted position.
Methods `go_up()` and `go_down()` are bound to `onkey()` function, and move Paddle object for 20px in defined direction.
Part of this module is `middle_line(center)` function, with given kw argument, that uses Turtle object to draw a line in the middle of the window. The pattern is got by using `while` loop inside which a repeating procedure is given.

### `ball.py`
This module defines `Ball(Turtle)` subclass of the Turtle superclass. At the initialization, circle shaped red Turtle object is created with starting arguments of 2. Movement of the Ball object is ruled by `move()`, `bounce_x()` and `bounce_y()` methods. `move()` takes `x_move` and `y_move` arguments to increase x and y coordinates of the ball object to move it using `Turtle.goto(x, y)` method.
`bounce_y` changes direction of movement upon hitting edge of the window (280 or -280 on y axis), and `bounce_x` to change direction and increase movement speed by 10%.
`reset_position()` is called when a player gets a point, and resets ball object position to center and moving speed to 1.

### `scoreboard.py`
This module defines `Scoreboard(Turtle)` subclass of Turtle superclass. Scoreboard object is of Turtle class that is used to write score at top of the screen. Score are saved in `l_score` and `r_score` variables. 
`update_scoreboard` method is used to write score points to the screen. `l_point()` and `r_pont()` update score arguments, and are called in game engine. `end()` method creates new Turtle object that checks if any of the players reached 10 points, and breaks from game engine by returning boolean value.

## Game engine
Game engine is a `while` loop embedded in GUI engine (from the calling of `Screen()` object to `screen.exitonclick()`). Inside `while` loop, screen is getting updated at the start of a cycle, and then series of if statements check ball position and calls appropriate methods in response to ball coordinates.

## Running the game
This game is intended to be run by Python IDE or other Python interpeter. 
To install Python 3 see [Tutorials Point page](https://www.tutorialspoint.com/how-to-install-python-in-windows).
