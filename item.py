from game_object import GameObject


class Item(GameObject):
    def __init__(self, name: str, description: str, visible: bool, estimated_level: int) -> None:
        super().__init__(name, description)
        self.__visible = visible
        self.estimated_level = estimated_level
