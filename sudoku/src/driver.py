'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date: April 12,2018

Assignment  4- driver.py
'''


from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv
from backtrack import backtracking_search
from csp_lib.backtrack_util import no_inference

def driver():
    'for sudoku problems - https://www.websudoku.com/?level=3'
    easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    mediu = '4.2.6...8..59.....6...18.5.3.1..9..7..8...4..9..8..2.1.9.58...2.....18..8...7.9.3'
    harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    evil = '.....19.....58...6...2..58.5.96..7..3.......1..7..28.4.92..7...7...24.....68.....'
    list = []
    list.append(easy1)
    list.append(mediu)
    list.append(harder1)
    list.append(evil)
    for puzzle in list:
        if puzzle == easy1:
            print("*****easy sudoku*****")
        elif puzzle == mediu:
            print("*****medi sudoku*****")
        elif puzzle == evil:
            print("*****evil sudoku*****")
        else:
            print("*****hard sudoku*****")
        s  = Sudoku(puzzle)  # construct a Sudoku problem
        s.display(s.infer_assignment())#problem
        print()
        AC3(s)
        s.display(s.infer_assignment())#solved
        if not s.goal_test(s.curr_domains):#the puzzle is not solved. hard sudoku
            print()
            solved = backtracking_search(s, select_unassigned_variable=mrv,inference=no_inference)
            print("     backtracking     ")
            s.display(s.infer_assignment())#solved
            print()
        else:
            print()


'used: https://www.sudoku-solutions.com/ to check solution'
if __name__ == '__main__':
    driver()

    