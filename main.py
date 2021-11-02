class MapTile:
    """ This Map uses x and y coordinates to print out location"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location(self):
        print("your current location is ", self.x, self.y)

valid_actions = ["forward", "backward", "left", "right"]

def menu():
    print("""Choose an action:
    """)
    for action in valid_actions:
        print(f"* {action}")



def firstTile():
    """ Prints out the menu and the current location for movement in the map """
    class firstTile(MapTile):
        print("""
        You are the start. enter direction to go
        """)
        Tile = MapTile(1, 0)
        Tile.location()
    menu()
    direction = input("Where do you want to go: ")
    if direction.lower() == "forward":
            print(" You are going forward")
            fourthTile()
    if direction.lower() == "backward":
            print("wrong way")
            firstTile()
    if direction.lower() == "left":
            print("wall ahead")
            firstTile()
    if direction.lower() == "right":
        print("You are going right to the second Tile")
        secondTiles()



def secondTiles():
    """ Prints out the menu and the current location for movement in the map """
    class secondTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(2, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the fifth Tile")
            fifthTile()
        if direction.lower() == "backward":
            print("dead end")
            secondTiles()
        if direction.lower() == "left":
            print("You are going right to the third Tile")
            firstTile()
        if direction.lower() == "right":
            print("You are going right to the third Tile")
            thirdTile()
            

def thirdTile():
    """ Prints out the menu and the current location for movement in the map """
    class thirdTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(3, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def fourthTile():
    """ Prints out the menu and the current location for movement in the map """
    class fourthTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(1, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def fifthTile():
    """ Prints out the menu and the current location for movement in the map """
    class fifthTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(2, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def sixthTile():
    """ Prints out the menu and the current location for movement in the map """
    class sixthTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(3, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def seventhTile():
    """ Prints out the menu and the current location for movement in the map """
    class seventhTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(1, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def eighthTile():
    """ Prints out the menu and the current location for movement in the map """
    class secondTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(2, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def ninthTile():
    """ Prints out the menu and the current location for movement in the map """
    class ninthTile(MapTile):
        print("You are at the second tile. enter direction to go")
        Tile_2 = MapTile(3, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            secondTiles()
        if direction.lower() == "backward":
            print("ok")
        if direction.lower() == "left":
            print("okie")
        if direction.lower() == "right":
            print("okay")

def main_map():
    gamemap_2 = [
    ["seventhTile", "eighthTile", "ninthTile",],
    ["fourthTile", "fifthTile", "sixthTile",],
    ["firstTile", "secondTile", "thirdTile",],
    ]
    print(gamemap_2)




# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """ Use the Night Vision Goggles to see
                        in the dark and find your way """, }},
             "Green Lantern": {"Power Ring":
                               {"description":
                                "Use it as a flashlight to find their way", }}}

# This dictionary includes the descriptions of Batman


character = {"Batman":
             {"description":
              """I am a vigilante and my real name is Bruce Wayne!
              """}}

# This dictionary includes the description of Green Lantern


character_2 = {"Green Lantern":
               {"description":
                "My name is Hal Jordan. I come from the Planet Mogo"}}


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory(player, character):
    """ prints out the description for Batman """
    for item in character[player]:
        description = character[player]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory_2(player_2, character_2):
    """ prints out the description for Green Lantern """
    for item in character_2[player_2]:
        description_2 = character_2[player_2]["description"]
        print(f"{player_2}'s {item} - {description_2}")


character_choice = input("Enter Batman or Green Lantern: ")
if character_choice == "Batman":
    character_inventory("Batman", character)
    main_map()
    firstTile()
if character_choice == "Green Lantern":
    character_inventory_2("Green Lantern", character_2)
    firstTile()
