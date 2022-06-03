from game_object import GameObject
import random


class TerrainList:
    def __init__(self) -> None:
        super().__init__()
        self.__list_of_terrain: list[GameObject] = []
        self.__add_terrain("rock", "A medium sized rock.")
        self.__add_terrain("boulder", "A large boulder.")
        self.__add_terrain("puddle", "A small puddle of water.")
        self.__add_terrain("stalactite", "A pointed rock formation.")
        self.__add_terrain("pool of blood", "A small pool of blood. Something was wounded here.")
        self.__add_terrain("scratches", "A set of scratches on the floor.")
        self.__add_terrain("bone", "A bone.")
        self.__add_terrain("pile of sticks", "A small pile of sticks.")
        self.__add_terrain("skull", "A skull.")

    def __add_terrain(self, name: str, description: str, map_icon: str = "."):
        self.__list_of_terrain.append(GameObject(name, description, map_icon))

    def get_random_terrain_feature(self):
        return random.choice(self.__list_of_terrain)
