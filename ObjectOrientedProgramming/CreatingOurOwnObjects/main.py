# OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Ryan', 26)
print(player1)  # <__main__.PlayerCharacter object at (random numbers)
print(player1.name)  # Ryan
print(player1.age)  # 26
print(player1.run())  # run
# done
