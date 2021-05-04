import util as util
import engine as engine
import ui as ui

MAP_WIDTH = 45
MAP_HEIGHT = 45

def init_game_map():
    game_map = engine.create_map(MAP_WIDTH, MAP_HEIGHT)
    engine.create_rooms(game_map)
    # ui.print_map(game_map)
    rooms_coordinates = engine.get_room_coordinates(game_map)

    gate_12 = engine.gate_generator_east(game_map, rooms_coordinates, 1)
    gate_21 = engine.gate_generator_west(game_map, rooms_coordinates, 2)
    gate_23 = engine.gate_generator_east(game_map, rooms_coordinates, 2)
    gate_32 = engine.gate_generator_west(game_map, rooms_coordinates, 3)
    gate_36 = engine.gate_generator_south(game_map, rooms_coordinates, 3)
    gate_63 = engine.gate_generator_north(game_map, rooms_coordinates, 6)
    gate_69 = engine.gate_generator_south(game_map, rooms_coordinates, 6)
    gate_96 = engine.gate_generator_north(game_map, rooms_coordinates, 9)
    gate_98 = engine.gate_generator_west(game_map, rooms_coordinates, 9)
    gate_89 = engine.gate_generator_east(game_map, rooms_coordinates, 8)
    gate_87 = engine.gate_generator_west(game_map, rooms_coordinates, 8)
    gate_78 = engine.gate_generator_east(game_map, rooms_coordinates, 7)
    gate_74 = engine.gate_generator_north(game_map, rooms_coordinates, 7)
    gate_47 = engine.gate_generator_south(game_map, rooms_coordinates, 4)
    gate_45 = engine.gate_generator_east(game_map, rooms_coordinates, 4)
    gate_54 = engine.gate_generator_west(game_map, rooms_coordinates, 5)

    gates_coordinates = {"12":gate_12, "21":gate_21,
                         "23":gate_23, "32":gate_32,
                         "36":gate_36, "63":gate_63,
                         "69":gate_69, "96":gate_96,
                         "98":gate_98, "89":gate_89,
                         "87":gate_87, "87":gate_87,
                         "74":gate_74, "47":gate_47,
                         "45":gate_45, "54":gate_54} 

    return game_map, rooms_coordinates, gates_coordinates

def generate_player(game_map, player_map, rooms_coordinates):
    player_coords = engine.get_init_player_coord(rooms_coordinates, 1)
    player = engine.create_player(player_coords)
    engine.put_player_on_board(player_map, player, player_coords)
    return player

def gameplay(player_map, player):
    util.clear_screen()
    is_running = True
    while is_running:
        ui.main_screen()
        ui.print_map(player_map)
        player_position = player["coords"]

        key = util.key_pressed()
        if key == 'b':
            is_running = False
        elif key == "w":
            player_position[0] -= 1 
            player["coords"] = player_position
        elif key == "s":
            player_position[0] += 1 
            player["coords"] = player_position
        elif key == "a":
            player_position[1] -= 1 
            player["coords"] = player_position
        elif key == "d":
            player_position[1] += 1 
            player["coords"] = player_position
        else:
            pass
        engine.put_player_on_board(player_map, player, player_position)
        util.clear_screen()


def main():  
    ui.main_screen()
    
    game_map, rooms_coordinates, gates_coordinates = init_game_map()
    player_map = engine.create_player_map(game_map)
    player = generate_player(game_map, player_map, rooms_coordinates)
    gameplay(player_map, player)
    # ui.print_map(game_map)
    # print(gates_coordinates)
    # print(player)
    

if __name__ == '__main__':
    main()
