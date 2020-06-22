#comment
'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date:  February 06, 2018

Assignment 1

build something to represent n-puzzles. It will be derived from class Board.

methods to include:
    creates a random n-size puzzle unless a force_state list is given:
        TileBoard(n, force_state=None)
    Turns the list of TileBoard into a Tuples type:
        state_tuples()
    returns a list of moves are available:
        get_actions()
    Move the blank space in the n-size puzzle:
        move(offset)
    Check rather the n-size puzzle is solved, the goal state:
        solved()
'''


#from board import board
from board import Board
import random   #used for shuffling the list randomly
import math     #used for checking if something is square with square root function.
from re import MULTILINE
import copy


class TileBoard(Board):
    def __init__(self,n,force_state=None):
        self.n=n
        self.force_state=force_state
        # check if the size is a square number to build a n by n square
        if(math.sqrt(self.n+1).is_integer()):     #Will not work on large numbers
            rols_and_cols = int(math.sqrt(self.n+1))
            Board.__init__(self,rols_and_cols,rols_and_cols)
        else:
            print('Invalid number enter. Example 8 implies 3 by 3 or 15 implies 4 by 4. Try again: ')
        #will fill the board with the list given
        if(self.force_state is not None):   
            if(len(self.force_state) == self.n+1):
                self.fill_it_in(self.force_state)
                return
            else:
                print('error not correct list size')
                return
        self.new_list = self.random_list()
        self.fill_it_in(self.new_list)
    
    def solvable(self,list):
        self.total_sum = 0
        self.list_name = list
        #for x in list_name:
        for x in range (0,self.n+1):
            #prevent from comparing a None value with a int
            if self.list_name[x] is None :      
                continue
            for y in range(x+1,self.n+1):
                #case: preventing from comparing None value with int
                if self.list_name[y]is None :    
                    continue
                elif self.list_name[y] < self.list_name[x]:
                    self.total_sum = self.total_sum + self.list_name[y]
        if(self.total_sum%2==0):
            #print('solveable: ',self.total_sum)
            return True
        return False

    #generate random list using the size that was passed in
    def random_list(self):
        self.list_random = None
        if self.list_random is None:
            self.list_random=[]
        #can also use range(self.n+1) to generate [0,1,2,3,...,self.n+1]
        for x in range (0,self.n):      #doesn't need self.n+1 because None is added last
            self.list_random.append(x+1)
        self.list_random.append(None)
        random.shuffle(self.list_random)
        #check if this list can be solved
        if(not self.solvable(self.list_random)):    
            #if not then recursively call it until we get one that is solvable    
            self.random_list()          
        return self.list_random
    
    #pass in a list and it will fill in the board
    def fill_it_in(self,list):
        self.list=list
        self.row_a = 0;
        self.col_a = 0;
        # fills in the board using the random list
        for x in self.list:
            # when it reaches the size of the column reset.
            if(self.col_a == self.get_cols()):      
                self.col_a = 0
                self.row_a += 1
            self.place(self.row_a,self.col_a,x)
            self.col_a +=1
            
    #turn the board into a list
    def make_it_into_a_list(self):
        self.list=[]
        self.col_a=0
        self.row_a=0
        for x in range (0,self.n+1):      #turning board into a list
            if(self.col_a == self.get_cols()):      # when it reaches the size of the column reset.
                self.col_a = 0
                self.row_a += 1
            self.list.append(self.get(self.row_a,self.col_a))
            self.col_a +=1
        return self.list
    
    #looks for the None and returns row and column of that position   
    def search_for_none(self):
        self.none_found = []
        self.col_a = 0
        self.row_a = 0
        for x in range (0,self.n+1):
            if( self.col_a == self.get_cols()):
                self.col_a = 0
                self.row_a +=1
            if(self.get(self.row_a,self.col_a) is None):
                self.none_found=[self.row_a,self.col_a]
            self.col_a += 1
        return self.none_found
    
    # check if two tile boards are the same. used to overload the equality operator        
    #comment: Not sure if I was suppose to make this or not.
    '''
    def Operator(self,other_obj):
        def __eq__(self,other_obj):
            if not isinstance(self,other_obj.__class__):
                return False
            return self.__dict__ == other_obj.__dict__
    '''        
    
    #flatten the list of list representation of the board
    def state_tuple(self):
        return tuple(self.make_it_into_a_list())
    
    #return list of possible moves
    def get_actions(self):
        self.location_of_zero=self.search_for_none()
        self.direction_up = [-1,0]
        self.direction_down = [1,0]
        self.direction_left = [0,-1]
        self.direction_right = [0,1]
        self.possible_action_list=[]
        #is there a up direction
        self.list_up = [(x + y) for x, y in zip(self.location_of_zero, self.direction_up)]
        self.list_down = [(x + y) for x, y in zip(self.location_of_zero, self.direction_down)]
        self.list_left = [(x + y) for x, y in zip(self.location_of_zero, self.direction_left)]
        self.list_right = [(x + y) for x, y in zip(self.location_of_zero, self.direction_right)]
        if(self.list_up[0]>-1):
            self.possible_action_list.append(self.direction_up)
        if(self.list_down[0]<self.get_rows()):
            self.possible_action_list.append(self.direction_down)
        if(self.list_left[1] > -1 ):
            self.possible_action_list.append(self.direction_left)
        if(self.list_right[1] < self.get_cols()):
            self.possible_action_list.append(self.direction_right)
        return self.possible_action_list
    
    #given a valid action of the rom, return a new tileboard
    def move(self,offset):
        newboard = copy.deepcopy(self)
        #store the blank list value [x,x]
        self.none = newboard.search_for_none()
        #send in a number to locate the index of the list   
        self.list = self.get_actions()    
        #This is where the blank will move to. The next step is to store the value there to another spot
        self.value_location = [(x + y) for x, y in zip(self.none, self.list[int(offset)])]
        #get(row,col) row is on the left side and column is on the right side
        self.row = self.value_location[0]
        self.col = self.value_location[1]
        self.store_value=self.get(self.row,self.col)
        #move blank spot to new location
        newboard.place(self.row,self.col,None)
        #move value to where blank spot was
        newboard.place(self.none[0],self.none[1],self.store_value)
        #tileboard
        return newboard
        
 #   def find_out_the_direction
    
    #return true if puzzle is in a goal state
    #Known problems: if there are more than one None will still return true if it is in order. No special case is taking care of this.
    def solved(self):        
        self.right_number =1
        self.list=self.make_it_into_a_list()
        if(self.get_rows()%2 == 0): #even rows
            for item in self.list:
                if(item == self.right_number):
                    self.right_number +=1
                    continue
                elif (item is None):
                    continue
                else:
                    return False
        else:       #odd rows
            for y in self.list:
                if(y == self.right_number):
                    self.right_number += 1
                    continue
                elif (y == self.get(int(self.get_rows()/2),int(self.get_rows()/2))): # this is the middle should be None
                    continue
                else:
                    return False
        return True

    
#    something.move()
#    new_list = something.random_list()
#    something.fill_it_in(new_list)
#    something = TileBoard(size,[1,2,3,4,None,5,6,7,8])
#    something = TileBoard(24, [1,2,3,4,5,6,7,8,9,10,11,12,None,13,14,15,16,17,18,19,20,21,22,23,24])
#    something = TileBoard(15,[1,2,3,None,4,5,6,7,8,9,10,11,12,13,14,15])
#    something = TileBoard(size,[None,8,6,5,4,7,2,3,1])

#    while not solved:
#        print(something)
#    print('None: ',something.search_for_none())
#    print(something.get_actions())

#    print(something.solve())

#    print(something.make_it_into_a_list())
#    print(something.state_tuple())
#    print(something)
     
#sources used:
'''
Assignment 01 sheet by Dr. Marie A. Roch
Used what was shown in class as an outline for my driver.
(video)Python Programming: https://www.youtube.com/watch?v=N4mEzFDjqtA
(video)Basic Python tutorial class: https://www.youtube.com/watch?v=H5KyLqBRNQc
How to check if list contains None: https://stackoverflow.com/questions/28836378/check-if-any-item-in-python-list-is-none-but-include-zero
How to print strings and numbers: https://stackoverflow.com/questions/12018992/print-combining-strings-and-numbers
How to square root: https://stackoverflow.com/questions/9595135/how-to-calc-square-root-in-python
How to check if something is a square root: https://stackoverflow.com/questions/44531084/python-check-if-a-number-is-a-square
How to randomized a list: https://stackoverflow.com/questions/1022141/best-way-to-randomize-a-list-of-strings-in-python 
How to !variable: https://stackoverflow.com/questions/17168046/python-how-to-negate-value-if-true-return-false-if-false-return-true
(video)How to create a function in python: https://www.youtube.com/watch?v=1wkBXYRKZSA
(book)How to empty a list: Python in a Nutshell page 80
(book)How key-word or paramters works: Python in a Nutshell page 81
How to find a None in a list: https://stackoverflow.com/questions/288.3.78/check-if-any-item-in-python-list-is-none-but-include-zero
How to resolve problems with importing: https://stackoverflow.com/questions/4631377/unresolved-import-issues-with-pydev-and-eclipse
How to turn a float into an integer: https://stackoverflow.com/questions/3387655/safest-way-to-convert-float-to-integer-in-python
How to increment a variable: https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
How to check if a variable is not None: https://stackoverflow.com/questions/3965104/not-none-test-in-python
How to add two list together: http://www.dreamincode.net/forums/topic/214465-add-two-lists/
How to overload: https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
How to use __eq__(): http://jcalderone.livejournal.com/32837.html
How to code overload using __eq__: https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
How to get an input from user: https://stackoverflow.com/questions/3345202/getting-user-input
How to use chr and ord: https://www.dotnetperls.com/ord-python
How to find the index of a given item: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
''' 