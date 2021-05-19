from human import Human
from player import Player
import random

class Computer(Human):
    def __init__(self):
        super().__init__()
        self.name = 'computer'
        self.move = ''
