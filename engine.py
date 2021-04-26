import random

EMPTY_SYMBOL = "-"
NUMER_OF_ROOMS = 9
BOARD_SLICES = 3

def temp_print_board(board):
    for row in board:
        print(row)
    print("\n\n")

def create_board(width, height):
    board = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(EMPTY_SYMBOL)
        board.append(row)

    return board

def create_rooms(board, width, height):
    room_width = random.choice(list(range(1,width//BOARD_SLICES + 1)))
    room_height = random.choice(list(range(1,height//BOARD_SLICES + 1)))
    rooms = []
    for _ in range(NUMER_OF_ROOMS):
        temp_room = create_board(room_width, room_height)
        rooms.append(temp_room)

    return rooms

def room_placement(board, rooms, width, height):
    start_line = 0
    end_line = height//BOARD_SLICES
    
    board_slices = []

    for _ in range(BOARD_SLICES):
        init_row = 0
        init_col = width//BOARD_SLICES
        for _ in range(BOARD_SLICES):
            temp_slice = []
            for row in board[start_line:end_line]:
                temp_slice.append([x for x in row[init_row:init_col]])
            board_slices.append(temp_slice)
            init_row += width//BOARD_SLICES
            init_col += height//BOARD_SLICES
        start_line += height//BOARD_SLICES
        end_line += height//BOARD_SLICES
    
    return board_slices

board = create_board(6,6)
rooms = create_rooms(board, 6, 6)
mini_board = room_placement(board,rooms, 6, 6)
temp_print_board(board)
temp_print_board(rooms)
temp_print_board(mini_board)


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