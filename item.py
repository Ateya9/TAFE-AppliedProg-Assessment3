from game_object import GameObject


class Item(GameObject):
    def __init__(self, name: str, description: str, visible: bool) -> None:
        super().__init__(name, description)
        self.__visible = visible
