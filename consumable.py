from item import Item
from creature import Creature


class Consumable(Item):
    """
    A consumable item that heals the user.
    """
    def __init__(self, name: str, description: str, visible: bool, heal_amount: int) -> None:
        """
        A consumable item that heals the user.

        :param name: Name of the item.
        :param description: Description of the item.
        :param visible: Whether the item is visible to the player.
        :param heal_amount: How much this consumable heals the user for.
        """
        super().__init__(name, description, visible, 0)
        self.heal_amount = heal_amount

    def use_item(self, player: Creature):
        """
        Uses this consumable to restore this items heal_amount to the user as hp.

        :param player: The items user.
        :return:
        """
        player.hp = player.hp + self.heal_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
