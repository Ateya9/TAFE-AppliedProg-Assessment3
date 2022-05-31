from game_object import GameObject
from creature import Creature
from NPC import NPC
from item import Item
from location import Location


class Player(Creature):
    def __init__(self, name: str, description: str, level: int, max_hp: int, defence: int, attack: int) -> None:
        super().__init__(name, description, level, max_hp, defence, attack)
        self.inventory: list[Item] = []
        self.current_location: Location

    def attack_target(self, target: GameObject):
        if isinstance(target, NPC):
            if target.can_be_attacked:
                target.take_damage(self.attack)
                print(f"You attack the {target.name}.")
                if target.hostile:
                    target.retaliate(self)
                else:
                    print(f"The {target.name} isn't hostile. You should feel bad for attacking it.")
                if target.is_dead():
                    print(f"The {target.name} is now dead.")
                    # TODO: Loot.
        elif not target.can_be_attacked:
            print(f"The {target.name} cannot be attacked.")
        else:
            print("Error.")
