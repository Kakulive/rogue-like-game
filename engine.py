import random
import ui as ui

MAP_WIDTH = 45
MAP_HEIGHT = 45
NO_OF_MAP_SLICES_VER = 3
NO_OF_MAP_SLICES_HOR = 3
MIN_ROOM_WIDTH = 6
MIN_ROOM_HEIGHT = 6
# FILLER = color("-", fg="red")
# WALL_SYMBOL = "\033[91m" + "%" + "\033[0m"
FILLER = "-"
WALL_SYMBOL = "W"
GATE_SYMBOL = "]"

def create_player():
    player = {"race": 'human', "hp":30, "atck":15, "load":150}

    name = ui.get_single_input("What is your name, adventurer sheepo?: ")
    player["name"] = name

    available_icons = ["M","F","H","S"]
    available_races = ["black_sheep", "normal_sheep", "rainbow_sheep", "elephant"]

    player["icon"] = "P"
    # '''
    # Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    # Fell free to extend this dictionary!

    # Returns:
    # dictionary
    # '''
    return player

def create_map(width, height):
    game_map = []
    for y in range(height):
        temp_row = []
        for x in range(width):
            temp_row.append(FILLER)
        game_map.append(temp_row)

    return game_map

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

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass