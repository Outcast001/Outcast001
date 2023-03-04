class PlayChoice():
    def __init__(self) -> None:
        self.playChoice = int(input("Escolha uma casa entre 1 e 9: "))
    
    def userChoice(self):
        return self.playChoice