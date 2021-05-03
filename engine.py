import random
import ui as ui
import copy
import itertools
import util as util

MAP_WIDTH = 45
MAP_HEIGHT = 45
NO_OF_MAP_SLICES_VER = 3
NO_OF_MAP_SLICES_HOR = 3
NO_OF_ROOMS = NO_OF_MAP_SLICES_VER*NO_OF_MAP_SLICES_HOR
MIN_ROOM_WIDTH = 6
MIN_ROOM_HEIGHT = 6
EMPTY_SPACE = " "
FILLER = "\u001b[32m,\u001b[37m"
WALL_SYMBOL = "\u001b[34mW\u001b[37m"
GATE_SYMBOL = "\u001b[35m]\u001b[37m"

DEFAULT_ATTACK = 15

ITEMS_COORD_INDEX = -1
ITEMS_ATCK_INDEX = 3

def create_player(player_init_coords):
    player = {"hp":30, "atck":15, "load":150}
    player["coords"] = list(player_init_coords)

    name = ui.get_single_input("What is your name, adventurer sheepo?")
    player["name"] = name

    available_icons = ["M","F","H","S","P"]
    icons_label = "Available icons to select"
    ui.print_choose_from_list(icons_label, available_icons)
    icon = ui.get_single_input("Please select your icon")
    player["icon"] = available_icons[int(icon)-1]

    available_races = ["black_sheep", "normal_sheep", "rainbow_sheep", "elephant"]
    races_label = "Available races to select"
    ui.print_choose_from_list(races_label, available_races)
    race = ui.get_single_input("Please select your race")
    player["race"] = available_races[int(race)-1]

    return player

def create_map(width, height):
    game_map = []
    for y in range(height):
        temp_row = []
        for x in range(width):
            temp_row.append(EMPTY_SPACE)
        game_map.append(temp_row)

    return game_map

def remove_room_numbers(game_map):
    room_numbers = [str(x + 1) for x in range(NO_OF_MAP_SLICES_HOR * NO_OF_MAP_SLICES_VER)]
    for row_index in range(len(game_map)):
        for column_index in range(len(game_map[row_index])):
            if game_map[row_index][column_index] in room_numbers:
                game_map[row_index][column_index] = FILLER

def create_player_map(game_map):
    player_map = copy.deepcopy(game_map)
    for row_index in range(len(player_map)):
        for column_index in range(len(player_map[row_index])):
            player_map[row_index][column_index] = EMPTY_SPACE

    return player_map

def is_room_coord_valid(room_coords, room_width, room_height, max_width, max_height):
    if max_width - (room_coords[0]+room_width) > 0 and max_height - (room_coords[1]+room_height) > 0:
        return True
    else:
        return False

def insert_room(room_coords, room_height, room_width, game_map, number_to_replace):
    for y in range(room_coords[1],room_coords[1] + room_height):
        for x in range(room_coords[0],room_coords[0] + room_width):
            if y == room_coords[1] or y == room_coords[1] + room_height - 1 or x == room_coords[0] or x == room_coords[0] + room_width -1:
                game_map[y][x] = WALL_SYMBOL
            else:
                game_map[y][x] = number_to_replace

def create_rooms(game_map):
    number_to_replace = "1"

    start_y_coord = 0
    end_y_coord = MAP_HEIGHT//3
    
    for _ in range(NO_OF_MAP_SLICES_VER):
        start_x_coord = 0
        end_x_coord = MAP_WIDTH//3
        for _ in range(NO_OF_MAP_SLICES_HOR):
            room_width = random.choice(list(range(MIN_ROOM_WIDTH,((MAP_WIDTH//NO_OF_MAP_SLICES_HOR)-2))))
            room_height = random.choice(list(range(MIN_ROOM_HEIGHT,((MAP_HEIGHT//NO_OF_MAP_SLICES_VER)-2))))
            room_coords = (random.choice(list(range(start_x_coord,end_x_coord))) , random.choice(list(range(start_y_coord,end_y_coord))))
            while is_room_coord_valid(room_coords, room_width, room_height, end_x_coord, end_y_coord) == False:
                room_coords = (random.choice(list(range(start_x_coord,end_x_coord))),random.choice(list(range(start_y_coord,end_y_coord))))

            insert_room(room_coords, room_height, room_width, game_map, number_to_replace)

            number_to_replace = str(int(number_to_replace) + 1)
            start_x_coord += MAP_WIDTH//NO_OF_MAP_SLICES_HOR
            end_x_coord += MAP_WIDTH//NO_OF_MAP_SLICES_HOR

        start_y_coord += MAP_HEIGHT//NO_OF_MAP_SLICES_VER
        end_y_coord += MAP_HEIGHT//NO_OF_MAP_SLICES_VER

def get_room_coordinates(game_map):
    rooms_coordinates = []
    current_room_numbers = [str(x+1) for x in range(NO_OF_MAP_SLICES_VER * NO_OF_MAP_SLICES_HOR)]
    for room in current_room_numbers:
        single_room = []
        for row_index in range(len(game_map)):
            for column_index in range(len(game_map[row_index])):
                if game_map[row_index][column_index] == room:
                    single_room.append((row_index, column_index))
        rooms_coordinates.append(single_room)
    return rooms_coordinates

def gate_generator_east(game_map, rooms_coordinates, room_number):
    min_col = 9999
    max_col = 0
    max_row = 0
    for coord in rooms_coordinates[room_number-1]:
        if coord[1] > max_row:
            max_row = coord[1]

        if coord[0] > max_col:
            max_col = coord[0]

        if coord[0] < min_col:
            min_col = coord[0]
    
    final_row = max_row + 1
    final_col = random.choice(list(range(min_col,max_col)))

    insert_into_map(game_map, GATE_SYMBOL, final_row, final_col)

    return (final_col, final_row)

def gate_generator_west(game_map, rooms_coordinates, room_number):
    min_col = 9999
    max_col = 0
    min_row = 9999
    for coord in rooms_coordinates[room_number-1]:
        if coord[1] < min_row:
            min_row = coord[1]

        if coord[0] > max_col:
            max_col = coord[0]

        if coord[0] < min_col:
            min_col = coord[0]
    
    final_row = min_row - 1
    final_col = random.choice(list(range(min_col,max_col)))

    insert_into_map(game_map, GATE_SYMBOL, final_row, final_col)

    return (final_col, final_row)

def gate_generator_north(game_map, rooms_coordinates, room_number):
    min_col = 9999
    min_row = 9999
    max_row = 0
    for coord in rooms_coordinates[room_number-1]:
        if coord[0] < min_col:
            min_col = coord[0]

        if coord[1] > max_row:
            max_row = coord[1]

        if coord[1] < min_row:
            min_row = coord[1]
    
    final_col = min_col - 1
    final_row = random.choice(list(range(min_row,max_row)))

    insert_into_map(game_map, GATE_SYMBOL, final_row, final_col)

    return (final_col, final_row)

def gate_generator_south(game_map, rooms_coordinates, room_number):
    max_col = 0
    min_row = 9999
    max_row = 0
    for coord in rooms_coordinates[room_number-1]:
        if coord[0] > max_col:
            max_col = coord[0]

        if coord[1] > max_row:
            max_row = coord[1]

        if coord[1] < min_row:
            min_row = coord[1]
    
    final_col = max_col + 1
    final_row = random.choice(list(range(min_row,max_row)))

    insert_into_map(game_map, GATE_SYMBOL, final_row, final_col)

    return (final_col, final_row)

def insert_into_map(game_map, symbol, x, y):
    game_map[y][x] = symbol

def put_player_on_board(game_map, player, player_coords):
    game_map[player_coords[0]][player_coords[1]] = player["icon"]

def get_init_player_coord(rooms_coordinates, room_number):
    player_coords = random.choice(rooms_coordinates[room_number-1])
    return player_coords

def make_move(key, player_position, is_running):
    if key == 'b':
        is_running = False
    elif key == "w":
        player_position[0] -= 1 
    elif key == "s":
        player_position[0] += 1 
    elif key == "a":
        player_position[1] -= 1 
    elif key == "d":
        player_position[1] += 1 
    return player_position, is_running

def is_not_wall(game_map, new_player_position):
    row = new_player_position[1] 
    col = new_player_position[0]
    return game_map[col][row] != WALL_SYMBOL and game_map[col][row] != EMPTY_SPACE 

def is_gate(game_map, new_player_position):
    row = new_player_position[1]
    col = new_player_position[0]
    return game_map[col][row] == GATE_SYMBOL

def is_item(game_map, new_player_position, items):
    for element in items:
        if items[element][ITEMS_COORD_INDEX] == new_player_position:
            return True
    return False

def check_inventory(key):
    return key == 'i'

def gate_travel(gates_coordinates, player_position):
    if player_position == gates_coordinates["12"]:
        player_position = copy.deepcopy(gates_coordinates["21"])
        player_position[1] += 1
    elif player_position == gates_coordinates["21"]:
        player_position = copy.deepcopy(gates_coordinates["12"])
        player_position[1] -= 1
    
    elif player_position == gates_coordinates["23"]:
        player_position = copy.deepcopy(gates_coordinates["32"])
        player_position[1] += 1
    elif player_position == gates_coordinates["32"]:
        player_position = copy.deepcopy(gates_coordinates["23"])
        player_position[1] -= 1

    elif player_position == gates_coordinates["36"]:
        player_position = copy.deepcopy(gates_coordinates["63"])
        player_position[0] += 1
    elif player_position == gates_coordinates["63"]:
        player_position = copy.deepcopy(gates_coordinates["36"])
        player_position[0] -= 1

    elif player_position == gates_coordinates["69"]:
        player_position = copy.deepcopy(gates_coordinates["96"])
        player_position[0] += 1
    elif player_position == gates_coordinates["96"]:
        player_position = copy.deepcopy(gates_coordinates["69"])
        player_position[0] -= 1


    elif player_position == gates_coordinates["98"]:
        player_position = copy.deepcopy(gates_coordinates["89"])
        player_position[1] -= 1
    elif player_position == gates_coordinates["89"]:
        player_position = copy.deepcopy(gates_coordinates["98"])
        player_position[1] += 1

    elif player_position == gates_coordinates["87"]:
        player_position = copy.deepcopy(gates_coordinates["78"])
        player_position[1] -= 1
    elif player_position == gates_coordinates["78"]:
        player_position = copy.deepcopy(gates_coordinates["87"])
        player_position[1] += 1

    elif player_position == gates_coordinates["74"]:
        player_position = copy.deepcopy(gates_coordinates["47"])
        player_position[0] -= 1
    elif player_position == gates_coordinates["47"]:
        player_position = copy.deepcopy(gates_coordinates["74"])
        player_position[0] += 1

    elif player_position == gates_coordinates["45"]:
        player_position = copy.deepcopy(gates_coordinates["54"])
        player_position[1] += 1
    elif player_position == gates_coordinates["54"]:
        player_position = copy.deepcopy(gates_coordinates["45"])
        player_position[1] -= 1

    return player_position

def reveal_player_map(game_map, player_map, player_coords):
    line_of_sight = list(itertools.product([-1,0,1], repeat=2))
    line_of_sight.remove((0,0))
    for i in range(len(line_of_sight)):
        col = copy.deepcopy(player_coords[1])
        row = copy.deepcopy(player_coords[0])
        new_col = col + line_of_sight[i][1]
        new_row = row + line_of_sight[i][0]
        player_map[new_row][new_col] = game_map[new_row][new_col]

def clear_position(old_player_position, player_map):
    row = old_player_position[1]
    col = old_player_position[0]
    player_map[col][row] = FILLER

def get_random_element(iterable):
    return random.choice(iterable)

def generate_monsters(rooms_coordinates):
    monsters_list = util.read_from_file("monsters.csv", "\u001b[31m")
    monster_number = 1
    monsters = {}
    for i in range((NO_OF_ROOMS-1)*2):
        temp_monster = []

        random_enemy = get_random_element(monsters_list).copy()
        temp_monster.append(random_enemy)

        temp_coordinates = get_random_element(rooms_coordinates[((monster_number-1)//2)])
        temp_monster[0].append(list(temp_coordinates))

        monsters["monster_"+str(monster_number)] = temp_monster[0]
        monster_number += 1

    return monsters

def generate_items(rooms_coordinates):
    items_list = util.read_from_file("all_items.csv", "\u001b[33m")
    item_number = 1
    items = {}
    for i in range(NO_OF_ROOMS*2):
        temp_item = []

        random_item = get_random_element(items_list).copy()
        temp_item.append(random_item)

        temp_coordinates = get_random_element(rooms_coordinates[((item_number-1)//2)])
        temp_item[0].append(list(temp_coordinates))

        items["item_"+str(item_number)] = temp_item[0]
        item_number += 1
    
    return items

def add_item_to_inventory(player_position, inventory, items):
    item_number = len(inventory) + 1
    for element in items:
        if items[element][ITEMS_COORD_INDEX] == player_position:
            key = element
    inventory["item_" + str(item_number)] = items[key]
     
def remove_item(game_map, player_map, items, coordinates):
    for element in items:
        if items[element][ITEMS_COORD_INDEX] == coordinates:
            key = element
    items.pop(key)
    ui.remove_from_map(game_map, coordinates, FILLER)
    ui.remove_from_map(player_map, coordinates, FILLER)

def inventory_remove_check(item_key):
    return item_key == 'r'

def remove_item_from_inventory(inventory, item_to_remove):
    inventory.pop(item_to_remove)

def get_player_attack(player, inventory):
    player["atck"] = DEFAULT_ATTACK
    for key in inventory:
        player["atck"] += int(inventory[key][ITEMS_ATCK_INDEX])