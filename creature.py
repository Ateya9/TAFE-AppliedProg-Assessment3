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

    def take_damage(self, initial_damage: int) -> None:
        """
        This creature takes the specified damage (minus their defence).

        :param initial_damage: The amount of damage this creature should take (before defence is considered).
        :return:
        """
        final_damage = initial_damage - self.defence
        if final_damage < 1:
            final_damage = 1
        self.hp = self.hp - final_damage
        print(f"The {self.name} takes {final_damage} damage.")
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount: int) -> None:
        """
        Heals this creature for the specified amount. Cannot be healed above max hp.

        :param amount: Amount to heal this creature for.
        :return:
        """
        self.hp = self.hp + amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"The {self.name} is now on {self.hp} hp.")

