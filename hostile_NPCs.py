from NPC_list import NPCList
from NPC import NPC


class HostileNPCs(NPCList):
    """
    An object containing a list of all available hostile NPCs.
    """
    boss = NPC("Minotaur", "A huge minotaur. He must have the key.", 12, 20, 4, 6, True)

    def __init__(self) -> None:
        """
        An object containing a list of all available hostile NPCs.
        """
        super().__init__()
        self.monster_placeholder = NPC("enemy", "Some sort of hostile creature, it's too far away to see what it is.",
                                       0, 0, 0, 0, True)
        self.add_NPC(NPC("Goblin", "A small runty goblin.", 1, 5, 0, 1, True))
        self.add_NPC(NPC("Massive Spider", "A massive spider! It's about as big as a dog!", 1, 3, 0, 2, True))
        self.add_NPC(NPC("Large Goblin", "A fairly large goblin.", 3, 10, 1, 1, True))
        self.add_NPC(NPC("Wolf", "A wolf with menacing fangs.", 4, 6, 0, 3, True))
        self.add_NPC(NPC("Ghoul", "A lanky ghoul with sharp claws.", 5, 8, 1, 3, True))
        self.add_NPC(NPC("Skeleton", "A skeleton, but not quite dead.", 6, 5, 0, 5, True))
        self.add_NPC(NPC("Bear", "A big 'ol bear.", 8, 15, 3, 6, True))

    def get_boss(self) -> NPC:
        return HostileNPCs.boss
