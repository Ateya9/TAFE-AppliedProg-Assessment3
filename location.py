from __future__ import annotations

from game_object import GameObject
from NPC import NPC


class Location:
    def __init__(self, location_contents: list[GameObject]) -> None:
        super().__init__()
        self.contents = location_contents
        self.visible = False

    def get_matching_objects(self, target: str = "all") -> list[GameObject]:
        """
        Returns a list of GameObjects that match the input string. If no string is specified, returns all GameObjects in
        this location.

        :param target:
        :return:
        """
        if target == "all":
            return self.contents
        result = []
        for game_object in self.contents:
            if game_object.name.lower() == target.lower():
                result.append(game_object)
        return result

    def update_visibility(self):
        """
        Sets the visibility of this location and all adjacent locations to True.

        :return:
        """
        self.visible = True

    def contains_hostile_NPC(self) -> bool:
        for game_object in self.contents:
            if isinstance(game_object, NPC) and game_object.hostile:
                return True
        return False

