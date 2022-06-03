class GameObject:
    """
    Base class of any object in the game.
    """
    def __init__(self, name: str, description: str, map_icon: str = " ") -> None:
        """
         Base class of any object in the game.

        :param name: Name of what this is.
        :param description: Description of what this is.
        :param map_icon: What should represent this object on the games map display.
        """
        super().__init__()
        self.name = name
        self.description = description
        self.map_icon = map_icon
        self.can_be_attacked = False
