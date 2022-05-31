from creature import Creature


class NPC(Creature):
    """
    A non-playable character.
    """
    def __init__(self, name: str, description: str, level: int, max_hp: int, defence: int, attack: int, hostile: bool):
        """
        A non-playable character.

        :param name: Name of this NPC.
        :param description: Description of this NPC.
        :param level: Level of this NPC.
        :param max_hp: How many hit points this NPC has.
        :param defence: How much defence this NPC has.
        :param attack: How much attack this NPC has.
        :param hostile: Is this NPC hostile toward the player?
        """
        super().__init__(name, description, level, max_hp, defence, attack)
        self.hostile = hostile

    def retaliate(self, player: Creature) -> None:
        """
        This method should be run after this NPC is attacked by the player.
        :param player: This should always be the player object.
        :return:
        """
        if self.can_be_attacked and self.hostile:
            if not self.is_dead():
                player.take_damage(self.attack)
                print(f"The {self.name} retaliates and hits you for {self.attack} damage.")
