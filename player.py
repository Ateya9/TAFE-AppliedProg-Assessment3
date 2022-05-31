from game_object import GameObject
from creature import Creature
from NPC import NPC
from item import Item
from weapon import Weapon
from armour import Armour
from consumable import Consumable
from location import Location


class Player(Creature):
    def __init__(self, name: str, description: str, level: int, max_hp: int, defence: int, attack: int) -> None:
        super().__init__(name, description, level, max_hp, defence, attack)
        self.inventory: list[Item] = []
        self.equipped_weapon = Weapon("rusty short sword",
                                      "A heavily rusted short sword. It does 2 damage.", True, 0, 2)
        self.equipped_armour = Armour("torn tunic",
                                      "A torn tunic. It doesn't look like it'd protect you from damage.", True, 0, 0)
        self.inventory.append(self.equipped_weapon)
        self.inventory.append(self.equipped_armour)
        self.inventory.append(Consumable("small healing potion",
                                         "A small healing potion. If drank, it will heal you for 3 hp.", True, 3))
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

    def examine(self, target: GameObject):
        # TODO: check current location for target
        print(target.description)

    def equip_item(self, item: Item):
        if item.can_equip:
            if item not in self.inventory:
                print(f"{item.name} isn't in your inventory.")
            else:
                if isinstance(item, Weapon):
                    self.equipped_weapon = item
                elif isinstance(item, Armour):
                    self.equipped_armour = item
        else:
            print(f"{item.name} isn't something you can equip.")

