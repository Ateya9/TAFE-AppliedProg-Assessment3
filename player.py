from game_object import GameObject
from creature import Creature
from NPC import NPC
from item import Item
from weapon import Weapon
from armour import Armour
from consumable import Consumable


class Player(Creature):
    """
    An object that represents the player.
    """
    def __init__(self, name: str) -> None:
        """
        An object that represents the player.

        :param name: The name of the player.
        """
        super().__init__(name, "That's you!", 1, 10, 0, 0)
        self.inventory: list[Item] = []
        starter_weapon = Weapon("rusty short sword",
                                "A heavily rusted short sword. It does 2 damage.", True, 0, 2)
        starter_armour = Armour("torn tunic",
                                "A torn tunic. It doesn't look like it'd protect you from damage.", True, 0, 0)
        self.inventory.append(starter_weapon)
        self.inventory.append(starter_armour)
        self.equipped_weapon = starter_weapon
        self.equipped_armour = starter_armour
        self.inventory.append(Consumable("small healing potion",
                                         "A small healing potion. If drank, it will heal you for 3 hp.", True, 3))

    def attack_target(self, target: GameObject) -> None:
        """
        Attempts to attack the specified target. If the target has can_be_attacked = false, gives feedback that the
        target cannot be attacked.

        :param target: Attempt to attack this target.
        :return:
        """
        if isinstance(target, NPC):
            if target.can_be_attacked:
                target.take_damage(self.attack)
                print(f"You attack the {target.name}.")
                if target.hostile:
                    target.retaliate(self)
                else:
                    print(f"The {target.name} isn't hostile. You should feel bad for attacking it.")
        elif isinstance(target, Player):
            print(f"Why would you want to do that?")
        elif not target.can_be_attacked:
            print(f"The {target.name} cannot be attacked.")
        else:
            print("Can't attack that.")

    def equip_item(self, item: GameObject) -> None:
        """
        Attempts to equip the specified GameObject. If the GameObject isn't able to be equipped, give this as feedback.
        If it can be equipped, equip it.

        :param item: The GameObject to try and equip.
        :return:
        """
        if isinstance(item, Item) and item.can_equip:
            if item not in self.inventory:
                print(f"{item.name} isn't in your inventory.")
            else:
                if isinstance(item, Weapon):
                    self.equipped_weapon = item
                elif isinstance(item, Armour):
                    self.equipped_armour = item
        else:
            print(f"{item.name} isn't something you can equip.")

    def drink_consumable(self, item: GameObject) -> None:
        """
        Attempt to consume the specified GameObject. If it's not a consumable, give feedback to the player that it
        cannot be consumed. If it is a consumable, consume it and restore health.

        :param item: The GameObject to try and consume.
        :return:
        """
        if isinstance(item, Consumable):
            if item in self.inventory:
                self.heal(item.heal_amount)
                self.inventory.remove(item)
            else:
                print(f"{item.name} isn't in your inventory.")
        else:
            print(f"{item.name} isn't a consumable.")

    def get_items_from_inv(self, target: str = "all") -> list[Item]:
        """
        Searches through the player's inventory and returns a list of all items that match the specified string. The
        input string is case-insensitive. If no string is supplied, a full list of the players inventory is returned.

        :param target: The item to search for.
        :return:
        """
        if target == "all":
            return self.inventory
        result = []
        for item in self.inventory:
            if item.name.lower() == target.lower():
                result.append(item)
        return result

    def add_item_to_inv(self, target: GameObject) -> bool:
        """
        Attempts to add the specified GameObject to the player's inventory. If the GameObject isn't an item, prints a
        message stating that it cannot be added to the inventory. If the GameObject is a Weapon or Armour, check if
        it's already in the player's inventory, if it is, state that it's already in the player's inventory. If it's
        not already in the players inventory, add it. Always adds the GameObject to the player's inventory if it's a
        Consumable.

        :param target: Attempt to place this object into the player's inventory.
        :return:
        """
        if isinstance(target, Item):
            if isinstance(target, Weapon) or isinstance(target, Armour):
                if target in self.inventory:
                    print(f"You've already got a {target.name} in your inventory.")
                else:
                    self.inventory.append(target)
                    return True
            elif isinstance(target, Consumable):
                self.inventory.append(target)
                return True
        else:
            print(f"{target.name} can't be put into your inventory.")
        return False
