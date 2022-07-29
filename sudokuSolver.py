'''
 * @author [Apar Pokhre;]
 * @email [apu8467@gmail.com]
 * @create date 2022-07-29 08:26:11
 * @modify date 2022-07-29 08:26:11
 * @desc [Sudoku Solver using AutoGUI]
 




              Sudoku Rules

    * Rule 1 - Each row must contain the numbers from 1 to 9, without repetitions
    * Rule 2 - Each column must contain the numbers from 1 to 9, without repetitions
    * Rule 3 - The digits can only occur once per block (nonet) (i.e once within the 3x3 grid)
    * Rule 4 - The sum of every single row, column and nonet must equal 45

               Other Details under Consideration
    * Each Sudoku puzzle has only one possible solution that can only be achieved by following 
      the Sudoku rules correctly.
 
    * Multiple solutions only occur when the puzzle is poorly designed or, the most frequent reason,
      when the player makes a mistake in its resolution and a duplicate is hidden somewhere on the grid.

 
 
 
 
 '''

import pyautogui as pg 
import numpy as np
import time


# Add list to grid to make list of lists
grid = []

print("Inuput the sudoku values without spaces or special characters")
print("Example: 401000000")
while True:
    
    row = list(input('Row: '))


    intLists = []

    #Each number in the row, convert number to integer, and append as a list to grid
    for n in row:
        intLists.append(int(n))
    grid.append(intLists)

    if len(grid) == 9:
        break
    print('Added Row : ' + str(len(grid)))
    print()

time.sleep(5) #gives you time to switch to the sudoku window


'''
 isSolutionPossible checks if a number (n) is possible at coordinates (x,y)

 Example: is 1 possible at first row second column (0,1)

            +-----+-----+-----+
            |5    |  8  |  4 9|
            |     |5    |  3  |
            |  6 7|3    |    1|
            +-----+-----+-----+
            |1 5  |     |     |
            |     |2   8|     |
            |     |     |  1 8|
            +-----+-----+-----+
            |7    |    4|1 5  |
            |  3  |    2|     |
            |4 9  |  5  |    3|
            +-----+-----+-----+



'''

def isSolutionPossible(r, c, n):

    #For numbers 1-9 check in the x position, if  n exists at the position,then there already the same number in the row
    for i in range(0, 9):
        if grid[i][r] == n and i != c: # Checks for number (n) in X columns
            return False
    
    #For numbers 1-9 check in the x position, if  n exists at the position,then there already the same number in the column
    for i in range(0, 9):
        if grid[c][i] == n and i != r: # Checks for number (n) in Y columns
            return False

    #How to check within the 3x3 grids?

    #Map the coordinate (x,y) to the (0,0) coordinate of the 3x3 grid
    r0 = (r // 3) * 3
    c0 = (c // 3) * 3

    #For numbers 1-9 check if n exists within the 3x3 grid
    for R in range(r0, r0 + 3):
        for C in range(c0, c0 + 3):  # Checks for numbers in box
            if grid[C][R] == n:
                return False    
    return True

def Print(matrix):
    result = []
    finalResult = []
    for i in range(9):
        result.append(matrix[i])

    for lists in result:
        for num in lists:
            finalResult.append(str(num))

    # count how many have passed
    counter = []

    '''
    In pyautogui number pressed is represented as a string
    i.e 1 is represented as '1'



    autogui movements:

            move right by 1 until end of first row
            go down by 1 and then move to the left

            And repeat the process unitl you reach the bottom left

            +-----+-----+-----+
            |5    |  8  |  4 9|
            |     |5    |  3  |
            |  6 7|3    |    1|
            +-----+-----+-----+
            |1 5  |     |     |
            |     |2   8|     |
            |     |     |  1 8|
            +-----+-----+-----+
            |7    |    4|1 5  |
            |  3  |    2|     |
            |4 9  |  5  |    3|
            +-----+-----+-----+

    
    '''
    for num in finalResult:
        pg.press(num)
        pg.hotkey('right') #Move right by 1 position from the top left: (0,0) -> (0,1)
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

start = time.time()
#backtracking
def solveSudoku():
    global grid
    for c in range(9):
        for r in range(9):
            #if it is an empty grid, find what number should be in the empty space
            #such that the inteegrity of the sudoku game holds true
            if grid[c][r] == 0:
                for n in range(1, 10):
                    if isSolutionPossible(r, c, n):
                        grid[c][r] = n
                        solveSudoku()
                        grid[c][r] = 0 #if the sollution didn't work, set it to 0 and try again
                return
    Print(grid)

solveSudoku()
stop = time.time()

print()
print(f'Solved sudoku in  ~ {int(stop-start)} seconds')


'''
010700208
900050000
000000030
002007000
080200106
000000400
100009603
030000070
000600040

'''
