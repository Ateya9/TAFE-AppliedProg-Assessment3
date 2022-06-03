from game_object import GameObject
from map import Map
from player import Player
from hostile_NPCs import HostileNPCs
from friendly_NPCs import FriendlyNPCs
from terrain_list import TerrainList
from item import Item
from item_list import ItemList


failed = False

if __name__ == "__main__":
    hostile_npc_list = HostileNPCs()
    friendly_NPC_list = FriendlyNPCs()
    terrain_list = TerrainList()
    item_list = ItemList()
    player = Player("Bob")
    exit_door = GameObject("exit door", "The door that leads out of the cave.")
    exit_key = Item("exit key", "The key to the cave exit.", True, 0)
    game_map = Map(hostile_npc_list, friendly_NPC_list, terrain_list, item_list, exit_door, exit_key)
    game_map.move_player(player, game_map.get_exit_location_coord())
    game_map.print_map()
