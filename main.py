from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Fighter():
    def __init__(self, weapon):
        self.weapon = weapon

class Monster():
    def __init__(self, life):
        self.life = life
