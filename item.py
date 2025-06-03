class Item():
    def __init__(self, name):
        self.name = name
        self.description = None

    def describe(self):
        print("There is a " + self.name + " lying on the floor")
        print(self.description)

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name