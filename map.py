from game_object import GameObject
from location import Location
from NPC import NPC
from hostile_NPCs import HostileNPCs
from friendly_NPCs import FriendlyNPCs
from terrain_list import TerrainList
from item import Item
from item_list import ItemList
from player import Player
import random


class Map:
    """
    An object that handles creating and managing the game map.
    """
    __MAP_DIMENSIONS = 8

    def __init__(self, hostile_npc_list: HostileNPCs,
                 friendly_npc_list: FriendlyNPCs,
                 terrain_list: TerrainList,
                 item_list: ItemList,
                 exit_door: GameObject,
                 exit_key: GameObject) -> None:
        """
        An object that handles creating and managing the game map.

        :param hostile_npc_list: The main HostileNPCs object.
        :param friendly_npc_list: The main FriendlyNPCs object.
        :param terrain_list: The main TerrainList object.
        :param item_list: The main ItemList object.
        """
        super().__init__()
        self.map_matrix: list[list[Location]] = []
        self.__hostile_NPC_list = hostile_npc_list
        self.__friendly_NPC_list = friendly_npc_list
        self.__terrain_list = terrain_list
        self.__item_list = item_list
        self.directions = ["north", "east", "south", "west"]

        for x in range(Map.__MAP_DIMENSIONS):
            self.map_matrix.append([])
            for y in range(Map.__MAP_DIMENSIONS):
                self.map_matrix[x].append(self.__create_new_location())

        randint_max = Map.__MAP_DIMENSIONS - 1
        # Put the exit (also the entrance) in a random Location.
        self.exit_location = self.map_matrix[random.randint(0, randint_max)][random.randint(0, randint_max)]
        self.exit_door = exit_door
        self.exit_location.contents.append(exit_door)
        self.exit_key = exit_key
        potential_key_location = self.get_location_coord(self.exit_location)
        while potential_key_location == self.get_location_coord(self.exit_location):
            # Pick a random location until the exit location isn't chosen
            potential_key_location = (random.randint(0, randint_max), random.randint(0, randint_max))
        # Put the key in this random location.
        self.get_location(potential_key_location).contents.append(self.exit_key)

    def __create_new_location(self) -> Location:
        """
        Creates a new location containing random NPCs, Terrain and a low chance of collectable healing potions.

        :return:
        """
        location_contents = []
        create_hostile_npc = (random.randint(1, 10) <= 3)
        create_friendly_npc = (random.randint(1, 10) <= 3)
        create_terrain_feature = (random.randint(1, 10) <= 7)
        create_item = (random.randint(1, 10) <= 2)
        if create_hostile_npc:
            location_contents.append(self.__hostile_NPC_list.monster_placeholder)
        if create_friendly_npc:
            location_contents.append(self.__friendly_NPC_list.get_random_NPC())
        if create_terrain_feature:
            location_contents.append(self.__terrain_list.get_random_terrain_feature())
        if create_item:
            location_contents.append(self.__item_list.get_small_potion())
        return Location(location_contents)

    def get_starting_location(self) -> Location:
        """
        Returns the player's starting location.

        :return:
        """
        return self.exit_location

    def get_location_coord(self, location: Location) -> tuple[int, int] | None:
        """
        Gets the coordinates of the supplied location within the map matrix. If the supplied location can't be found,
        returns None.

        :param location: The location to look for.
        :return:
        """
        for x in range(Map.__MAP_DIMENSIONS):
            for y in range(Map.__MAP_DIMENSIONS):
                if self.map_matrix[x][y] == location:
                    return x, y
        return None

    def get_player_current_location(self, player: Player) -> tuple[int, int] | None:
        """
        Finds the supplied player object's location in the map matrix and returns those coordinates. Returns None if the
        player cannot be found.

        :param player: The player to find.
        :return:
        """
        for x in range(Map.__MAP_DIMENSIONS):
            for y in range(Map.__MAP_DIMENSIONS):
                current_location = self.map_matrix[x][y]
                if player in current_location.contents:
                    return self.get_location_coord(current_location)
        return None

    def move_player(self, player: Player, move_to_coord: tuple[int, int]) -> bool:
        """
        Moves the specified player to the supplied coordinates in the map matrix. If the coordinates are out of the
        bounds of the map matrix, return False. Return True if the player was moved successfully.

        :param player: The player to move.
        :param move_to_coord: The coordinates to move to.
        :return:
        """
        if move_to_coord is None:
            return False
        elif 0 <= move_to_coord[0] < Map.__MAP_DIMENSIONS and 0 <= move_to_coord[1] < Map.__MAP_DIMENSIONS:
            # If the supplied coordinate is within the bounds of the map.
            player_coord = self.get_player_current_location(player)
            if player_coord is not None:
                self.map_matrix[player_coord[0]][player_coord[1]].contents.remove(player)
            self.map_matrix[move_to_coord[0]][move_to_coord[1]].contents.append(player)
            self.update_visibility(move_to_coord)
        return False

    def get_location(self, coord: tuple[int, int]) -> Location | None:
        """
        Returns the Location object at the specified coordinates in the map matrix. Returns None if Location is out of
        bounds

        :param coord: The coordinates of the object.
        :return:
        """
        if coord is None:
            return None
        elif 0 <= coord[0] < Map.__MAP_DIMENSIONS and 0 <= coord[1] < Map.__MAP_DIMENSIONS:
            # If supplied coordinates are within the bounds of the map.
            return self.map_matrix[coord[0]][coord[1]]
        return None

    def get_exit_location_coord(self) -> tuple[int, int]:
        """
        Returns the coordinates of the exit location

        :return: tuple[int, int]
        """
        return self.get_location_coord(self.exit_location)

    def update_visibility(self, coord: tuple[int, int]):
        """
        Updates the visibility of the specified and adjacent Location.

        :param coord: The coordinate of the area to update.
        :return:
        """
        locations_to_update = [self.get_location(coord),
                               self.get_location(self.convert_coord_using_direction("north", coord)),
                               self.get_location(self.convert_coord_using_direction("east", coord)),
                               self.get_location(self.convert_coord_using_direction("south", coord)),
                               self.get_location(self.convert_coord_using_direction("west", coord))]
        for location in locations_to_update:
            if isinstance(location, Location):
                location.visible = True

    def convert_coord_using_direction(self, direction: str, coord: tuple[int, int]) -> tuple[int, int] | None:
        """
        Returns the coordinate of a location based on the direction and starting coordinate supplied.
        Returns None if the supplied direction is invalid.

        :param direction: The direction of the location you want.
        :param coord: The starting coordinate.
        :return: tuple[int, int] or None
        """
        dir_lower = direction.lower()
        if dir_lower not in self.directions:
            return None
        match dir_lower:
            case "north":
                return coord[0], coord[1] + 1
            case "east":
                return coord[0] + 1, coord[1]
            case "south":
                return coord[0], coord[1] - 1
            case "west":
                return coord[0] - 1, coord[1]
            case _:
                return None

    def print_map(self) -> None:
        print("P = Player")
        print("E = Enemy")
        print("K = The key to the exit")
        print("X = The exit")
        print("I = Item")
        print("C = A non-hostile creature")
        print(". = Some sort of terrain")
        print("? = Unexplored area")
        top_bottom_row = ["*"]
        for i in range(Map.__MAP_DIMENSIONS):
            top_bottom_row.append("-")
        top_bottom_row.append("*")
        top_bottom_row = " ".join(top_bottom_row)
        file = open("Map.txt", "w")
        file.write(top_bottom_row + "\n")
        print(top_bottom_row)
        # Because of the way the matrix is set up, the axes aren't correct unless we rotate the map 90 degrees.
        # to do this, we need to start at the last y coord and go through the x.
        for y in range(Map.__MAP_DIMENSIONS - 1, -1, -1):
            current_line = ["|"]
            for x in range(Map.__MAP_DIMENSIONS):
                if not self.map_matrix[x][y].visible:
                    location_symbol = "?"
                else:
                    location_contents = self.map_matrix[x][y].contents
                    # TODO: Improve this so it's not going over the same list of contents multiple times.
                    if any(isinstance(game_object, Player) for game_object in location_contents):
                        # If the player is in this Location
                        location_symbol = "P"
                    elif any(game_object is self.exit_key for game_object in location_contents):
                        # If the key to the exit is in this Location
                        location_symbol = "K"
                    elif any(isinstance(game_object, NPC) and game_object.hostile for game_object in location_contents):
                        # If there is an enemy in this Location
                        location_symbol = "E"
                    elif any(game_object is self.exit_door for game_object in location_contents):
                        # If the exit is in this Location
                        location_symbol = "X"
                    elif any(isinstance(game_object, Item) for game_object in location_contents):
                        # If there is an item at this Location
                        location_symbol = "I"
                    elif any(isinstance(game_object, NPC) for game_object in location_contents):
                        # If there is any other sort of NPC in this Location
                        location_symbol = "C"
                    elif any(game_object in self.__terrain_list.list_of_terrain for game_object in location_contents):
                        # If there is a terrain feature at this Location
                        location_symbol = "."
                    else:
                        location_symbol = " "
                current_line.append(location_symbol)
            current_line.append("|")
            current_line = " ".join(current_line)
            print(current_line)
            file.write(current_line + "\n")
        print(top_bottom_row)
        file.write(top_bottom_row + "\n")
        file.close()
