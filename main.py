class MapTile:
    """ This Map uses x and y coordinates to print out location"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location(self):
        print("your current location is ", self.x, self.y)


def start():
    class firstTile(MapTile):
        print("You are the start. enter direction to go")
        Tile = MapTile(0, 1)
        Tile.location()
        direction = input("Where do you want to go: ")
        if direction == "right":
            second()


def second():
    class firstTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(0, 2)
        Tile_2.location()
        direction = input("Where do you want to go: ")
        if direction == "left":
            start()

gamemap = {start, second}


character = {"Batman" : {"description":
                        "My real name is Bruce Wayne"}}

def character_inventory(player, character):
    for item in character[player]:
        description = character[player]["description"]
        print(f"{player}'s {item} - {description}")


character_choice = input("Enter Batman: ")
while True:
  if character_choice == "Batman":
     character_inventory("Batman", character)
     start()
     second()