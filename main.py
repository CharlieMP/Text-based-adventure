from cave import Cave

cavern = Cave("cavern")
cavern.set_description("A dank and dirty cave")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
grotto = Cave("grotto")
grotto.set_description("A samll cave with ancient graffiti")
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")
dungeon.get_details()