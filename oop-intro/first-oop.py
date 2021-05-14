from random import randint

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Player:
  def __init__(myself):
    myself.dice = []

  def roll(myself):
    myself.dice = [] # clears current dice
    for i in range(3):
      myself.dice.append(randint(1,6))

  def get_dice(myself):
    return myself.dice

player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print("Player 1 rolled" + str(player1.get_dice()))
print("Player 2 rolled" + str(player2.get_dice()))

if sum(player1.get_dice()) == sum(player2.get_dice()):
  print("Draw!")
elif sum(player1.get_dice()) > sum(player2.get_dice()):
  print("Player 1 wins!")
else:
  print("Player 2 wins!")

del player1
del player2

