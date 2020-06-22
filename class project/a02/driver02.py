'''
driver for graph search problem
Created on Feb 10, 2018

@author: mroch
'''

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer

from npuzzle import NPuzzle
from basicsearch_lib02.tileboard import TileBoard
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
import collections
import time
import searchstrategies


def tic():
    "Return current time representation"
    return time.time()

def tock(t):
    "Return time elapsed in sec since t where t is the output of tic()"
    return time.time() - t
    
def driver() :

    raise NotImplemented

if __name__ == '__main__':
    driver()
