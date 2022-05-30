from creature import Creature


class NPC(Creature):
    """
    A non-playable character.
    """
    def __init__(self, name: str, description: str, level: int, hp: int, defence: int, attack: int, hostile: bool):
        """
        A non-playable character.

        :param name: Name of this NPC.
        :param description: Description of this NPC.
        :param level: Level of this NPC.
        :param hp: How many hit points this NPC has.
        :param defence: How much defence this NPC has.
        :param attack: How much attack this NPC has.
        :param hostile: Is this NPC hostile toward the player?
        """
        super().__init__(name, description, level, hp, defence, attack)
        self.hostile = hostile
        self.can_be_attacked = True

    def retaliate(self, player: Creature) -> None:
        """
        This method should be run after this NPC is attacked by the player.
        :param player: This should always be the player object.
        :return:
        """
        if self.hostile and self.can_be_attacked:
            if not self.is_dead():
                self.attack_target(player)
        elif self.can_be_attacked:
            print(f"The {self.name} isn't aggressive. You should feel bad for attacking it.")
        else:
            print(f"You can't attack the {self.name}.")
