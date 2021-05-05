import random

ITEMS_HEADERS = ["Symbol","Name","Type","Atck","Weight","HP Regen"]
MONSTERS_HEADERS = ["Symbol", "Name","Type","Atck","HP"] 

SYMBOL_INDEX = 0
NAME_INDEX = 1
COORD_INDEX = -1
WEIGHT_INDEX = 4
ENEMY_TYPE_INDEX = 1
ENEMY_ATTACK_INDEX = 3
ENEMY_HP_INDEX = 4

def print_player_stats(player):
    print(f"{player['name']}  |  Race:{player['race']}  |  HP:{player['hp']}/{player['max_hp']}  |  Attack power:{player['atck']}")

def print_map(game_map):
    for row in game_map:
        print(" ".join(row))
    print("\n\n")

def get_single_input(message):
    user_input = input (f"{message}: ")
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
        print('  |  '.join(inventory[key][NAME_INDEX:COORD_INDEX]))
    print("\n\nPress (R) to remove item\n\n")
    print(f"Total weight: {total_load}/{player['load']}")

def print_battle(player, enemy):
    print_enemy(enemy[ENEMY_TYPE_INDEX])
    print(f"Player stats: ATTACK: {player['atck']}, HP:{player['hp']}/{player['max_hp']} ")
    print(f"Enemy stats: ATTACK: {enemy[ENEMY_ATTACK_INDEX]}, HP: {enemy[ENEMY_HP_INDEX]}")
    label = "Choose your move!"
    choices = ["ATTACK!" , "RUN"]
    print_choose_from_list(label, choices)

def print_game_over():
    print("""
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

    """)
    input("Press ENTER to continue...")

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

def print_enemy(enemy_type):
    if enemy_type == "BAT":
        print("""
                 _,._       
             __.'   _)                             /'.    .'\ 
            <_,)'.-"a\                             \( \__/ )/
              /' (    \                      ___   / (.)(.) \   ___
  _.-----..,-'   (`"--^                 _.-"`_  `-.|  ____  |.-`  _`"-._
 //              |                   .-'.-'//||`'-.\  V--V  /.-'`||\\'-.'-.
(|   `;      ,   |          VS      `'-'-.// ||    / .___.  \    || \\.-'-'`
  \   ;.----/  ,/                         `-.||_.._|        |_.._||.-'
   ) // /   | |\ \                                 \ ((  )) /
   \ \\`\   | |/ /                                  '.    .'
    \ \\ \  | |\/                                     `\/`
     `" `"  `"`             

        """)

    elif enemy_type == "DUCK":
        print("""
                 _,._                            ,----,
             __.'   _)                      ___.`      `,
            <_,)'.-"a\                      `===  D     :
              /' (    \                       `'.      .'
  _.-----..,-'   (`"--^                          )    (                   ,
 //              |                              /      \_________________/|
(|   `;      ,   |          VS                 /                          |
  \   ;.----/  ,/                             |                           ;
   ) // /   | |\ \                            |               _____       /
   \ \\`\   | |/ /                            |      \       ______7    ,'
    \ \\ \  | |\/                             |       \    ______7     /
     `" `"  `"`                                \       `-,____7      ,'  
                                        ^~^~^~^`\                  /~^~^~^~^
                                          ~^~^~^ `----------------' ~^~^~^
                                         ~^~^~^~^~^^~^~^~^~^~^~^~^~^~^~^~

        """)

    elif enemy_type == "WOLF":
        print("""
                 _,._       
             __.'   _)                                    ,     ,
            <_,)'.-"a\                                    |\---/|
              /' (    \                                  /  , , |
  _.-----..,-'   (`"--^                             __.-'|  / \ /
 //              |                         __ ___.-'        ._O|
(|   `;      ,   |          VS          .-'  '        :      _/
  \   ;.----/  ,/                      / ,    .        .     |
   ) // /   | |\ \                    :  ;    :        :   _/
   \ \\`\   | |/ /                    |  |   .'     __:   /
    \ \\ \  | |\/                     |  :   /'----'| \  |
     `" `"  `"`                       \  |\  |      | /| |
                                       '.'| /       || \ |
                                      | /|.'        '.l \\_
                                      || ||              '-'
                                      '-''-'
        """)

    elif enemy_type == "BEAVER":
        print("""
                 _,._       
             __.'   _)                               _,--""--,_
            <_,)'.-"a\                          _,,-"          \ 
              /' (    \                     ,-e"                ;
  _.-----..,-'   (`"--^                    (*             \     |
 //              |                          \o\     __,-"  )    |
(|   `;      ,   |          VS               `,_   (((__,-"     L___,,--,,__
  \   ;.----/  ,/                               ) ,---\  /\    / -- '' -'-' )
   ) // /   | |\ \                            _/ /     )_||   /---,,___  __/
   \ \\`\   | |/ /                           ''''     ''''|_ /         ""
    \ \\ \  | |\/                                         ''''
     `" `"  `"`                         

        """)

    elif enemy_type == "BEAR":
        print("""
                 _,._    /------\   
             __.'   _)  | MonkaS |                  _         _
            <_,)'.-"a\ / \------/  .-""-.          ( )-"```"-( )          .-""-.
              /' (    \           / O O  \          /         \          /  O O \
  _.-----..,-'   (`"--^           |O .-.  \        /   0 _ 0   \        /  .-. O|
 //              |                \ (   )  '.    _|     (_)     |     .'  (   ) /
(|   `;      ,   |          VS     '.`-'     '-./ |             |`\.-'     '-'.'
  \   ;.----/  ,/                    \         |  \   \     /   /  |         /
   ) // /   | |\ \                    \        \   '.  '._.'  .'   /        /
   \ \\`\   | |/ /                     \        '.   `'-----'`   .'        /
    \ \\ \  | |\/                       \   .'    '-._        .-'\   '.   /
     `" `"  `"`                          |/`          `'''''')    )    `\|
                                        ;                    \    '-..-'/ ;
                                        |                     '.       /  |
                                        |                       `'---'`   |
                                        ;                                 ;
                                        \                               /
                                            `.                           .'
                                            '-._                   _.-'
                                            __/`"  '  - - -  ' "`` \__
                                            /`            /^\           `\ 
                                            \(          .'   '.         )/
                                            '.(__(__.-'       '.__)__).'
        """)