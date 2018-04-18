
"""
ai - search & strategy module

implement a concrete Strategy class and AlphaBetaSearch
"""

import abstractstrategy
#alpha beta pruning: https://youtu.be/xBXHtz4Gbdo
#mit search: games, minimax, and alpha-beta: https://www.youtube.com/watch?v=STjW3eH0Cik
class Strategy(abstractstrategy.Strategy):
    "AI player"
    def play(self, board):
        """"play - Make a move
        Given a board, return (newboard, action) where newboard is
        the result of having applied action to board and action is
        determined via a game tree search (e.g. minimax with alpha-beta
        pruning).
        """
        self.board=board
        print(board)
        search = AlphaBetaSearch(board,self.maxplayer,self.minplayer)
        action = search.alphabeta(board)
        return (board.move(action), action)
        #raise NotImplementedError("Subclass must implement")
    
class AlphaBetaSearch:
    """AlphaBetaSearch Conduct alpha beta searches from a given state.
    Example usage:
    # Given an instance of a class derived from AbstractStrategy, set up class
    # to determine next move, maximizing utility with respect to red player 
    # and minimiizing with respect to black player.  Search 3 plies.
    search = AlphaBetaSearch(strategy, 'r', 'b', 3)
    # To find the move, run the alphabetamethod
    best_move = search.alphabeta(some_checker_board)
    """
    def __init__(self,strategy, maxplayer, minplayer, maxplies=3, verbose=False):
        self.strategy = strategy
        self.me = maxplayer
        self.you = minplayer
        self.maxplies = maxplies
        self.verbose = verbose#not using
        self.depth =0
        self.alpha = -float('inf')
        self.beta = float('inf')
        self.move = None
    
    """"
    AlphaBetaSearch 
    - Initialize a class capable of alphabeta search strategy 
    - implementation of AbstractStrategy class maxplayer 
    - name of player that will maximize the utility function minplayer 
    - name of player that will minimize the utility function maxplies
    - Maximum ply depth to search verbose 
    - Output debugging information

    alphbeta (state) 
    - Run an alphabeta search from the current state.  Returns maximizer action.
    """ 
    
    def alphabeta(self,state):
        self.depth=0
        score = self.maximizer(state=state, alpha = self.alpha,beta=self.beta)
        actions = state.get_actions(self.me)
        why=Strategy(player=self.me,game=state,maxplies=self.maxplies)
        for moves in actions:
            if self.move == moves:
                return moves
       
    def maximizer(self,state, alpha, beta):#alpha - maximizer, maximize my points
        return_value= [None,None]
        counter =0
        did_i_go_left=False
        stop = state.is_terminal()#stop= (False, None)
        value = self.alpha#-inf
        why = Strategy(player = self.me, game=state,maxplies=self.maxplies)
        if stop[0]:#the game is over or no more moves
            return why.utility(state)#pass back the value
        else:
            action_list = state.get_actions(self.me)#action = [[(2,1),(3,0)],[(a,b),(a,b)]]
            if self.depth > self.maxplies:#this is the depth that we want to stop at
                self.depth-=1#about to return so reduce the depth level to 3
                return why.utility(state)#return value
            self.depth += 1 # depth=1 then depth=3
            for action in action_list:
                go_left = self.minimizer(state=state.move(action), alpha=alpha, beta=beta)    
                if counter ==0:
                    return_value[0] = go_left
                else:
                    return_value[1] = go_left
                counter +=1
                if counter >=2:
                    return_value[0] = max(return_value[0],return_value[1])
                if go_left >= beta:
                    return go_left
                elif go_left > value: #max(go_left,value)
                    value = go_left
                    alpha = max (alpha, value)
                    self.move = action
        return return_value[0]
    
    def minimizer(self, state, alpha, beta):#beta minimizer, minimize enemy points
        value = self.beta#inf
        did_i_go_left=False
        counter =0
        return_value= [None,None]
        stop = state.is_terminal()#black ai wins with 7 p 1 king. Red wins with 1 k 6 p
        why = Strategy(player = self.me, game=state,maxplies=self.maxplies)#ai against itself red wins with 9 p 3kings
        if stop[0]:#stop return value game or no available move
            return why.utility(state)
        else:
            action_list = state.get_actions(self.you)#get a list of actions
            for action in action_list:#moving through the possible moves
                if self.depth > self.maxplies:
                    self.depth-=1
                    return why.utility(state)
                self.depth+=1
                go_left = self.maximizer(state=state.move(action), alpha=alpha, beta=beta)
                if counter ==0:
                    return_value[0] = go_left
                else:
                    return_value[1] = go_left
                counter +=1
                if counter >=2:
                    return_value[0] = min(return_value[0],return_value[1])
                if go_left <= alpha:
                    return alpha
                elif go_left < value: 
                    value = go_left
                    beta  = min (beta, value)
                

        return return_value[0]#util-value_for_minimizer = 4

