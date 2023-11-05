# PYROGATRET
pong is a table tennis-themed 2-player 2D arcade video game developed in the early 1970s. The game consists of two paddles/strikers, located at the left and right edges of the screen, and a ball.

Create a Pong Game in Python
The basic theme of this game is to make sure that the ball doesn’t hit the wall behind you. If it does, the opponent scores a point. And if the ball touches the opponent’s wall, you score a point. This article covers how to create such a game in Python using the Pygame module. 

Key Controls
This is 2 player game and hence there will be two controllable paddles in the game. One at the leftmost edge of the screen and the other at the rightmost edge of the screen

To control the left paddle, use the ‘s’ and ‘w’ keys. ‘w’ will move the paddle upwards and ‘s’ will move the paddle downwards
To control the right paddle, use the UP and DOWN arrow keys. UP arrow will move the paddle upwards and the DOWN arrow will move the paddle downwards
Implementation to Create a Pong Game in Python
The game is developed in the Object Oriented Programming(OOP) style.

Create a “Striker” (paddle) class that handles all the controls related to the player
Create a “Ball” class that handles all the controls related to the ball
Two objects of the Striker class, geek1, and geek2, are instantiated
One object of the Ball class is instantiated.
The “main” function acts as the game manager and controls the game logic and flow
Initial Setup: This is the initial setup that consists of all the initializations and global variables that are needed
