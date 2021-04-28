import util as util
import engine as engine
import ui as ui

MAP_WIDTH = 45
MAP_HEIGHT = 45

def main():
    game_map = engine.create_map(MAP_WIDTH, MAP_HEIGHT)
    ui.print_map(game_map)

    engine.create_rooms(game_map)
    ui.print_map(game_map)

    rooms_coordinates = engine.get_room_coordinates(game_map)
    gate_1 = engine.gate_generator_room_1(game_map, rooms_coordinates)
    ui.print_map(game_map)
    
    player = engine.create_player()
    player_position = ui.put_player_on_board(game_map, player, rooms_coordinates)
    ui.print_map(game_map)
    
    # util.clear_screen()
    # is_running = True
    # while is_running:
    #     engine.put_player_on_board(board, player)
    #     ui.display_board(board)

    #     key = util.key_pressed()
    #     if key == 'q':
    #         is_running = False
    #     else:
    #         pass
    #     util.clear_screen()

if __name__ == '__main__':
    main()
