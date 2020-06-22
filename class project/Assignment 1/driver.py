#comment
'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date: February 06,2018

Assignment 1 - driver.py

build a driver that will call tileboard

put the driver into a while loop as long as the puzzle is not solved
    make a two list one for the menu and the other the direction
    put it in a loop to append into the list.
    the format of the out put will be w.(up)[1,0] etc. (using wsad to move up down left right)
    the movement can be changed to 5213 if we want to use the pad number. This is commented out.
once it is solved pull out and tell them that they won.
'''
from boardtypes import TileBoard

def driver():
    size=8
    puzzle = TileBoard(size)
#    puzzle = TileBoard(size,[2,3,None,1,6,8,7,5,4]) #known solution to puzzle, used for testing

    #checks if the puzzle is already solved
    is_it_solved = puzzle.solved()
    #keep in the loop until solved
    while not is_it_solved:
        print(puzzle.__repr__())
        menu=None
        menu=[]
        direction=None
        direction=[]
        list_of_possible_moves = puzzle.get_actions()
        for number_of_possible_moves in range (len(list_of_possible_moves)):
            if(list_of_possible_moves[number_of_possible_moves][0] == -1):
                #menu.append('5')
                menu.append('w')
                direction.append('up')
            elif(list_of_possible_moves[number_of_possible_moves][0] == 1):
                #menu.append('2')
                direction.append('down')
                menu.append('s')
            elif(list_of_possible_moves[number_of_possible_moves][1] == 1):
                #menu.append('3')
                direction.append('right')
                menu.append('d')
            else:
                #menu.append('1')
                direction.append('left')
                menu.append('a')
            #if we want to have letters instead A., B., C., D.
            #menu.append(chr(ord('A')+number_of_possible_moves))
             
        print("valid actions (row,column): ")
        #display  A.{direction}[x, x]
        for(letters,moves,directions) in zip (menu,list_of_possible_moves,direction):
            print("{}.({}){}  ".format(letters,directions,moves),end="")
        print()
        choose = None
        keyboard = "Choose a number: "
        while choose not in menu:
            choose = input(keyboard)
            #keyboard = "invalid number, pick again: "
            keyboard = "invalid letter, (the letter should be lower case). Try again."
        print()
        puzzle = puzzle.move(menu.index(choose))
        is_it_solved = puzzle.solved()
    print(puzzle.__repr__())
    print("You Win! You are a winner")
        
        
if __name__ == '__main__':
    driver()
    


