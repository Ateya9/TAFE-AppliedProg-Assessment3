from item import Item
from creature import Creature


class Consumable(Item):
    def __init__(self, name: str, description: str, visible: bool, heal_amount: int) -> None:
        super().__init__(name, description, visible, 0)
        self.heal_amount = heal_amount

    def use_item(self, player: Creature):
        player.hp = player.hp + self.heal_amount
        if player.hp > player.max_hp:
            player.hp = player.max_hp
