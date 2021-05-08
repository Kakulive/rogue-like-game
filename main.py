import util as util
import engine as engine
import ui as ui
import copy
import sys

MAP_WIDTH = 45
MAP_HEIGHT = 45

def init_game_map():
    game_map = engine.create_map(MAP_WIDTH, MAP_HEIGHT)
    engine.create_rooms(game_map)
    rooms_coordinates = engine.get_room_coordinates(game_map)
    monsters = engine.generate_monsters(rooms_coordinates)
    items = engine.generate_items(rooms_coordinates)
    boss = engine.create_boss(rooms_coordinates)
    ui.put_on_board(game_map, monsters)
    ui.put_on_board(game_map, items)
    ui.put_boss_on_board(game_map, boss)

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

    engine.remove_room_numbers(game_map)
    return game_map, rooms_coordinates, gates_coordinates, items, monsters, boss

def generate_player(game_map, player_map, rooms_coordinates):
    player_coords = engine.get_init_player_coord(rooms_coordinates, 1)
    player = engine.create_player(player_coords)
    engine.put_player_on_board(player_map, player, player_coords)
    engine.reveal_player_map(game_map, player_map, player["coords"])
    inventory = {}
    return player, inventory

def gameplay(game_map, player_map, player, gates_coordinates, items, monsters, inventory, boss):
    util.clear_screen()
    is_running = True
    while is_running:
        engine.get_player_attack(player, inventory)
        ui.main_screen()
        ui.print_map(player_map)
        ui.print_player_stats(player)
        player_position = copy.deepcopy(player["coords"])
        old_player_position = copy.deepcopy(player["coords"])

        key = util.key_pressed()
        if engine.check_inventory(key) == True:
            util.clear_screen()
            ui.print_inventory(player, inventory)
            item_key = util.key_pressed()
            if engine.inventory_remove_check(item_key) == True:
                item_to_remove = ui.get_single_input("Which item to remove?")
                engine.remove_item_from_inventory(inventory, item_to_remove)
                ui.print_inventory(player, inventory)
            ui.press_enter_to_continue()
            continue

        new_player_position, is_running = engine.make_move(key, player_position, is_running, player, inventory)
        if engine.is_item(game_map, new_player_position, items) == True:
            player["coords"] = new_player_position
            engine.add_item_to_inventory(player["coords"], inventory, items)
            engine.remove_item(game_map, player_map, items, player["coords"])
            engine.clear_position(old_player_position, player_map)

        elif engine.is_boss(game_map, new_player_position, boss) == True:
            victory = boss_fight(player, boss, new_player_position)
            if victory == True and engine.is_player_alive(player) == True:
                ui.print_victory_screen()
                sys.exit()

        elif engine.is_enemy(game_map, new_player_position, monsters) == True:
            victory = battlemode(player, monsters, new_player_position)
            if victory == True:
                player["coords"] = new_player_position
                engine.remove_monster(game_map, player_map, monsters, player["coords"])
                engine.clear_position(old_player_position, player_map)

        elif engine.is_gate(game_map, new_player_position) == True:
            player["coords"] = engine.gate_travel(gates_coordinates, new_player_position)
            engine.clear_position(old_player_position, player_map)

        elif engine.is_not_wall(game_map, new_player_position) == True:
            player["coords"] = new_player_position
            engine.clear_position(old_player_position, player_map)

        if engine.is_player_alive(player) == False:
            ui.print_game_over()
            sys.exit()
            
        engine.put_player_on_board(player_map, player, player["coords"])
        engine.reveal_player_map(game_map, player_map, player["coords"])
        util.clear_screen()

def boss_fight(player, boss, new_player_position):
    util.clear_screen()
    enemy = boss
    is_retreat = False
    while (engine.is_player_alive(player) == True and engine.is_enemy_alive(enemy) == True) and is_retreat == False:
        util.clear_screen()
        ui.print_boss_battle(player, enemy)
        player_move = util.key_pressed()
        is_retreat = engine.battle(player, enemy, player_move, is_retreat)
    if is_retreat == False:
        return True
    else:
        return False 

def battlemode(player, monsters, new_player_position):
    util.clear_screen()
    enemy = engine.monster_check(new_player_position, monsters)
    is_retreat = False
    while (engine.is_player_alive(player) == True and engine.is_enemy_alive(enemy) == True) and is_retreat == False:
        util.clear_screen()
        ui.print_battle(player, enemy)
        player_move = util.key_pressed()
        is_retreat = engine.battle(player, enemy, player_move, is_retreat)
    if is_retreat == False:
        return True
    else:
        return False 

def main():
    ui.main_screen()

    game_map, rooms_coordinates, gates_coordinates, items, monsters, boss = init_game_map()
    player_map = engine.create_player_map(game_map)
    player, inventory = generate_player(game_map, player_map, rooms_coordinates)

    gameplay(game_map, player_map, player, gates_coordinates, items, monsters, inventory, boss)

if __name__ == '__main__':
    main()