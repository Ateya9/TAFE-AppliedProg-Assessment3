from NPC_list import NPCList
from NPC import NPC


class HostileNPCs(NPCList):
    """
    An object containing a list of all of the available hostile NPCs.
    """
    def __init__(self) -> None:
        """
        An object containing a list of all of the available hostile NPCs.
        """
        super().__init__()
        self.add_NPC(NPC("Goblin", "A small runty goblin.", 1, 5, 0, 1, True))
        self.add_NPC(NPC("Massive Spider", "A massive spider! It's about as big as a dog!", 1, 3, 0, 2, True))
        self.add_NPC(NPC("Large Goblin", "A fairly large goblin.", 3, 10, 1, 1, True))
        self.add_NPC(NPC("Wolf", "A wolf with menacing fangs.", 4, 6, 0, 3, True))
        self.add_NPC(NPC("Ghoul", "A lanky ghoul with sharp claws.", 5, 8, 1, 3, True))
        self.add_NPC(NPC("Skeleton", "A skeleton, but not quite dead.", 6, 5, 0, 5, True))
        self.add_NPC(NPC("Bear", "A big 'ol bear. You should maybe run away.", 8, 15, 3, 6, True))
