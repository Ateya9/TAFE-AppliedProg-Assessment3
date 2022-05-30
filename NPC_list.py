from NPC import NPC
import random


class NPCList:
    """
    An object that handles a list of NPCs.
    """
    def __init__(self) -> None:
        """
        An object that handles a list of NPCs.
        """
        super().__init__()
        self.__NPCList: list[NPC] = []

    def get_random_NPC(self) -> NPC:
        """
        Returns a random NPC from the list.
        :return:
        """
        return random.choice(self.__NPCList)

    def add_NPC(self, npc: NPC):
        """
        Adds the NPC to the list of NPCs.

        :param npc: The NPC to add.
        :return:
        """
        self.__NPCList.append(npc)
