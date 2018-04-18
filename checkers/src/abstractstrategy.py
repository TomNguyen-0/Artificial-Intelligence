'''
Created on Mar 1, 2015

@author: mroch
'''

import checkerboard

class Strategy:
    """"Abstract strategy for playing a two player game.
    Abstract class from which specific strategies should be derived
    """
        
    def __init__(self, player, game, maxplies):
        """"Initialize a strategy
        player is the player represented by this strategy
        game is a class or instance that supports the class or instance method
            game.other_player(player) which finds the name 
                of the other player
        maxplies is the maximum number of plies before a cutoff is applied
        """
        
        # Useful for initializing any constant values or structures
        # used to evaluate the utility of a board
        self.maxplayer = player#me
        self.minplayer = game.other_player(player)#other player
        self.maxplies = maxplies
        self.starting_holder=True
    
    def utility(self, board):
        "Return the utility of the specified board"
        #find the distance
        #find the number of pieces pawns and kings
        #eating moves
        #to improve ai you can add in edge as being a better move because they are safe
        on_the_board_pieces = self.how_many_pieces_on_the_board(board)#number of pieces on the board
        on_the_board_distance = self.how_far_is_everything(board)
        on_the_board_moves = self.the_winning_move(board)
        answer = on_the_board_pieces+on_the_board_distance+on_the_board_moves
        return answer
          
    
    def player_pieces(self,board):
        you=board.playeridx(self.minplayer)
        me=board.playeridx(self.maxplayer)
        my_pawns = board.get_pawnsN()[me]
        my_kings = board.get_kingsN()[me]
        your_pawns = board.get_pawnsN()[you]
        your_kings = board.get_kingsN()[you]
        return [[my_pawns,my_kings],[your_pawns,your_kings]]
        
    
    def how_many_pieces_on_the_board(self,board):
        piece = self.player_pieces(board)
        pawn_value = piece[0][0] - piece[1][0]#my_pawns - your_pawns
        king_value = piece[0][1] - piece[1][1]#my_kings - your_kings
        real_value = pawn_value + (2*king_value)#king is worth twice the pawn
        return real_value
    
    def how_far_is_everything(self,board):
        me=board.playeridx(self.maxplayer)#me = 0, you = 1
        distance=0
        for row,col,item in board:  #row = 0, col =1 , item =b
            identify_piece = board.identifypiece(item) 
            playeridx = identify_piece[0]# returns 1
            kingpred = identify_piece[1] #return True or False
            if not kingpred:#check to see if it is a king
                if playeridx is me:
                    distance = distance + board.disttoking(item,row)#my piece from the throne
                else:#the other player piece to the throne
                    distance = distance - board.disttoking(item,row)
        return distance
    
    def the_winning_move(self,board):
        if self.starting_holder:
            self.start = self.player_pieces(board)
            self.later = self.start
            self.starting_holder=False
        self.now = self.later
        self.later = self.player_pieces(board)
        my_score= (self.now[0][0]+self.now[0][1])-(self.later[0][0]+self.later[0][1])
        your_score = (self.now[1][0]+self.now[1][1])-(self.later[1][0]+self.later[1][1])
        if my_score > your_score:#I lost more pieces than you
            return -(my_score-your_score)#bad move
        else:#better move
            return my_score-your_score               

'''      
    def play(self, board):
        located in ai.
'''
