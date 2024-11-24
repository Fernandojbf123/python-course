import random
from choices import choices

class Player():
    def __init__(self):
        self.choiceNumber = None
        self.choiceText   = None
        self.isChoiceOk   = False
        
    def MakeChoice(self):
        self.choiceNumber = None
        self.choiceText   = None
        self.isChoiceOk   = False
        
        while self.isChoiceOk == False:
            self.choiceNumber = input("\n Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
            if self.choiceNumber == "1" or self.choiceNumber == "2" or self.choiceNumber == "3":
                self.isChoiceOk = True
                self.choiceNumber = int(self.choiceNumber)
                self.ChoiceNumberToText()
                print(f"You picked {self.choiceText}")
                return self.choiceText                
            else:
                print("You must pick an opcion 1 = ROCK 2 = PAPER or 3 = SCICSSORS")

    def ComputerPick(self):
        self.choiceNumber = random.randint(1, 3)
        self.ChoiceNumberToText()
        print(f"Computer picked {self.choiceText}")
        return self.choiceText

    def ChoiceNumberToText(self):
        self.choiceText = choices[str(self.choiceNumber)]
        
        