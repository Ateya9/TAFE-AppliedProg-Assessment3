from item import Item
from weapon import Weapon
from armour import Armour
from consumable import Consumable
import random


class ItemList:
    """
    An object that creates and manages all items that are available in the game.
    """
    def __init__(self) -> None:
        """
        An object that creates and manages all items that are available in the game.
        """
        super().__init__()
        self.weapon_list: list[Weapon] = []
        self.armour_list: list[Armour] = []
        self.consumable_list: list[Consumable] = []
        self.exit_key = Item("Key to the exit", "This key unlocks the door to the exit.", True, 0)
        self.weapon_list.append(Weapon("short sword",
                                       "A sharp short sword. It does 3 damage.", True, 1, 3))
        self.weapon_list.append(Weapon("spiky mace",
                                       "A deadly looking mace. It does 4 damage.", True, 4, 4))
        self.weapon_list.append(Weapon("heavy axe",
                                       "A deadly looking mace. It does 6 damage.", True, 8, 6))
        self.weapon_list.append(Weapon("enchanted long sword",
                                       "An enchanted long sword. It does 10 damage.", True, 11, 10))

        self.armour_list.append(Armour("shabby leather armour", "Shoddy leather armour.", True, 1, 1))
        self.armour_list.append(Armour("old chainmail", "An old set of chainmail.", True, 6, 3))
        self.armour_list.append(Armour("full plate mail", "A shiny set of plate mail.", True, 11, 6))

        self.small_healing_pot = Consumable("tiny healing potion", "A very small healing potion. It heals 3 hp.",
                                            True, 3)
        self.consumable_list.append(self.small_healing_pot)
        self.consumable_list.append(Consumable("healing potion", "A healing potion. It heals 5 hp.", True, 5))
        self.consumable_list.append(Consumable("large healing potion", "A large healing potion. It heals 8 hp.",
                                               True, 8))

    def get_exit_key(self) -> Item:
        """
        Gets the exit key item.

        :return:
        """
        return self.exit_key

    def get_small_potion(self) -> Consumable:
        """
        Returns the smallest available potion.

        :return:
        """
        return self.small_healing_pot

    def get_random_item_biased(self, level_range: tuple[int, int]) -> Item:
        """
        Returns a random item based on the input level requirements.

        :param level_range: The range of acceptable leveled items.
        :return:
        """
        # TODO: Implement only returning items inside of the supplied level range.
        type_of_item = random.randint(0, 2)
        result_item = self.small_healing_pot
        match type_of_item:
            case 0:
                # Weapon is chosen.
                result_item = random.choice(self.weapon_list)
            case 1:
                # Armour is chosen.
                result_item = random.choice(self.armour_list)
            case 2:
                # Consumable is chosen.
                result_item = random.choice(self.consumable_list)
        return result_item

    def __check_min_of_desired_level(self, level_range: tuple[int, int], list_to_check: list) -> int:
        """
        Checks whether the minimum of the level range is higher than the maximum level item in a list of items.
        This is to prevent an infinite loop if the player is too high of a level to get relevant loot.

        :param level_range: The level_range that's passed into get_random_item_biased
        :param list_to_check: Which list of items to check the max level for.
        :return:
        """
        max_item_level = 0
        for item in list_to_check:
            if item.estimated_level > max_item_level:
                max_item_level = item.estimated_level
        if level_range[0] > max_item_level:
            min_range = max_item_level
        else:
            min_range = level_range[0]
        return min_range
