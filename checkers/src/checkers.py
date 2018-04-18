'''
Created on Feb 22, 2015

@author: mroch
'''

import time
import datetime
import checkerboard
# tonto - Professor Roch's not too smart strategy
# You are not given source code to this, but compiled .pyc files
# are available for Python 3.5 and 3.6 (fails otherwise).
# This will let you test some of your game logic without having to worry
# about whether or not your AI is working and let you pit your player
# against another computer player.
#
# Decompilation is cheating, don't do it.
#import tonto
# human - human player, prompts for input    
import human
import boardlibrary # might be useful for debuggingimport tonto
import human
import ai
import boardlibrary # might be useful for debugging
from itertools import count # counts up infinitely from a value
import imp
import sys
#major = sys.version_info[0]
#minor = sys.version_info[1]
#modpath = "__pycache__/tonto.cpython-{}{}.pyc".format(major, minor)
#tonto = imp.load_compiled("tonto", modpath)

def elapsed(earlier, later):
    """
    elapsed - Convert elapsed time.time objects to duration string
    
    Useful for tracking move and game time.  Example pseudocode:
    
    gamestart = time.time()
    
    while game not over:
        movestart = time.time()
        ...  logic ...
        current = time.time() 
        print("Move time: {} Game time: {}".format(
            elapsed(movestart, current), elapsed(gamestart, current))
    
    
    """
    return time.strftime('%H:%M:%S', time.gmtime(later - earlier))
           
                                    #tonto.Stragegy
                                    
def Game(red=ai.Strategy, black=ai.Strategy, maxplies=5, init=None, verbose=True, firstmove=0):
#def Game(red=human.Strategy, black=ai.Strategy, maxplies=5, init=None, verbose=True, firstmove=0):
    """
    Game(red, black, maxplies, init, verbose, turn)
    Start a game of checkers
    red,black - Strategy classes (not instances)
    maxplies - # of turns to explore (default 10)
    init - Start with given board (default None uses a brand new game)
    verbose - Show messages (default True)
    firstmove - Player N starts 0 (red) or 1 (black).  Default 0. 
    """

    # Don't forget to create instances of your strategy,
    # e.g. black('b', checkerboard.CheckerBoard, maxplies)
    
    checker_board = checkerboard.CheckerBoard()#creating an instance of the board.#checker board.   0  1  2  3  4  5  6  7\n0     b     b     b     b
#    print(checker_board)
    red_player = red('r', checkerboard.CheckerBoard, maxplies)
    black_player = black('b',checkerboard.CheckerBoard, maxplies)
    
    for i in count(2):
        whose_turn_is_it_anyways = i %2 #print('whose {}'.format(whose_turn_is_it_anyways))#whose 0
        if( whose_turn_is_it_anyways == 0):
            print("Player Red, Pick a move")
            checker_board = red_player.play(checker_board)[0]#display the possible moves
            print("Red Moved\n")
        else:#print('whose {}'.format(whose_turn_is_it_anyways))#whose 1
            print("Pick a move, Player Black")
            checker_board = black_player.play(checker_board)[0]
           # checker_board = black_player()
            print("Black Moved\n")
       # print (checker_board)
        if checker_board.is_terminal()[0]:
            if whose_turn_is_it_anyways ==0:
                print('CONGRATULATIOINS RED. You won!')
            else:
                print('CONGRATULATIONS BLACK. You won!')
            print(checker_board)
            break
    'sidenote: the F does not work when trying to forfeit'


if __name__ == "__main__":
    Game()  
        
        
        


        
                    
            
        

    
    
