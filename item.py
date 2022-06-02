from game_object import GameObject


class Item(GameObject):
    """
    An item that has no special properties.
    """
    def __init__(self, name: str, description: str, visible: bool, estimated_level: int = 0) -> None:
        """
        An item that has no special properties.

        :param name: Name of this item.
        :param description: Description of this item.
        :param visible: Whether this item is visible to the player.
        :param estimated_level: Estimated level of when this item should be lootable.
        """
        super().__init__(name, description)
        self.__visible = visible
        self.estimated_level = estimated_level
        self.can_equip = False
