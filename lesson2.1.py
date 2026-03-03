# MageHero
# mage_hero

# родительский/Супер класс
# class Hero:
#     # конструктор класса
#     def __init__(self, name, level=0, hp=10, power=25):
#         # атрибуты класса
#         self.name = name
#         self.level = level
#         self.hp = hp
#         self.power = power
#     # метод класса
#     def action(self):
#         print(f"{self.name} base action!!")
#     def power1(self):
#         if self.power == 0:
#             return f"ваш персонаж исчерпал силу. текущая сила: {self.power}"
#         elif self.power >= 0:
#             self.power -= 1
#             return f"ваш персонаж применил силу -1 к силе. текущий сила: {self.power}"
#         else:
#             print(f"ваш персонаж немощь. возобновите силу")
#             print(f"текущая сила: {self.power}")
#     # принт
#     def __str__(self):
#         return self.name
#
# # экземпляр/объктом на основе класса
# kirito = Hero('Kirito')
# asuna = Hero('Asuno')
#
# # дочерный класс
# class MageHero(Hero):
#
#     def __init__(self, name, level, hp, mp):
#         super().__init__(name, level, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return f"{self.mp} cass spell {self.name}"
#
#     def action(self):
#         return f"HP: "
#
# gendalf = MageHero('Gendalf')
# print(asuna.power1)


# class Fly:
#     def action(self):
#         print("Fly")
#
# class Swim:
#     def action(self):
#         print("Swim")
#
# class Animal(Swim, Fly):
#     ...
#
# duck = Animal()
#
# duck.action()

class A:
    def action(self):
        print('A')

class B(A):
    def action(self):
        super().action()
        print('B')

class C(A):
    def action(self):
        super().action()
        print('C')

class D(B, C):
    def action(self):
        super().action()
        print('D')
d = D()
d.action()
# A
# C
# B
# D

TEST = 11