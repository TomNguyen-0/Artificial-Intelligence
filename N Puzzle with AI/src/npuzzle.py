'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date:  February 27, 2018

Assignment 2
'''

from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem
import math

class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """
    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any any remaining arguments captured in **kwargs.
        """
        
        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments 
        # into a dictionary.  The dictionary can be accessed like any other 
        # dictionary, e.g. kwargs["keyname"], or passed to another function 
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).

        #raise NotImplemented
        goal_state = self.make_goal(int(math.sqrt(n+1)))
       # print('goal_state ',goal_state)#goal_state  [[1, 2, 3], [4, None, 5], [6, 7, 8]]
        goal_state = [[1,3,5],[4,2,None],[6,7,8]]
        if force_state == None:
            puzzle = TileBoard(n)
        else:
            puzzle = TileBoard(n,force_state=force_state)
#        print(puzzle)
        super (NPuzzle,self).__init__(initial=puzzle,goals=goal_state,**kwargs)

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        return state.get_actions()
        raise NotImplemented
    
    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        if action not in self.actions(state):
            raise ValueError ('%d is not a legal action' %action)
        return state.move(action)
        raise NotImplemented
    
    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        return state in self.goal
        raise NotImplemented

    def make_goal(self,size):       
        self.size =size
        self.list=[]
        list_row=[]
        number_to_add_to_list=0
        if size%2 ==0: #even rows. the None is at the end of the list. not a good use for even numbers
            for i in range(size):
                for j in range(size):
                    number_to_add_to_list = number_to_add_to_list +1
                    list_row.append(number_to_add_to_list)
                self.list.append(list_row)
                list_row=[]
            self.list[size-1][size-1]=None
        else:       #odd rows
            middle = int(size/2)
            for i in range(size):
                if(i!=middle):
                    for j in range(size):
                        number_to_add_to_list = number_to_add_to_list +1
                        list_row.append(number_to_add_to_list)
                    self.list.append(list_row)
                    list_row=[]
                else:
                    for j in range(size):
                        if(j==middle):#we found the middle tile
                            list_row.append(None)
                            continue
                        number_to_add_to_list = number_to_add_to_list +1
                        list_row.append(number_to_add_to_list)
                    self.list.append(list_row)
                    list_row=[]
        return self.list
        



