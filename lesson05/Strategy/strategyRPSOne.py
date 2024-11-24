from Strategy.strategyRPS import StrategyRPS


class StrategyRPSOne(StrategyRPS):

    def __init__(self):
        super().__init__() 

    def PickWinner(self,playerOneChoice,playerTwoChoice):
        print("\n")
        print("***")
        if (playerOneChoice == playerTwoChoice):
            print("It's a tie. :O ")
            print("*** \n")
            return 0
        elif (playerOneChoice == "ROCK" and playerTwoChoice == "SCISSORS") or \
           (playerOneChoice == "SCISSORS" and playerTwoChoice == "PAPER") or \
           (playerOneChoice == "PAPER" and playerTwoChoice == "ROCK"):
            print("You won! **CONGRATZ!!**")
            print("*** \n")
            return 1
        else:
            print("You lost! sorry :'( ")
            print("*** \n")
            return 2