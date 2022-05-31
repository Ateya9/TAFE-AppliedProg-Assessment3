from __future__ import annotations

from game_object import GameObject


class Creature(GameObject):
    """
    Base class of any creature in the game, including the player.
    """
    def __init__(self, name: str, description: str, level: int, max_hp: int, defence: int, attack: int) -> None:
        """
        Base class of any creature in the game, including the player.

        :param name: What this creature is called.
        :param description: A description of this creature.
        :param level: This creature's level.
        :param max_hp: How many hit points this creature has.
        :param defence: How much defence this creature has.
        :param attack: How much attack this creature has.
        """
        super().__init__(name, description)
        self.level = level
        self.max_hp = max_hp
        self.hp = max_hp
        self.defence = defence
        self.attack = attack
        self.can_be_attacked = True

    def is_dead(self) -> bool:
        """
        Returns true or false depending on whether this creature has any hit points left.
        :return:
        """
        if self.hp < 1:
            return True
        return False

    def attack_target(self, target: GameObject) -> None:
        """
        Attacks the target creature.
        :param target: What is going to be attacked.
        :return:
        """
        if target.can_be_attacked:
            # TODO: Fix this.
            target.__take_damage(self.attack)
        else:
            print(f"{target} can't be attacked.")

    def __take_damage(self, initial_damage: int) -> None:
        """
        This creature takes the specified damage (minus their defence).
        :param initial_damage: The amount of damage this creature should take (before defence is considered).
        :return:
        """
        final_damage = initial_damage - self.defence
        if final_damage < 0:
            final_damage = 0
        self.hp = self.hp - final_damage

