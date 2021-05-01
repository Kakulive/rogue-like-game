import random

ITEMS_HEADERS = ["Name","Type","Atck","Weight","HP Regen"]
MONSTERS_HEADERS = ["Name","Type","Atck","HP"] 

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