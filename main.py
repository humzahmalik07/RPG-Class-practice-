class Character(object):
    def __init__(self, name, special_power, birthplace):
        self.name = name
        self.special_power = special_power
        self.birthplace = birthplace
        self.location = 'start'

    def introduction(self):
      print('Hi, my name is ', self.name)
      print("I have been chosen by you for this mission. Here are some of my qualitites and background:") 

    def power_birthplace(self):
      print("My special power is my", self.special_power)
      print("My birthplace is", self.birthplace)
      print('\n')

def green_lantern_class():
    class Green_Lantern(Character):
        green_lantern = Character("Green Lantern", "power ring", "Coast City")
        green_lantern.introduction()
        green_lantern.power_birthplace()

def batman_class():
    class Batman(Character):
        batman = Character("Batman", "High Intelligence", "Gotham City")
        batman.introduction()
        batman.power_birthplace()


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


def firstTiles():
    """Prints out the menu and the current location for movement in the map """
    class firstTile(MapTile):
        print("""
        You are at the start. enter direction to go
        """)
        Tile = MapTile(1, 0)
        Tile.location()
    menu()
    direction = input("Where do you want to go: ")
    if direction.lower() == "forward":
            print(" You are going forward")
            fourthTiles()
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
    """Prints out the menu and the current location for movement in the map """
    class secondTile(MapTile):
        print("""
        You are at the second tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the fifth Tile")
            fifthTiles()
        if direction.lower() == "backward":
            print("dead end")
            secondTiles()
        if direction.lower() == "left":
            print("You are going right to the third Tile")
            firstTiles()
        if direction.lower() == "right":
            print("You are going right to the third Tile")
            thirdTiles()


def thirdTiles():
    """Prints out the menu and the current location for movement in the map """
    class thirdTile(MapTile):
        print("""
        You are at the third tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the sixth Tile")
            sixthTiles()
        if direction.lower() == "backward":
            print("Dead end")
            thirdTiles()
        if direction.lower() == "left":
            print("You are going left back to the second Tile")
            secondTiles()
        if direction.lower() == "right":
            print("Wall ahead")
            thirdTiles()


def fourthTiles():
    """Prints out the menu and the current location for movement in the map """
    class fourthTile(MapTile):
        print("""
        You are at the fourth tile. enter direction to go
        """)
        Tile_2 = MapTile(1, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the seventh Tile")
            seventhTiles()
        if direction.lower() == "backward":
            print("You are going back to the first Tile")
            firstTiles()
        if direction.lower() == "left":
            print("Dead End")
            fourthTiles()
        if direction.lower() == "right":
            print("You are going right to the fifth Tile")
            fifthTiles()


def fifthTiles():
    """Prints out the menu and the current location for movement in the map """
    class fifthTile(MapTile):
        print("""
        You are at the fifth tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the eighth Tile")
            eighthTiles()
        if direction.lower() == "backward":
            print("You are going back to the second Tile")
            secondTiles()
        if direction.lower() == "left":
            print("You are going left to the fourth Tile")
            fourthTiles()
        if direction.lower() == "right":
            print("You are going right to the sixth Tile")
            sixthTiles()


def sixthTiles():
    """Prints out the menu and the current location for movement in the map """
    class sixthTile(MapTile):
        print("""
        You are at the sixth tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the ninth Tile")
            ninthTiles()
        if direction.lower() == "backward":
            print("You are going back to the third Tile")
            thirdTiles()
        if direction.lower() == "left":
            print("You are going left to the fifth Tile")
            fifthTiles()
        if direction.lower() == "right":
            print("Dead End")
            sixthTiles()


def seventhTiles():
    """Prints out the menu and the current location for movement in the map """
    class seventhTile(MapTile):
        print("""
        You are at the seventh tile. enter direction to go
        """)
        Tile_2 = MapTile(1, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("Wall ahead")
            seventhTiles()
        if direction.lower() == "backward":
            print("You are going back to the fourth Tile")
            fourthTiles()
        if direction.lower() == "left":
            print("Dead End")
            seventhTiles()
        if direction.lower() == "right":
            print("You are going right to the eighth Tile")
            eighthTiles()


def eighthTiles():
    """Prints out the menu and the current location for movement in the map """
    class secondTile(MapTile):
        print("""
        You are at the eighth tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 2)
        Tile_2.location()
        print(""" Congratulations!!!. You have found the treasure.
                  You will now move to the next round, where you have
                  to escape the enemies with the treasure. """)


def ninthTiles():
    """Prints out the menu and the current location for movement in the map """
    class ninthTile(MapTile):
        print("""
        You are at the ninth tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("Wall ahead")
            ninthTiles()
        if direction.lower() == "backward":
            print("You are going back to the sixth Tile")
            sixthTiles()
        if direction.lower() == "left":
            print("You are going left to the eighth Tile")
            eighthTiles()
        if direction.lower() == "right":
            print("Dead end")
            ninthTiles()


def main_map():
    gamemap_2 = [
            ["seventhTile=(1, 2)", "eighthTile=(2, 2)", "ninthTile=(3, 2)", ],
            ["fourthTile=(1, 1)", "fifthTile=(2, 1)", "sixthTile=(3, 1)", ],
            ["firstTile=(1, 0)", "secondTile=(2, 0)", "thirdTile=(3, 0)", ],
                ]
    print("""All the locations of the map with their x-y coordinates
    are printed below:
    """)
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
    batman_class()
    main_map()
    firstTiles()
if character_choice == "Green Lantern":
    character_inventory_2("Green Lantern", character_2)
    green_lantern_class()
    main_map()
    firstTiles()
  