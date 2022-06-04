from game_object import GameObject
from map import Map
from player import Player
from hostile_NPCs import HostileNPCs
from friendly_NPCs import FriendlyNPCs
from terrain_list import TerrainList
from item import Item
from item_list import ItemList


failed = False
hostile_npc_list = HostileNPCs()
friendly_NPC_list = FriendlyNPCs()
terrain_list = TerrainList()
item_list = ItemList()
player = Player("Player", item_list)
exit_door = GameObject("exit door", "The door that leads out of the cave.")
exit_key = Item("exit key", "The key to the cave exit.", True, 0)
game_map = Map(hostile_npc_list, friendly_NPC_list, terrain_list, item_list, exit_door, exit_key)


def player_attack(target: str, attacking_player: Player = player):
    pass


def player_use_item(item: str):
    pass


def player_equip_item(item: str):
    pass


def player_pick_up_item(item: str):
    # TODO: This should be automatic as you move onto a space with an item.
    pass


def get_inventory() -> list[Item]:
    return player.inventory


def __move_player(location_coord: tuple[int, int], player_to_move: Player = player):
    pass


def move_player_in_direction(direction: str):
    # TODO: Player should be able to type 'move exit' to use the exit. If they have the key, spawn boss.
    pass


def examine(obj: str):
    # TODO: When examining something that's dead, instead of printing it's description, print 'A dead *name*'
    available_directions = ["north", "east", "south", "west"]
    pass


def examine_direction(direction: str):
    pass


def clarify_target(target_list: list[GameObject]):
    # TODO: When listing objects, if the object is an NPC and it's dead, state it as '*name* (dead)'
    pass


def display_help():
    actions = available_actions.keys()
    print(", ".join(actions))


def player_input(raw_input_text: str):
    # Split the player's input into chunks.
    action_chunks = raw_input_text.lower().split()
    if len(action_chunks) == 0:
        # If the player didn't enter anything.
        print("You must enter an action. Type 'help' to see a list of actions.")
    elif action_chunks[0] in available_actions:
        # If the first word is a valid action.
        if action_chunks[0] in ["help", "map"]:
            # If the action doesn't need an option/target.
            available_actions[action_chunks[0]]()
        elif len(action_chunks) == 1:
            # If the action wasn't supplied a target
            available_actions[action_chunks[0]](None)
        else:
            available_actions[action_chunks[0]](action_chunks[1])
    else:
        print(f"Unknown action: {action_chunks[0]}")


available_actions = {"move": move_player_in_direction,
                     "attack": player_attack,
                     "examine": examine,
                     "drink": player_use_item,
                     "equip": player_equip_item,
                     "collect": player_pick_up_item,
                     "map": game_map.print_map,
                     "help": display_help}

if __name__ == "__main__":
    print("########## CAVE ESCAPE ##########")
    print("You wake up in cold cave. Your head is throbbing and you can't remember how you got here.")
    print("You look behind you and see a large door with a large lock on it. You'll have to find the key to escape.")
    player.name = input(":Please enter your name to continue: ")
    game_map.move_player(player, game_map.get_exit_location_coord())
    print(f"Ok {player.name}, Type 'help' to get a list of possible actions.")
    while not failed:
        player_input(input("What will you do now? "))
