from __future__ import annotations

from game_object import GameObject


class Creature(GameObject):
    """
    Base class of any creature in the game, including the player.
    """
    def __init__(self, name: str, description: str, level: int, hp: int, defence: int, attack: int) -> None:
        """
        :param name: What this creature is called.
        :param description: A description of this creature.
        :param level: This creature's level.
        :param hp: How many hit points this creature has.
        :param defence: How much defence this creature has.
        :param attack: How much attack this creature has.
        """
        super().__init__(name, description)
        self.level = level
        self.hp = hp
        self.defence = defence
        self.attack = attack

    def is_dead(self) -> bool:
        """
        Returns true or false depending whether this creature has any hit points left.
        :return:
        """
        if self.hp < 1:
            return True
        return False

    def attack_target(self, target: Creature) -> None:
        """
        Attacks the target creature.
        :param target: What is going to be attacked.
        :return:
        """
        target.__take_damage(self.attack)

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
