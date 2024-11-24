
import sys
from player import Player
from playerComputer import PlayerComputer
from Strategy.strategyRPSOne import StrategyRPSOne
from Strategy.contextRPS import ContextRPS
from clearTerminal import clear_terminal

class RockPaperScissors():
    def __init__(self):
        # Player
        self.playerOneChoice = None
        self.playerOnePicks = []
        self.playerOne = Player()
        
        # Computer
        self.playerTwoChoice = None
        self.playerTwoPicks = []
        self.playerTwo = Player()

        # Score
        self.gameNumber = 1
        self.numberOfGames = 10
        self.winner = None
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.ties = 0

        print("WELCOME TO SUPER ROCK PAPER SCISSORS")
        print("\n")
        self.SetNumberOfGames()

    def render(self):
        while self.gameNumber <= self.numberOfGames+1:
            # Print scores
            self.PrintScore()

            self.playerOneChoice = self.playerOne.MakeChoice()
            self.playerOnePicks.insert(0,self.playerOne.choiceText) # Store history

            self.playerTwoChoice = self.playerTwo.ComputerPick()
            self.playerTwoPicks.insert(0,self.playerTwo.choiceText) # Store history

            #Call the strategy of the game to pick the winner
            self.strategy   = StrategyRPSOne()
            self.ctx        = ContextRPS(self.strategy)
            self.winner     = self.ctx.GetWinner(self.playerOneChoice,self.playerTwoChoice)

            #Add one (01) point to winner
            self.AddScore(self.winner)

            self.gameNumber += 1

            if self.gameNumber == self.numberOfGames+1:
                self.PrintScore()
                sys.exit()
            
        

    def SetNumberOfGames(self):
        isValid = False
        while isValid == False:
            userInput = input("Pick the number of rolls (integer number between 1 to 10)\n")
            try:
                num = int(userInput)
                isValid = True
                self.numberOfGames = num
            
            except ValueError:
                print("You must pick a valid integer number. \n")




    def AddScore(self,winner):
        if winner == 1:
            self.playerOneScore += 1
        elif winner == 2:
            self.playerTwoScore += 1
        else:
            self.ties += 1
    
    def PrintScore(self):
        print("*******SCORE BOARD*******")
        print(f"** Your score: {self.playerOneScore} **\n** Computers score: {self.playerTwoScore} **\n** Ties: {self.ties} **")
        print(f"******* BEST OF {self.numberOfGames} *******")
    
    

def Animate():
    game.render()
    # clear_terminal()
    Animate()

## Running the game!
clear_terminal()
game = RockPaperScissors()
Animate()