from item import Item


class Armour(Item):
    """
    An Armour item.
    """
    def __init__(self, name: str, description: str, visible: bool, estimated_level: int, armour_rating: int) -> None:
        """
        An Armour item.

        :param name: Name of the item.
        :param description: Description of the item.
        :param visible: Whether the item is visible to the player.
        :param estimated_level: The level at which this item should be lootable
        :param armour_rating: How much this armour protects the user. This value directly negates incoming damage 1:1
        """
        super().__init__(name, description, visible, estimated_level)
        self.armour_rating = armour_rating
        self.can_equip = True
