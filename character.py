class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("" + self.name + " says: " + self.conversation)
        else:
            print(self.name + "doesnt want to talk to you")

    def fight(self, combat_item):
        print(self.name + "doesnt want to fight with you")
        return True
    
    def steal(self):
        print("You steal from" + self.name)
    

class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " swallows you, little wimp")
            return False
        

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def pat(self):
        print(self.name + " pats you back!")