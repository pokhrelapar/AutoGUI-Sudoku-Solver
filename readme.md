# Sudoku Solver

## Introduction


This is a Python based sudoku solver that supports automated solving of  most of the online sudoku games. You can also use this to solve other 
digital based sudoku puzzles as long as you are able to move from one cell to the other using arrow keys.

## Sudoku

Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, 
column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game. If you
play Sudoku daily, you will soon start to see improvements in your concentration and overall brain power. Start a game now. Within no
time Sudoku free puzzles will be your favorite online game.

## How to play Sudoku

The goal of Sudoku is to fill in a 9×9 grid with digits so that each column, row, and 3×3 section contain the numbers between 1 to 9. 
At the beginning of the game, the 9×9 grid will have some of the squares filled in. Your job is to use logic to fill in the missing digits 
and complete the grid. Don’t forget, a move is incorrect if:

-Any row contains more than one of the same number from 1 to 9

-Any column contains more than one of the same number from 1 to 9

-Any 3×3 grid contains more than one of the same number from 1 to 9


## Libraries Used

-PyAutoGui

-Time

-Numpy

## Sample Run


https://user-images.githubusercontent.com/37117865/181810012-ac1e26bb-7577-4d55-8500-3d6da97521bf.mp4




## How to run

Clone the repository. Install necessary dependencies. Follow the user prompt displayed. Input each of the rows (1-9) of the sudoku without any special 
characters or spaces between two values. If a gird is empty, enter the value as 0. Always enter the value starting form the first row. Enusre that 
you only enter 9 values in each row.

Example: If this is the first row of the sudoku, where x marks the empty cells


![image](https://user-images.githubusercontent.com/37117865/181800668-aa1621e7-ce0e-4a71-ad9f-bd6cc45c6bb2.png)



Input the row as : 230000007

Follow the same for each of the 1-9 rows


Open any online sudo games. [Sample Game](https://sudoku.com). You can also copy a vlaid suodku puzzle and make a table in Excel or Word as long as you can move between the cells using arrow keys.

After you input the last row into the program, quickly switch to the window running the game. Click on the first cell of the sudoku. i.e (0,0) cell 
and wait for the programto auto fill the solution.

Notice the time it takes to solve easy, medium, and hard puzzles.
 

## Limitations

The program does not support solving for physical sudoku copies or digital copies that do not support trigger events through arrow keys :(


## Future Work

-Automate fillup on images wihtout with key trigger events
-Autofill missing values using grid detection and OpenCV


## References
https://pyautogui.readthedocs.io/en/latest/
https://sudoku.com/




