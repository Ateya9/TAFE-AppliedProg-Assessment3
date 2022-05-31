from item import Item


class Armour(Item):
    def __init__(self, name: str, description: str, visible: bool, estimated_level: int, armour_rating: int) -> None:
        super().__init__(name, description, visible, estimated_level)
        self.armour_rating = armour_rating
