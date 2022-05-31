from item import Item


class Weapon(Item):
    def __init__(self, name: str, description: str, visible: bool, estimated_level: int, attack_rating: int) -> None:
        super().__init__(name, description, visible, estimated_level)
        self.attack_rating = attack_rating
