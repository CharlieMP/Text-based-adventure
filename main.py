from cave import Cave
from character import Enemy
from character import Friend
from item import Item

#creation of caverns
dead = False
cavern = Cave("cavern")
cavern.set_description("A dank and dirty cave")
dungeon1 = Cave("Dungeon chamber 1")
dungeon1.set_description("A large cave with bones strewn everywhere")
grotto = Cave("grotto")
grotto.set_description("A small cave with ancient graffiti")
startcave = Cave("Start cave")
startcave.set_description("You are in a small cave with a one way exit")
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

#linking all caverns according to diagram
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
wumpusLair.link_cave(dungeon3, "west")


#creation of items
vegemite = Item("Vegemite")
vegemite.set_description("A Wumpus' worst nightmare")
grotto.set_item(vegemite)

bone = Item("Bone")
bone.set_description("A worryingly large femur bone, probably useless")
dungeon2.set_item(bone)

torch = Item("Torch")
torch.set_description("A torch to light your way")
dungeon1.set_item(torch)

jokebook = Item("Jokebook")
jokebook.set_description("A book full of bad skeleton puns")
puddle.set_item(jokebook)

mushroom = Item("Mushroom")
mushroom.set_description("A mushroom with white spots")
mushroomTunnel.set_item(mushroom)

rock = Item("Rock")
rock.set_description("A smooth round rock, perfect for squashing someone")
cavern.set_item(rock)

#bag list to store items
bag = []

#creation of enemies
harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("What, who are you? get out of my lair!")
harry.set_weakness("vegemite")
wumpusLair.set_character(harry)

skelebones = Enemy("Skelebones", "A skeleton wearing a red cape with shoulder pads")
skelebones.set_conversation("OH MY GOD IS THAT A HUMAN?")
skelebones.set_weakness("jokebook")
dungeon1.set_character(skelebones)

jushroom = Friend("Weird ass Jushroom", "A weird little mushroom guy")
jushroom.set_conversation("dont listen to the mustard sprouts, i've heard that they're irradiated")
mushroomTunnel.set_character(jushroom)

mark = Enemy("Mark", "An incredibly small leprechaun")
mark.set_conversation("Please dont squash me, im very frail")
mark.set_weakness("rock")
sump.set_character(mark)

drake = Enemy("Cave Drake", "A smooth scaled drake with large eyes that are sensetive to light")
drake.set_conversation("You can't see me but i can see you!")
drake.set_weakness("torch")
dungeon3.set_character(drake)

john = Enemy("John enemy", "An enemy named John")
john.set_conversation("Oh this? its just a rash I got from my mushroom allergy")
john.set_weakness("mushroom")
dungeon2.set_character(john)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

#beginning of mainline
current_cave = startcave
#plays while variable 'dead' equals false
while dead == False:
    #describes everything in the current cave
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
    #checks for different commands
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
        #checks if there is a character in the cave
        if inhabitant is not None:
            #checks if the character is an enemy or not
            if isinstance(inhabitant, Enemy):
                print("What will you fight with?")
                fight_with = input().lower()
                #checks if the item chosen is in the player's bag
                if fight_with in bag:
                    #checks if the item selected is the enemy's weakness
                    if inhabitant.fight(fight_with) == True:
                        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
                        #checks if all enemies have bene defeated
                        if Enemy.enemies_to_defeat == 0:
                            print("Congratulations, you have survived another adventure!")
                            #sets variable 'dead' to true to end the gameplay loop
                            dead = True
                        else:
                            print("Bravo hero, you won the fight!")
                            current_cave.set_character(None)
                    else:
                        print("Scurry home, you lost the fight\nThats the end of the game")
                        dead = True                        
                else:
                    print("You dont have a " + fight_with)
            else:
                print("They dont want to fight you")
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            #adds item in current cave to bag and removes it from the current cave
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name().lower())
            current_cave.set_item(None)
        else:
            print("Theres nothing here to take")
    else:
        #else move the character in the direction that they choose
        current_cave = current_cave.move(command)