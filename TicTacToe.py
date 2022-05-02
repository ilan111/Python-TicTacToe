"""
Author: Ilan Yadgarov
15/10/2021
"""

import random
import math

class TicTacToe:

    gameboard_values = [' ' for x in range(9)]

    scores = {'X': 10, 'O': -10, 'tie': 0}

    def print_gameboard(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.gameboard_values[0], self.gameboard_values[1], self.gameboard_values[2]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.gameboard_values[3], self.gameboard_values[4], self.gameboard_values[5]))
        print('\t_____|_____|_____')
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.gameboard_values[6], self.gameboard_values[7], self.gameboard_values[8]))
        print("\t     |     |")
        print("\n")

    def take_input(self, sign):
        while True:
            try:
                position_input = int(input("Choose where to place the "+sign+" (1-9): "))
            except ValueError:
                print("You are allowed entering a single digit only (1-9)")
                continue
            if position_input < 1 or position_input > 9:
                print("Wrong choice... please try again")
                continue
            else:
                break
        return position_input


    def is_position_taken(self,position_index):
        if self.gameboard_values[position_index-1] == 'X' or self.gameboard_values[position_index-1] == 'O':
            return True
        else:
            return False

    def is_gameboard_full(self):
        if ' ' in self.gameboard_values:
            return False
        return True

    def x_player_turn(self):
        players_input = self.take_input('X')
        while True:
            is_taken = self.is_position_taken(players_input)
            if (is_taken):
                print("Position is already taken, try once again")
                players_input = self.take_input('X')
                continue
            else:
                self.gameboard_values[players_input-1] = 'X'
                break
        # print(self.gameboard_values)
        self.print_gameboard()

    def o_player_turn(self):
        players_input = self.take_input('O')
        while True:
            is_taken = self.is_position_taken(players_input)
            if (is_taken):
                print("Position is already taken, try once again")
                players_input = self.take_input('O')
                continue
            else:
                self.gameboard_values[players_input-1] = 'O'
                break
        # print(self.gameboard_values)
        self.print_gameboard()

    def bot_player_turn_random(self, sign):
        empty_indexes = []
        for i in range(len(self.gameboard_values)):
            if self.gameboard_values[i] == ' ':
                empty_indexes.append(i)
        players_input = random.choice(empty_indexes)
        self.gameboard_values[players_input] = sign
        self.print_gameboard()

    def check_winner(self):
        winner = None

        if(self.gameboard_values[0]==self.gameboard_values[1] and self.gameboard_values[1]==self.gameboard_values[2] and self.gameboard_values[0]!=' '):
            winner = self.gameboard_values[0]
        if(self.gameboard_values[3]==self.gameboard_values[4] and self.gameboard_values[4] == self.gameboard_values[5] and self.gameboard_values[3]!=' '):
            winner = self.gameboard_values[3]
        if(self.gameboard_values[6]==self.gameboard_values[7] and self.gameboard_values[7]==self.gameboard_values[8] and self.gameboard_values[6]!= ' '):
            winner = self.gameboard_values[6]
        if(self.gameboard_values[0]==self.gameboard_values[3] and self.gameboard_values[3]==self.gameboard_values[6] and self.gameboard_values[0]!=' '):
            winner = self.gameboard_values[0]
        if(self.gameboard_values[1]==self.gameboard_values[4] and self.gameboard_values[4]==self.gameboard_values[7] and self.gameboard_values[1]!=' '):
            winner = self.gameboard_values[1]
        if(self.gameboard_values[2]==self.gameboard_values[5] and self.gameboard_values[5]==self.gameboard_values[8] and self.gameboard_values[2]!=' '):
            winner = self.gameboard_values[2]
        if(self.gameboard_values[0]==self.gameboard_values[4] and self.gameboard_values[4]==self.gameboard_values[8] and self.gameboard_values[0]!=' '):
            winner = self.gameboard_values[0]
        if(self.gameboard_values[2]==self.gameboard_values[4] and self.gameboard_values[4]==self.gameboard_values[6] and self.gameboard_values[2]!=' '):
            winner = self.gameboard_values[2]

        if (winner == None and self.is_gameboard_full()):
            return 'tie'
        else:
            return winner

    def minimax(self, board, depth, isMaximazing):
        result = self.check_winner()
        if(result != None):
            return self.scores[result]

        if(isMaximazing):
            bestScore = -math.inf
            for spot in range(len(board)):
                if self.gameboard_values[spot] == ' ':
                    board[spot] = 'X'
                    score = self.minimax(board, depth+1, False)
                    board[spot] = ' '
                    bestScore = max(score, bestScore)
            return bestScore

        else:
            bestScore = math.inf
            for spot in range (len(board)):
                if self.gameboard_values[spot] == ' ':
                    board[spot] = 'O'
                    score = self.minimax(board, depth + 1, True)
                    board[spot] = ' '
                    bestScore = min(score, bestScore)
            return bestScore

    def best_move(self, sign):
        bestScore = -math.inf
        move = math.inf
        for spot in range (len(self.gameboard_values)):
            if self.gameboard_values[spot] == ' ':
                self.gameboard_values[spot] = sign
                score = self.minimax(self.gameboard_values, 0, False)
                self.gameboard_values[spot]=' '
                if(score > bestScore):
                    bestScore = score
                    move = spot
        self.gameboard_values[move] = sign
        self.print_gameboard()

    def player_vs_player_game(self):
        self.print_gameboard()
        while True:
            self.x_player_turn()
            if (self.check_winner() == 'X'):
                print("X WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break

            self.o_player_turn()
            if (self.check_winner() == 'O'):
                print("O WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break

    def player_vs_bot_game_random(self):
        self.print_gameboard()
        while True:
            print("Bot's move:")
            self.bot_player_turn_random('X')
            if (self.check_winner() == 'X'):
                print("X WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break

            print("Your turn:")
            self.o_player_turn()
            if (self.check_winner() == 'O'):
                print("O WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break


    def player_vs_bot_game_ai(self):
        self.print_gameboard()
        while True:
            print("Bot's move:")
            self.best_move('X')
            if (self.check_winner()=='X'):
                print("X WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break

            print("Your turn:")
            self.o_player_turn()
            if (self.check_winner()=='O'):
                print("O WINS!")
                break
            if (self.check_winner() == 'tie'):
                print("Draw!")
                break

    def start_game(self):
        while(True):
            selection=''
            print("Welcome to X/O Game!\n")
            print("Please choose a game:")
            print("For PVP type 1")
            print("For Player vs Bot (Random choices) type 2")
            print("For player vs Bot (AI) type 3")
            print("To exit type 0\n")
            answer = input("Type and enter here -> ")
            if(answer == '1'):
                self.player_vs_player_game()
            if(answer == '2'):
                self.player_vs_bot_game_random()
            if(answer == '3'):
                self.player_vs_bot_game_ai()
            self.gameboard_values = [' ' for x in range(9)]
            if(answer =='0'):
                break
            else:
                print("\nTry again...\n")

TicTacToe().start_game()