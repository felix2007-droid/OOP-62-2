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
print(Kirito.name,
Kirito.lvl,
Kirito.hp,
Kirito.strength)

Kirito.greet()
Kirito.attack()
Kirito.rest()

print(Kirito.name,
Kirito.lvl,
Kirito.hp,
Kirito.strength)

print(Asuna.name,
Asuna.lvl,
Asuna.hp,
Asuna.strength)

Asuna.greet()
Asuna.attack()
Asuna.rest()

print(Asuna.name,
Asuna.lvl,
Asuna.hp,
Asuna.strength)