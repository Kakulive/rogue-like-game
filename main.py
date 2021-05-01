import util as util
import engine as engine
import ui as ui
import copy

MAP_WIDTH = 45
MAP_HEIGHT = 45

def init_game_map():
    game_map = engine.create_map(MAP_WIDTH, MAP_HEIGHT)
    engine.create_rooms(game_map)
    rooms_coordinates = engine.get_room_coordinates(game_map)

    gate_12 = list(engine.gate_generator_east(game_map, rooms_coordinates, 1))
    gate_21 = list(engine.gate_generator_west(game_map, rooms_coordinates, 2))
    gate_23 = list(engine.gate_generator_east(game_map, rooms_coordinates, 2))
    gate_32 = list(engine.gate_generator_west(game_map, rooms_coordinates, 3))
    gate_36 = list(engine.gate_generator_south(game_map, rooms_coordinates, 3))
    gate_63 = list(engine.gate_generator_north(game_map, rooms_coordinates, 6))
    gate_69 = list(engine.gate_generator_south(game_map, rooms_coordinates, 6))
    gate_96 = list(engine.gate_generator_north(game_map, rooms_coordinates, 9))
    gate_98 = list(engine.gate_generator_west(game_map, rooms_coordinates, 9))
    gate_89 = list(engine.gate_generator_east(game_map, rooms_coordinates, 8))
    gate_87 = list(engine.gate_generator_west(game_map, rooms_coordinates, 8))
    gate_78 = list(engine.gate_generator_east(game_map, rooms_coordinates, 7))
    gate_74 = list(engine.gate_generator_north(game_map, rooms_coordinates, 7))
    gate_47 = list(engine.gate_generator_south(game_map, rooms_coordinates, 4))
    gate_45 = list(engine.gate_generator_east(game_map, rooms_coordinates, 4))
    gate_54 = list(engine.gate_generator_west(game_map, rooms_coordinates, 5))

    gates_coordinates = {"12":gate_12, "21":gate_21,
                         "23":gate_23, "32":gate_32,
                         "36":gate_36, "63":gate_63,
                         "69":gate_69, "96":gate_96,
                         "98":gate_98, "89":gate_89,
                         "87":gate_87, "78":gate_78,
                         "74":gate_74, "47":gate_47,
                         "45":gate_45, "54":gate_54} 

    return game_map, rooms_coordinates, gates_coordinates

def generate_player(game_map, player_map, rooms_coordinates):
    player_coords = engine.get_init_player_coord(rooms_coordinates, 1)
    player = engine.create_player(player_coords)
    engine.put_player_on_board(player_map, player, player_coords)
    return player

def gameplay(game_map, player_map, player, gates_coordinates):
    util.clear_screen()
    is_running = True
    while is_running:
        ui.main_screen()
        ui.print_map(player_map)
        player_position = copy.deepcopy(player["coords"])
        old_player_position = copy.deepcopy(player["coords"])

        key = util.key_pressed()
        new_player_position, is_running = engine.make_move(key, player_position, is_running)
    
        if engine.is_gate(player_map, new_player_position) == True:
            player["coords"] = engine.gate_travel(gates_coordinates, new_player_position)
            engine.clear_position(old_player_position, player_map)

        elif engine.is_not_wall(player_map, new_player_position) == True:
            player["coords"] = new_player_position
            engine.clear_position(old_player_position, player_map)

        engine.put_player_on_board(player_map, player, player["coords"])
        util.clear_screen()


def main():
    ui.main_screen()
    
    game_map, rooms_coordinates, gates_coordinates = init_game_map()
    player_map = engine.create_player_map(game_map)
    player = generate_player(game_map, player_map, rooms_coordinates)
    gameplay(game_map, player_map, player, gates_coordinates)
    # ui.print_map(game_map)
    # print(gates_coordinates)
    # print(player)
    

if __name__ == '__main__':
    main()
