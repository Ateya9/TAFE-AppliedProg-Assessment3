from game_object import GameObject
from location import Location
from hostile_NPCs import HostileNPCs
from friendly_NPCs import FriendlyNPCs
from terrain_list import TerrainList
from item_list import ItemList
# TODO: Implement ItemList
from player import Player
import random


class Map:
    """
    An object that handles creating and managing the game map.
    """
    __MAP_DIMENSIONS = 8

    def __init__(self, hostile_NPC_list: HostileNPCs,
                 friendly_NPC_list: FriendlyNPCs,
                 terrain_list: TerrainList,
                 item_list: ItemList) -> None:
        """
        An object that handles creating and managing the game map.

        :param hostile_NPC_list: The main HostileNPCs object.
        :param friendly_NPC_list: The main FriendlyNPCs object.
        :param terrain_list: The main TerrainList object.
        :param item_list: The main ItemList object.
        """
        super().__init__()
        self.map_matrix: list[list[Location]] = []
        self.__hostile_NPC_list = hostile_NPC_list
        self.__friendly_NPC_list = friendly_NPC_list
        self.__terrain_list = terrain_list
        self.__item_list = item_list

        for x in range(Map.__MAP_DIMENSIONS):
            self.map_matrix.append([])
            for y in range(Map.__MAP_DIMENSIONS):
                self.map_matrix[x].append(self.__create_new_location())

        randint_max = Map.__MAP_DIMENSIONS - 1
        self.exit_location = self.map_matrix[random.randint(0, randint_max)][random.randint(0, randint_max)]
        self.exit_location.contents.append(GameObject("locked door", "I need to find a key to get through this door."))

    def __create_new_location(self) -> Location:
        """
        Creates a new location containing a random number of NPCs, Terrain and a low chance of collectable items.

        :return:
        """
        location_contents = []
        create_hostile_NPC = (random.randint(1, 10) <= 3)
        create_friendly_NPC = (random.randint(1, 10) <= 3)
        create_terrain_feature = (random.randint(1, 10) <= 7)
        create_item = (random.randint(1, 10) <= 2)
        if create_hostile_NPC:
            location_contents.append(GameObject("enemy", "An enemy. It's too far away to see any details."))
        if create_friendly_NPC:
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

    def get_location_coord(self, location: Location) -> tuple[int, int]:
        """
        Gets the coordinates of the supplied location within the map matrix. If the supplied location can't be found,
        returns None.

        :param location: The location to look for.
        :return:
        """
        for x in range(Map.__MAP_DIMENSIONS):
            for y in range(Map.__MAP_DIMENSIONS):
                if self.map_matrix[x][y] == location:
                    return (x, y)
        return None

    def get_player_current_location(self, player: Player) -> tuple[int, int]:
        """
        Finds the supplied player object's location in the map matrix and returns those coords. Returns None if the
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
        elif 0 > move_to_coord[0] >= Map.__MAP_DIMENSIONS:
            return False
        elif 0 > move_to_coord[1] >= Map.__MAP_DIMENSIONS:
            return False
        player_coord = self.get_player_current_location(player)
        if player_coord is not None:
            self.map_matrix[player_coord[0]][player_coord[1]].contents.remove(player)
        self.map_matrix[move_to_coord[0]][move_to_coord[1]].contents.append(player)
        return True

    def get_location(self, coord: tuple[int, int]) -> Location:
        """
        Returns the Location object at the specified coordinates in the map matrix.

        :param coord: The coordinates of the object.
        :return:
        """
        return self.map_matrix[coord[0]][coord[1]]
