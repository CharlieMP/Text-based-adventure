from cave import Cave
from character import Enemy
from character import Friend
from item import Item

dead = False
cavern = Cave("cavern")
cavern.set_description("A dank and dirty cave")
dungeon1 = Cave("Dungeon chamber 1")
dungeon1.set_description("A large cave with a rack")
grotto = Cave("grotto")
grotto.set_description("A small cave with ancient graffiti")
startcave = Cave("Start cave")
startcave.set_description("You are in a small cave with one exit")
mossyTunnel = Cave("mossy tunnel")
mossyTunnel.set_description("A tunnel lined with a variety of different mosses")
smallCliff = Cave("small cliff")
smallCliff.set_description("A small east facing cliff")
puddle = Cave("puddle")
puddle.set_description("A muddy pit at the bottom of the cliff")
mushroomTunnel = Cave("mushroom tunnel")
mushroomTunnel.set_description("A long tunnel filled with mushrooms")
crossroads = Cave("crossroads")
crossroads.set_description("A tunnel that splits into two directions")
dungeon2 = Cave("Dungeon chamber 2")
dungeon2.set_description("A smooth stoned room with dart traps")
crystalCavern = Cave("crystal cavern")
crystalCavern.set_description("A large cave with crystals protruding from the walls and ceiling")
tallCliff = Cave("tall cliff")
tallCliff.set_description("A tall cliff that overlooks a sump")
sump = Cave("sump")
sump.set_description("A small cave that collects water")
bridge = Cave("bridge")
bridge.set_description("A rickety bridge just above the crossroads")
dungeon3 = Cave("Dungeon chamber 3")
dungeon3.set_description("A long room with hair all over the floor")
wumpusLair = Cave("Wumpus lair")
wumpusLair.set_description("The lair of the mighty Wumpus!")

startcave.link_cave(cavern, "north")
cavern.link_cave(mossyTunnel, "west")
cavern.link_cave(smallCliff, "east")
cavern.link_cave(crossroads, "north")
smallCliff.link_cave(cavern, "west")
smallCliff.link_cave(dungeon1, "north")
smallCliff.link_cave(puddle, "east")
puddle.link_cave(mushroomTunnel, "north")
mushroomTunnel.link_cave(puddle, "south")
mushroomTunnel.link_cave(dungeon1, "west")
dungeon1.link_cave(mushroomTunnel, "east")
dungeon1.link_cave(smallCliff, "south")
dungeon1.link_cave(crossroads, "west")
crossroads.link_cave(dungeon1, "east")
crossroads.link_cave(cavern, "south")
crossroads.link_cave(dungeon2, "west")
mossyTunnel.link_cave(cavern, "east")
mossyTunnel.link_cave(dungeon2, "north")
dungeon2.link_cave(crossroads, "east")
dungeon2.link_cave(mossyTunnel, "south")
dungeon2.link_cave(crystalCavern, "west")
crystalCavern.link_cave(grotto, "south")
crystalCavern.link_cave(dungeon2, "east")
crystalCavern.link_cave(tallCliff, "north")
grotto.link_cave(crystalCavern, "north")
tallCliff.link_cave(crystalCavern, "south")
tallCliff.link_cave(sump, "east")
sump.link_cave(dungeon2, "south")
sump.link_cave(bridge, "east")
bridge.link_cave(sump, "west")
bridge.link_cave(crossroads, "south")
bridge.link_cave(dungeon3, "east")
dungeon3.link_cave(bridge, "west")
dungeon3.link_cave(wumpusLair, "east")


vegemite = Item("Vegemite")
vegemite.set_description("A Wumpus' worst nightmare")
grotto.set_item(vegemite)

bone = Item("Bone")
bone.set_description("A worryingly large femur bone")
dungeon2.set_item(bone)

torch = Item("Torch")
torch.set_description("A torch to light your way")
dungeon1.set_item(torch)

rock = Item("Rock")
rock.set_description("A smooth round rock")
cavern.set_item(rock)

bag = []

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("What, who are you? get out of my lair!")
harry.set_weakness("vegemite")
wumpusLair.set_character(harry)


josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)


current_cave = startcave
while dead == False:
    print("\n")
    current_cave.describe()
    current_cave.get_details()
    item = current_cave.get_item()
    inhabitant = current_cave.get_character()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat")
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                print("Bravo hero, you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight\nThats the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)
    else:
        current_cave = current_cave.move(command)