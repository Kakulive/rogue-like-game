import random

ITEMS_HEADERS = ["Symbol","Name","Type","Atck","Weight","HP Regen"]
MONSTERS_HEADERS = ["Symbol", "Name","Type","Atck","HP"] 

SYMBOL_INDEX = 0
NAME_INDEX = 1
COORD_INDEX = -1
WEIGHT_INDEX = 4

def print_player_stats(player):
    print(f"{player['name']}  |  Race:{player['race']}  |  HP:{player['hp']}  |  Attack power:{player['atck']}")

def print_map(game_map):
    for row in game_map:
        print(" ".join(row))
    print("\n\n")

def get_single_input(message):
    user_input = input(f"{message}: ")
    print("\n")
    
    return user_input

def print_choose_from_list(label, choices):
    print(label)
    for index, value in enumerate(choices):
        print(f"({index +1}): {value}")

def put_on_board(game_map, stuff):
    for key in stuff:
        col, row = stuff[key][COORD_INDEX]
        game_map[col][row] = stuff[key][SYMBOL_INDEX]

def remove_from_map(game_map, coordinates, symbol):
    row = coordinates[1]
    col = coordinates[0]
    game_map[col][row] = symbol

def print_inventory(player, inventory):
    print("Your current inventory:")
    print(f"{'|'.join(ITEMS_HEADERS[NAME_INDEX:])}\n")
    total_load = 0
    for key in inventory:
        total_load += int(inventory[key][WEIGHT_INDEX])
        print(f"{key}: {'|'.join(inventory[key][NAME_INDEX:COORD_INDEX])}")
    print("\n\nPress (R) to remove item\n\n")
    print(f"Total weight: {total_load}/{player['load']}")

def main_screen():
    print("""
    
 (              (       *                         (     (         )      )  
 )\ )    (      )\ )  (  `     (      (           )\ )  )\ )   ( /(   ( /(  
(()/(    )\    (()/(  )\))(    )\     )\ )    (  (()/( (()/(   )\())  )\()) 
 /(_))((((_)(   /(_))((_)()\((((_)(  (()/(    )\  /(_)) /(_)) ((_)\  ((_)\  
(_))_| )\ _ )\ (_))  (_()((_))\ _ )\  /(_))_ ((_)(_))_ (_))_    ((_)  _((_) 
| |_   (_)_\(_)| _ \ |  \/  |(_)_\(_)(_)) __|| __||   \ |   \  / _ \ | \| | 
| __|   / _ \  |   / | |\/| | / _ \    | (_ || _| | |) || |) || (_) || .` | 
|_|    /_/ \_\ |_|_\ |_|  |_|/_/ \_\    \___||___||___/ |___/  \___/ |_|\_| 
                                                                            
""")