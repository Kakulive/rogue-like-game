import util as util
import engine as engine
import ui as ui

PLAYER_ICON = '🐑'
PLAYER_START_X = 3
PLAYER_START_Y = 3

MAP_WIDTH = 45
MAP_HEIGHT = 45


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    # player = create_player()
    game_map = engine.create_map(MAP_WIDTH, MAP_HEIGHT)
    ui.print_map(game_map)
    engine.create_rooms(game_map)
    ui.print_map(game_map)
    rooms_coordinates = engine.get_room_coordinates(game_map)
    print(rooms_coordinates)

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
