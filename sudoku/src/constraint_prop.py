'''
Constraint propagation
'''
'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date: April 12,2018

Assignment  4- constraint_prop.py

lecture 05 constraint satisfaction - slide page 15
'''

from csp_lib.csp import *

from csp_lib.sudoku import (Sudoku, easy1, harder1)

def AC3(csp, queue=None, removals=None):
    
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    cps.neighbors[x] is the neighbors of variable x
    
    #None
    #print(csp.display(csp.infer_assignment()))
    queue=True
    list = []
    for spots in csp.variables:#print(spots) # 81 spots
        for parts in csp.neighbors[spots]:#print(parts)
            list.append((spots,parts))#print(list)#[(0, 1), (0, 2), (0, 3), ...]
    list.reverse()#start from position 0 instead of position 80
    while list:
        (x,y)=list.pop()#pop an item off the list
        for row in csp.curr_domains[x]:#check for a value that we can use
            not_constraints = ( not csp.constraints(x,row,y,col) for col in csp.curr_domains[y])#lecture 05 page 15
            check = all (not_constraints)
            if check:
                csp.prune(x,row,removals=removals)
                if len(csp.curr_domains[x]) is not 0:#there is a possible solution
                    for next in csp.neighbors[x]:
                        list.append((next,x))
                else:
                    queue=False
                    return queue  
    return queue
 
'''
if __name__ == '__main__':
    easy1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    harder1 = '4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    
    e = Sudoku(easy1)
    AC3(e)
    e.display(e.infer_assignment())
    h = Sudoku(harder1)
    print()
    AC3(h)
    h.display(h.infer_assignment())
'''    