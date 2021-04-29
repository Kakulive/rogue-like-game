import random

ITEMS_HEADERS = ["Name","Type","Atck","Weight","HP Regen"]
MONSTERS_HEADERS = ["Name","Type","Atck","HP"] 

def print_map(game_map):
    for row in game_map:
        print("|".join(row))
    print("\n\n")

def get_single_input(message):
    user_input = input(message)
    
    return user_input

def put_player_on_board(game_map, player, rooms_coordinates):
    player_coords = random.choice(rooms_coordinates[0])
    game_map[player_coords[0]][player_coords[1]] = player["icon"]

    return player_coords

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