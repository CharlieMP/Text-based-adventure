from character import Enemy

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Come closer. I cant see you!")
harry.describe()
harry.talk()
harry.set_weakness("vegemite")
print("what will you fight with?")
fight_with = input()
harry.fight(fight_with)