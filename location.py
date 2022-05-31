from __future__ import annotations

from game_object import GameObject


class Location(GameObject):
    def __init__(self, name: str, description: str,
                 location_north: Location,
                 location_east: Location,
                 location_south: Location,
                 location_west: Location,
                 location_contents: list[GameObject]) -> None:
        super().__init__(name, description)
        self.location_north = location_north
        self.location_east = location_east
        self.location_south = location_south
        self.location_west = location_west
        self.location_contents = location_contents
