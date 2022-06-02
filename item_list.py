from item import Item
from weapon import Weapon
from armour import Armour
from consumable import Consumable


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
        self.weapon_list.append(Weapon("short sword", "A sharp short sword. It does 3 damage.", True, 1, 3))
