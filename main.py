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
    # TODO: Player needs to be able to 'use' the exit key to try and exit.
    pass


def player_equip_item(item: str):
    pass


def player_pick_up_item(item: str):
    # TODO: This should be automatic as you move onto a space with an item.
    pass


def get_inventory() -> list[Item]:
    return player.inventory


def move_player_in_direction(direction: str):
    if direction not in game_map.directions:
        print(f"Invalid direction {direction}. Valid directions are: {', '.join(game_map.directions)}.")
    player_location_coord = game_map.get_player_current_location(player)
    if player_location_coord is None:
        player_start_loc = game_map.get_starting_location()
        game_map.move_player(player, game_map.get_location_coord(player_start_loc))
    else:
        player_move_to_coord = game_map.convert_coord_using_direction(direction, player_location_coord)
        if player_move_to_coord is None:
            print(f"You can't move {direction}.")
        else:
            move_successful = game_map.move_player(player, player_move_to_coord)
            if move_successful:
                print(f"You move {direction}.")
                examine("surroundings")
            else:
                print(f"You can't move that way. That's the cave wall.")


def examine(obj: str):
    available_directions = game_map.directions
    available_options = ["{target}"] + available_directions + ["inventory", "surroundings", "weapon", "armour"]
    if obj is None:
        print(f"Available options are: {', '.join(available_options)}")
        return
    if obj in available_directions:
        __examine_direction(obj)
    else:
        player_current_location = game_map.get_player_current_location(player)
        curr_loc_contents = game_map.get_location(player_current_location).contents
        curr_loc_contents_dict = __create_name_dictionary(curr_loc_contents)
        player_inv_dict = __create_name_dictionary(player.inventory)
        if obj == "surroundings":
            print(f"You can see: {', '.join(curr_loc_contents_dict.keys())}")
        elif obj == "inventory":
            print(f"You currently have: {', '.join(player_inv_dict.keys())}")
        elif obj == "weapon":
            print(f"Your currently equipped weapon is: {player.equipped_weapon.name}")
        elif obj == "armour":
            print(f"Your currently equipped armour is: {player.equipped_armour.name}")
        elif obj in player_inv_dict:
            print(f"{player_inv_dict[obj].description}")
        elif obj in curr_loc_contents_dict:
            print(f"{curr_loc_contents_dict[obj].description}")
        else:
            print(f"I don't see a {obj}.")


def __create_name_dictionary(obj_list: list[GameObject]) -> dict[str, GameObject]:
    result = {}
    for game_object in obj_list:
        result[game_object.name.lower()] = game_object
    return result


def __examine_direction(direction: str):
    curr_player_coord = game_map.get_player_current_location(player)
    direction_coord = game_map.convert_coord_using_direction(direction, curr_player_coord)
    examine_location = game_map.get_location(direction_coord)
    if examine_location is None:
        print(f"You look {direction}. You can see the outer cave wall.")
        return
    location_contents_dict = __create_name_dictionary(examine_location.contents)
    print(f"You look {direction}. You can see: {', '.join(location_contents_dict.keys())}")


def clarify_target(target_list: list[GameObject]):
    # TODO: When listing objects, if the object is an NPC and it's dead, state it as '*name* (dead)'
    pass


def display_help():
    actions = available_actions.keys()
    print(f"Available options are: {', '.join(actions)}")


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
            # Join all chucks following the action to account for if there's a space in the target.
            full_target_string = " ".join(action_chunks[1::])
            available_actions[action_chunks[0]](full_target_string)
    else:
        print(f"Unknown action: {action_chunks[0]}")


available_actions = {"move": move_player_in_direction,
                     "attack": player_attack,
                     "examine": examine,
                     "look": examine,
                     "use": player_use_item,
                     "equip": player_equip_item,
                     "collect": player_pick_up_item,
                     "take": player_pick_up_item,
                     "map": game_map.print_map,
                     "help": display_help}

if __name__ == "__main__":
    print("########## CAVE ESCAPE ##########")
    print("You wake up in cold cave. Your head is throbbing and you can't remember how you got here.")
    print("You look behind you and see a large door with a large lock on it. You'll have to find the key to escape.")
    player.name = input(":Please enter your name to continue: ")
    game_map.move_player(player, game_map.get_exit_location_coord())
    # game_map.move_player(player, (0, 0))
    print(f"Ok {player.name}, Type 'help' to get a list of possible actions.")
    examine("surroundings")
    while not failed:
        player_input(input("What will you do now? "))
