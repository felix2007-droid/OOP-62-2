import random
class Hero():
    def __init__(self, name='Bob', lvl=0, hp=10, strength=25):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.lvl}"

    def attack(self):
        if self.strength <= 0:
            return f"сила героя исчерпана. невозможно провести атаку."
        else:
            self.strength -= 1
            return f"{self.name} наносит удар!"

    def rest(self):
        self.hp += 1
        return f"{self.name} отдыхает…; +1 к здоровью"

Asuna = Hero('Asuno', 10, 100, 200)
Kirito = Hero('Kirito', 12, 120, 240)

class Warrior(Hero):
    def __init__(self, name='Bob', lvl=0, hp=10, strength=25, stamina=35):
        super().__init__(name, lvl, hp, strength)
        self.stamina = stamina

    def attack(self):
        if self.strength - 2 < 0 or self.stamina - 2 < 0:
            return f"Недостаточно силы или выносливости. невозможно провести атаку."
        else:
            self.strength -= 2
            self.stamina -= 2
            return f"Воин {self.name} атакует мечом! -2 к силе и выносливости"
class Mage(Hero):
    def __init__(self, name='Bob', lvl=0, hp=10, strength=25, mana=25):
        super().__init__(name, lvl, hp, strength)
        self.mana = mana

    def attack(self):
        if self.mana - 5 < 0:
            return f"Маг исчерпал свой запас маны. невозможно коставать заклинание."
        else:
            self.mana -= 5
            return f"Маг по имени {self.name} кастует мощное заклинание!!! -5 к мане"
class Assassin(Hero):
    def __init__(self, name='Bob', lvl=0, hp=10, strength=25, stealth=20):
        super().__init__(name, lvl, hp, strength)
        self.stealth = stealth

    def attack(self):
        if self.strength <= 0 or self.stealth - 3 < 0:
            return f"Ассасин теряет скрытость и силу. атака теряет свою элемент неожидонасти."
        else:
            self.strength -= 1
            self.stealth -= 3
            return f"Ассасин по имени {self.name} атакует из-под тишка!!! -3 к скрытость и -1 к силе"

Guts = Warrior("Guts", 122, 233, 312, 432)
Poter = Mage('Poter', 111, 95, 67, 512)
Jin_Woo = Assassin('Jin_Woo', 192, 145, 342, 455)

print(Jin_Woo.stealth)
print(Jin_Woo.attack())
print(Jin_Woo.stealth)
print(Guts.attack())
print(Guts.greet())
print(Poter.hp)
print(Poter.rest())
print(Poter.hp)
while True:
    rand1 = random.choice(['Warrior', 'Mage', 'Assassin'])
    input1 = input('выберите героя! Warrior, Mage или Assassin. введите в терминал нужный вам герой'
            ' или нажмите пробел чтобы завершить праграмму: ').lower()
    if rand1 == 'Warrior' and input1 == 'warrior' or rand1 == 'Mage' and input1 == 'mage' or rand1 == 'Assassin' and input1 == 'assassin':
        print(f'Ничья!!! оба класса {rand1} победителя нет!')
    elif rand1 == 'Warrior' and input1 == 'assassin' or rand1 == 'Mage' and input1 == 'warrior' or rand1 == 'Assassin' and input1 == 'Mage':
        print(f'порожение!!! ваш противник {rand1} победил вашего {input1}')
    elif rand1 == 'Warrior' and input1 == 'mage' or rand1 == 'Mage' and input1 == 'assassin' or rand1 == 'Assassin' and input1 == 'warrior':
        print(f'Победа!!! ваш {input1} победил {rand1} противника')
    else:
        print("вы прекратили игру")
        break