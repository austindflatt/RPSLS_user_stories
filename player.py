from human import Human

class Player(Human):
    def __init__(self):
        super().__init__()
        self.name = input('Enter name')
        self.move = ''
    choice = ['rock', 'paper', 'scissors', 'lizard', 'spock']
