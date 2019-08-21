# Задание 1
# Я решил использовать классы из ООП что-бы упростить процесс
import random

class Enemy:
    def __init__(self):
        self.health = 100
        self.armor = 1.2
        self.damage = random.randint(20,40) # Случайное число урона
    def attack(self):
        print(self.health - (self.damage / self.armor)) # формула по которой вычесляется урон
    def checkhealth(self):
        print(self.health)

enemy1 = Enemy()

enemy1.attack()
enemy1.checkhealth()
