from Strategy.strategyRPS import StrategyRPS

class ContextRPS():
    def __init__(self,strategy: StrategyRPS):
        self.strategy = strategy

    def SetStrategy(self, strategy: StrategyRPS):
        self.strategy = strategy

    def GetWinner(self, playerOneChoice, playerTwoChoice):
        return self.strategy.PickWinner(playerOneChoice, playerTwoChoice)