'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date:  February 27, 2018

Assignment 2

driver for graph search problem
Created on Feb 10, 2018

@author: mroch
'''

#from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies
import math


def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t

def mean(list):
    "return the mean of the list because i couldn't get numpy to work"
    return math.fsum(list)/len(list)
    

def standard_deviation_formulas(list_of_numbers):#list of numbers to be calulated
        mule =mean(list_of_numbers)
        x_subtract_mean_then_squared=[]
        #print('listl ',list_of_numbers)
        #print("mean ",mule)
        for i in range(len(list_of_numbers)):
            x_subtract_mean_then_squared.append((list_of_numbers[i]-mule)**2)
        y= mean(x_subtract_mean_then_squared)
        std= math.sqrt(y)
        #print('my std: ',std)#my std:  3.926748634520636
        return std
    
def table_summary(list_steps,list_explored,starting_time):
    #print('list: ',list_steps)#list:  [25, 24]
    #print('list: ',list_explored)#list:  [280, 1546]
    #print('list: ', starting_time)#list:  [0.06706500053405762, 0.39033007621765137]
    generic_list = list_steps
    print('                table summary: Steps for {} puzzles.'.format(len(generic_list)))
    print('    total: {} mean: {} std: {}'.format(math.fsum(generic_list),mean(generic_list),standard_deviation_formulas(generic_list)))
    generic_list = list_explored
    print('                table summary: Explored node for {} puzzles'.format(len(generic_list)))
    print('    total: {} mean: {} std: {}'.format(math.fsum(generic_list),mean(generic_list),standard_deviation_formulas(generic_list)))
    generic_list = starting_time
    print('                table summary for time')
    print('    total: {} mean: {} std: {}'.format(math.fsum(generic_list),mean(generic_list),standard_deviation_formulas(generic_list)))
    
    
def driver() :
    size = 8
    trials_size=31
    #puzzle = NPuzzle(size)
   # force_state = puzzle.initial.state_tuple()

  #  force_state = [1,3,5,4,2,None,6,7,8]
  #  force_state = [1,2,3,6,4,5,7,8,None]
  #  force_state = [3,2,1,5,4,6,7,8,None]
  #  print(puzzle.initial)
   # graph_search(NPuzzle(size,g=BreadthFirst.g, h=BreadthFirst.h,force_state= ),debug=True)#number of nodes explored: 31
    print("Breadth First Search (BFS)")
    list_of_explored=[]
    list_of_steps=[]
    list_of_time=[]
    for i in range(trials_size):
        puzzle = NPuzzle(size)
        force_state = puzzle.initial.state_tuple()
        start_time=tic()
        item_graph=graph_search(NPuzzle(size,g=BreadthFirst.g, h=BreadthFirst.h,force_state=force_state))
        list_of_time.append(tock(start_time))
        list_of_explored.append(item_graph[0])
        list_of_steps.append(item_graph[1])
    table_summary(list_of_steps, list_of_explored,list_of_time)
#    print(tock(start_time))

    print('A star search (Manhattan)')
    list_of_explored=[]
    list_of_steps=[]
    list_of_time=[]
    for i in range(trials_size):
        puzzle = NPuzzle(size)
        force_state = puzzle.initial.state_tuple()
        start_time=tic()
        item_graph=graph_search(NPuzzle(size, g=Manhattan.g, h=Manhattan.h,force_state=force_state))#first number is explored, second number is steps
        list_of_time.append(tock(start_time))
        list_of_explored.append(item_graph[0])
        list_of_steps.append(item_graph[1])
    table_summary(list_of_steps, list_of_explored,list_of_time)
    #print(list_of_steps)

    print('Depth First Search (DFS)')
    list_of_explored=[]
    list_of_steps=[]
    list_of_time=[]
    for i in range (trials_size):
        puzzle = NPuzzle(size)
        force_state = puzzle.initial.state_tuple()
        start_time=tic()
        item_graph=graph_search(NPuzzle(size, g=DepthFirst.g, h=DepthFirst.h,force_state=force_state))
        list_of_time.append(tock(start_time))
        list_of_explored.append(item_graph[0])
        list_of_steps.append(item_graph[1])
    table_summary(list_of_steps, list_of_explored,list_of_time)



if __name__ == '__main__':
    driver()
