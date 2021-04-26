import util as util
import engine as engine
import ui as ui

PLAYER_ICON = '🐑'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 39
BOARD_HEIGHT = 39


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
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    ui.display_board(board)

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
