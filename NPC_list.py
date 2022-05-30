from NPC import NPC
import random


class NPCList:
    def __init__(self) -> None:
        super().__init__()
        self.__NPCList: list[NPC] = []

    def get_random_NPC(self) -> NPC:
        return random.choice(self.__NPCList)
