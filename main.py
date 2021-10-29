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
        if direction == "forward":
            second()


def second():
    class firstTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(0, 2)
        Tile_2.location()
        direction = input("Where do you want to go: ")
        if direction == "backward":
            start()
            

a1 = start()
a2 = second()


gamemap = {a1, a2,
          } 
