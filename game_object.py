class GameObject:
    """
    Base class of any object in the game.
    """
    def __init__(self, name: str, description: str) -> None:
        """
         Base class of any object in the game.

        :param name: Name of what this is.
        :param description: Description of what this is.
        """
        super().__init__()
        self.name = name
        self.description = description
        self.can_be_attacked = False
