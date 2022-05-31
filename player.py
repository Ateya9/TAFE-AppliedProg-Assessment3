from creature import Creature
from item import Item
from location import Location


class Player(Creature):
    def __init__(self, name: str, description: str, level: int, max_hp: int, defence: int, attack: int) -> None:
        super().__init__(name, description, level, max_hp, defence, attack)
        self.inventory: list[Item] = []
        self.current_location: Location

