from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        print('Боец стреляет из оружия')
        pass

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


class Monster():
    def attack(self):
        pass


class Gan(Weapon):
    def attack(self):
        print('Боец стреляет из пистолета')

class Bow(Weapon):
    def attack(self):
        print('Боец делает выстрел из лука')

gan1 = Gan()
bow1 = Bow()
boy = Fighter(gan1)

for i in range(4):
    boy.change_weapon(bow1)
    boy.fight()
    boy.change_weapon(gan1)
    boy.fight()