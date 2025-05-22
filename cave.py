class Cave:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_caves = {}

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)