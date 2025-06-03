class Cave:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name
    
    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item
    
    def get_item(self):
        return self.item

    def get_character(self):
        return self.character

    def describe(self):
        print(self.description)

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self