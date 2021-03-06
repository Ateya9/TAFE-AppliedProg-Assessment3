from game_object import GameObject
from creature import Creature
from NPC import NPC
from item import Item
from weapon import Weapon
from armour import Armour
from item_list import ItemList
from consumable import Consumable


class Player(Creature):
    """
    An object that represents the player.
    """
    def __init__(self, name: str, loot_table: ItemList) -> None:
        """
        An object that represents the player.

        :param name: The name of the player.
        :param loot_table: The main item_list object.
        """
        super().__init__(name, "That's you!", 1, 20, 0, 0)
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
        self.xp = 0
        self.xp_threshold = self.level * 2
        self.__loot_table = loot_table

    def attack_target(self, target: GameObject) -> None:
        """
        Attempts to attack the specified target. If the target has can_be_attacked = false, gives feedback that the
        target cannot be attacked.

        :param target: Attempt to attack this target.
        :return:
        """
        if target.can_be_attacked:
            if isinstance(target, NPC):
                if target.is_dead():
                    print(f"The {target.name} is already dead.")
                else:
                    print(f"You attack the {target.name}.")
                    target.take_damage(self.attack)
                    if target.hostile:
                        target.retaliate(self)
                        if self.is_dead():
                            # If the player is dead, exit immediately.
                            return
                    else:
                        print(f"The {target.name} isn't hostile. You should feel bad for attacking it.")
                    if target.is_dead():
                        print(f"The {target.name} is now dead.")
                        loot = self.__loot_table.get_random_item_biased((self.level - 2, self.level + 1))
                        while loot in self.inventory and isinstance(loot, (Weapon, Armour)):
                            loot = self.__loot_table.get_random_item_biased((self.level - 2, self.level + 1))
                        self.add_item_to_inv(loot, False)
                        print(f"You looted a {loot.name} off of the {target.name}.")
            elif isinstance(target, Player):
                print(f"Why would you want to do that?")
        else:
            print(f"The {target.name} cannot be attacked.")

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

    def add_item_to_inv(self, target: GameObject, player_feedback: bool = True) -> bool:
        """
        Attempts to add the specified GameObject to the player's inventory. If the GameObject isn't an item, prints a
        message stating that it cannot be added to the inventory. If the GameObject is a Weapon or Armour, check if
        it's already in the player's inventory, if it is, state that it's already in the player's inventory. If it's
        not already in the players inventory, add it. Always adds the GameObject to the player's inventory if it's a
        Consumable.

        :param target: Attempt to place this object into the player's inventory.
        :param player_feedback: Whether feedback should be printed to the player when attempting to add the target to
        inventory.
        :return: True or False depending on whether the target was successfully added to the player's inventory.
        """
        success = False
        feedback = ""
        if isinstance(target, Item):
            if isinstance(target, Weapon) or isinstance(target, Armour):
                if target in self.inventory:
                    feedback = f"You've already got a {target.name} in your inventory."
                    success = False
                else:
                    self.inventory.append(target)
                    feedback = f"You put the {target.name} into your inventory."
                    success = True
            elif isinstance(target, Consumable):
                self.inventory.append(target)
                feedback = f"You put the {target.name} into your inventory."
                success = True
        else:
            feedback = f"{target.name} can't be put into your inventory."
        if player_feedback:
            print(feedback)
        return success

    def level_up(self) -> None:
        """
        Increases the player's level by 1, heals them for 999, resets xp to 0 and increases the xp threshold to twice
        the player's current level.

        :return: None
        """
        self.max_hp = self.max_hp + 10
        self.heal(999)
        self.level = self.level + 1
        self.xp = 0
        self.xp_threshold = self.level * 2
