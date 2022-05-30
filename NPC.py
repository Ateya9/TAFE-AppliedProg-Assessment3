from creature import Creature


class NPC(Creature):
    def __init__(self, name: str, description: str, level: int, hp: int, defence: int, attack: int, hostile: bool):
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
