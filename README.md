# isola_bot
A bot for playing isola game.

Isola is a two-player board game. It is played on a 7x7 grid which is initially filled with squares on each cell. Both players have one piece; it is in the middle position of the row closest to his/her side of the board. Players can place their piece on squares only.

A move consists of two subsequent actions: 

1. Moving one's piece to a neighboring (horizontally, vertically, or diagonally) position that contains a square but not the opponent's piece. 
2. Removing any square with no piece on it. 

The player who cannot move his/her piece loses the game. 

Input 
The input will be an 7x7 matrix consisting only of 0, 1, 2 and -1. Then another line will follow which will contain a number 1 or 2, which is your player id. The difference between player 1 and 2 is that player 1 plays first in start of the game. 

In the given matrix, top-left is [0,0] and bottom-right is [6,6]. The coordinate of a cell is represented by [row, column]. Rows increases from top to bottom and column increases from left to right. 

The cell marked 0 means it contains a square which is yellow in color. The cell marked 1 means it contains player 1's piece which is blue in color. The cell marked 2 means it contains player 2's piece which is red in color. The cell marked -1 means it doesn't contain the square. The board is brown in color. 

Output 
Print the coordinates of the neighbor cell [row, column] where you want to move your piece. In next line, print the coordinates of any cell to remove the square. 

