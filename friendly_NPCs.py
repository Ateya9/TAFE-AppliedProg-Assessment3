from NPC_list import NPCList
from NPC import NPC


class FriendlyNPCs(NPCList):
    """
    An object containing a list of all of the available friendly NPCs.
    """
    def __init__(self) -> None:
        """
        An object containing a list of all of the available friendly NPCs.
        """
        super().__init__()
        self.add_NPC(NPC("Badger", "It's a badger.", 1, 1, 0, 0, False))
        self.add_NPC(NPC("Bat", "It's a small bat. It's hanging from the ceiling, watching you.", 1, 1, 0, 0, False))
        self.add_NPC(NPC("Feral Man", "There's a feral man hiding from you behind some rocks. Best leave him alone",
                         1, 1, 0, 0, False))
