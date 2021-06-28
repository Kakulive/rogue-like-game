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
ENEMY_NAME_INDEX = 1
BOSS_COORDS_INDEX = -1

def print_player_stats(player):
    print(f"{player['name']}  |  Race:{player['race']}  |  HP:{player['hp']}/{player['max_hp']}  |  Attack power:{player['atck']}")

def print_map(game_map):
    for row in game_map:
        print(" ".join(row))
    print("\n\n")

def valid_input_icons(message):
    while True:
        user_input = input(f"{message}: ")
        try:
            user_input = int(user_input)
        except:
            print("You have to type number from 1 to 5")
            print("\n")
            continue

        if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 4 or user_input == 5:
            return user_input
        else:
            print("You have to choose correct number")
            print("\n")

def valid_input_races(message):
    while True:
        user_input = input(f"{message}: ")
        try:
            user_input = int(user_input)
        except:
            print("You have to type number from 1 to 4")
            print("\n")
            continue

        if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 4:
            return user_input
        else:
            print("You have to choose correct number")
            print("\n")
        

def get_single_input(message):
    user_input = input (f"{message}: ")
    print("\n")
    
    return user_input

def print_choose_from_list(label, choices):
    print(label)
    for index, value in enumerate(choices):
        print(f"({index +1}): {value}")
    print("\n")


def put_on_board(game_map, stuff):
    for key in stuff:
        col, row = stuff[key][COORD_INDEX]
        game_map[col][row] = stuff[key][SYMBOL_INDEX]

def put_boss_on_board(game_map, boss):
    for coord in boss[BOSS_COORDS_INDEX]:
        col = coord[0]
        row = coord[1]
        game_map[col][row] = boss[SYMBOL_INDEX]

def remove_from_map(game_map, coordinates, symbol):
    row = coordinates[1]
    col = coordinates[0]
    game_map[col][row] = symbol

def print_inventory(player, inventory):
    print("Your current inventory:")
    print(f"Item No.  |  " + f"{'  |  '.join(ITEMS_HEADERS[NAME_INDEX:])}\n")
    total_load = 0
    for key in inventory:
        total_load += int(inventory[key][WEIGHT_INDEX])
        print(f"{key}  |  " + '  |  '.join(inventory[key][NAME_INDEX:COORD_INDEX]))
    print("\n\nPress (R) to remove item\n\n")
    print(f"Total weight: {total_load}/{player['load']}")

def print_battle(player, enemy):
    print_enemy(enemy[ENEMY_TYPE_INDEX])
    print(f"Player stats: ATTACK: {player['atck']}, HP:{player['hp']}/{player['max_hp']} ")
    print(f"Enemy stats: ATTACK: {enemy[ENEMY_ATTACK_INDEX]}, HP: {enemy[ENEMY_HP_INDEX]}")
    label = "Choose your move!"
    choices = ["ATTACK!" , "RUN"]
    print_choose_from_list(label, choices)

def print_boss_battle(player, enemy):
    print_boss()
    print(f"Player stats: ATTACK: {player['atck']}, HP:{player['hp']}/{player['max_hp']} ")
    print(f"Enemy stats: ATTACK: {enemy[ENEMY_ATTACK_INDEX]}, HP: {enemy[ENEMY_HP_INDEX]}")
    label = "Choose your move!"
    choices = ["ATTACK!" , "RUN"]
    print_choose_from_list(label, choices)

def print_players_attack_result(player,enemy):
    print(f"WOAH! {player['name']} attacked {enemy[NAME_INDEX]} and dealt {player['atck']} damage! Noice!")

def print_enemys_attack_result(player,enemy):
    print(f"WOAH! {enemy[NAME_INDEX]} attacked {player['name']} and dealt {enemy[ENEMY_ATTACK_INDEX]} damage! NOT Noice!")

def print_enemy_defeated():
    print("""
 _____ _                                              _           _       __           _           _ _ 
|_   _| |                                            (_)         | |     / _|         | |         | | |
  | | | |__   ___    ___ _ __   ___ _ __ ___  _   _   _ ___    __| | ___| |_ ___  __ _| |_ ___  __| | |
  | | | '_ \ / _ \  / _ \ '_ \ / _ \ '_ ` _ \| | | | | / __|  / _` |/ _ \  _/ _ \/ _` | __/ _ \/ _` | |
  | | | | | |  __/ |  __/ | | |  __/ | | | | | |_| | | \__ \ | (_| |  __/ ||  __/ (_| | ||  __/ (_| |_|
  \_/ |_| |_|\___|  \___|_| |_|\___|_| |_| |_|\__, | |_|___/  \__,_|\___|_| \___|\__,_|\__\___|\__,_(_)
                                               __/ |                                                   
                                              |___/                                                    
    """)

def press_enter_to_continue():
    input("Press enter to continue...")


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

def print_victory_screen():
    print("""
  o              o   __o__       o__ __o    ____o__ __o____     o__ __o        o__ __o    \o       o/ 
 <|>            <|>    |        /v     v\    /   \   /   \     /v     v\      <|     v\    v\     /v  
 < >            < >   / \      />       <\        \o/         />       <\     / \     <\    <\   />   
  \o            o/    \o/    o/                    |        o/           \o   \o/     o/      \o/     
   v\          /v      |    <|                    < >      <|             |>   |__  _<|        |      
    <\        />      < >    \\                    |        \\           //    |       \      / \     
      \o    o/         |       \         /         o          \         /     <o>       \o    \o/     
       v\  /v          o        o       o         <|           o       o       |         v\    |      
        <\/>         __|>_      <\__ __/>         / \          <\__ __/>      / \         <\  / \     
    """)
    press_enter_to_continue()

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

def print_boss():
    print("""
                                                                    ."-,.__
                                                                    `.     `.  ,
                                                                .--'  .._,'"-' `.
                                                                .    .'         `'
                                                                `.   /          ,'
                                                                `  '--.   ,-"'
                                                                    `"`   |  \ 
                                                                    -. \, |
                                                                        `--Y.'      ___.
                                                                            \     L._, \ 
                                                                _.,        `.   <  <\                _
                                                                ,' '           `, `.   | \            ( `
                                                            ../, `.            `  |    .\`.           \ \_
                                                            ,' ,..  .           _.,'    ||\l            )  '".
                                                            , ,'   \           ,'.-.`-._,'  |           .  _._`.
                                                        ,' /      \ \        `' ' `--/   | \          / /   ..\ 
                                                        .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
                                                        |  '          ..         `-...-"  |  `-'      / /        . `.
                                                        | /           |L__           |    |          / /          `. `.
                                                    , /            .   .          |    |         / /             ` `
                                                    / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \ 
                                                    / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
                                                    .  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \ 
                                                    ' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
                 _,._    /------\                   |'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \ 
             __.'   _)  | MonkaS |                  ||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
            <_,)'.-"a\ / \------/                   ||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
              /' (    \                             || '              V      / /           `   | `   ,'   ,' '.    !  `. ||
  _.-----..,-'   (`"--^                             ||/            _,-------7 '              . |  `-'    l         /    `||
 //              |                                  . |          ,' .-   ,' ||               | .-.        `.      .'     ||
(|   `;      ,   |          VS                       `'        ,'    `".'    |               |    `.        '. -.'       `'
  \   ;.----/  ,/                                             /      ,'      |               |,'    \-.._,.'/'
   ) // /   | |\ \                                            .     /        .               .       \    .''
   \ \\`\   | |/ /                                          .`.    |         `.             /         :_,'.'
    \ \\ \  | |\/                                             \ `...\   _     ,'-.        .'         /_.-'
     `" `"  `"`                                            `-.__ `,  `'   .  _.>----''.  _  __  /
                                                                 .'        /"'          |  "'   '_
                                                                /_|.-'\ ,".             '.'`__'-( \ 
                                                                  / ,"'"\,'               `/  `-.|
    """)