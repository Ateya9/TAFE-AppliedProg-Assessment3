from game_object import GameObject
from location import Location
from hostile_NPCs import HostileNPCs
from friendly_NPCs import FriendlyNPCs
from terrain_list import TerrainList
from item_list import ItemList
import random


class Map:
    def __init__(self) -> None:
        super().__init__()
        self.map_matrix: list[list[Location]] = []
        self.hostile_NPC_list = HostileNPCs()
        self.friendly_NPC_list = FriendlyNPCs()
        self.terrain_list = TerrainList()
        self.item_list = ItemList()

        for x in range(8):
            self.map_matrix.append([])
            for y in range(8):
                self.map_matrix[x].append(self.create_new_location())

        self.exit_location = self.map_matrix[random.randint(0, 7)][random.randint(0, 7)]
        self.exit_location.contents.append(GameObject("locked door", "I need to find a key to get through this door."))

        self.boss_location = self.exit_location
        while self.boss_location == self.exit_location and self.boss_location.contains_hostile_NPC():
            # If the chosen location for the boss is the exit location, or it already has an enemy there, retry.
            self.boss_location = self.map_matrix[random.randint(0, 7)][random.randint(0, 7)]
        self.boss_location.contents.append(self.hostile_NPC_list.get_boss())

    def create_new_location(self) -> Location:
        location_contents = []
        create_hostile_NPC = (random.randint(1, 10) <= 3)
        create_friendly_NPC = (random.randint(1, 10) <= 3)
        create_terrain_feature = (random.randint(1, 10) <= 7)
        create_item = (random.randint(1, 10) <= 2)
        if create_hostile_NPC:
            location_contents.append(GameObject("enemy", "An enemy. It's too far away to see any details."))
        if create_friendly_NPC:
            location_contents.append(self.friendly_NPC_list.get_random_NPC())
        if create_terrain_feature:
            location_contents.append(self.terrain_list.get_random_terrain_feature())
        if create_item:
            location_contents.append(self.item_list.get_random_item())
        return Location(location_contents)

    def get_starting_location(self) -> Location:
        return self.exit_location
