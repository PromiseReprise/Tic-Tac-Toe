# A game of tik tak toe

import random
import time

# Set the game stage
GAME_STAGE = {
    "R1A": "_", "R1B": "_", "R1C": "_",
    "R2A": "_", "R2B": "_", "R2C": "_",
    "R3A": "_", "R3B": "_", "R3C": "_"
}

# Set NPC stage to the game stage, it will act as a move condition
NPC_STAGE = {
    "R1A": "_", "R1B": "_", "R1C": "_",
    "R2A": "_", "R2B": "_", "R2C": "_",
    "R3A": "_", "R3B": "_", "R3C": "_"
}

IS_GAME_OVER = False
is_player_turn = True


# Convert array to string for printing
def array_to_string(array):
    converted_string = " ".join(str(x) for x in array)
    return converted_string


# Stage printing
def show_stage():
    row1 = [GAME_STAGE["R1A"], "|", GAME_STAGE["R1B"], "|", GAME_STAGE["R1C"]]
    row2 = [GAME_STAGE["R2A"], "|", GAME_STAGE["R2B"], "|", GAME_STAGE["R2C"]]
    row3 = [GAME_STAGE["R3A"], "|", GAME_STAGE["R3B"], "|", GAME_STAGE["R3C"]]
    return print(f"{array_to_string(row1)}\n{array_to_string(row2)}\n{array_to_string(row3)}")


# Check if move is valid
def check_move_validity(player_input, is_a_player):
    if player_input in GAME_STAGE:
        if GAME_STAGE[player_input] == "_":
            if is_a_player:
                GAME_STAGE[player_input] = "O"
            else:
                GAME_STAGE[player_input] = "X"
            del NPC_STAGE[player_input]
            return True
        else:
            print("Invalid move, space is already played on, please chose again")
            return False
    else:
        print("Invalid input, please chose again")
        return False


def check_game_state():
    select_player = ["O", "X"]
    for i in select_player:
        if GAME_STAGE["R1A"] == i and GAME_STAGE["R2A"] == i and GAME_STAGE["R3A"] == i\
                or GAME_STAGE["R1B"] == i and GAME_STAGE["R2B"] == i and GAME_STAGE["R3B"] == i\
                or GAME_STAGE["R1C"] == i and GAME_STAGE["R2C"] == i and GAME_STAGE["R3C"] == i\
                or GAME_STAGE["R1A"] == i and GAME_STAGE["R1B"] == i and GAME_STAGE["R1C"] == i\
                or GAME_STAGE["R2A"] == i and GAME_STAGE["R2B"] == i and GAME_STAGE["R3C"] == i\
                or GAME_STAGE["R3A"] == i and GAME_STAGE["R3B"] == i and GAME_STAGE["R3C"] == i\
                or GAME_STAGE["R1A"] == i and GAME_STAGE["R2B"] == i and GAME_STAGE["R3C"] == i\
                or GAME_STAGE["R3A"] == i and GAME_STAGE["R2B"] == i and GAME_STAGE["R1C"] == i:
            if i == "O":
                print("Player wins")
                return True
            else:
                print("NPC wins")
                return True
        elif not NPC_STAGE:
            print("Game Over")
            return True
        else:
            return False


print("Welcome to the game of Tik Tak Toe. It is Players 'O' turn.")
print("To place 'O', input R1, R2 or R3 for row and A, B or C for column. Example: R1B (top row 1, middle column B)")
show_stage()

while not IS_GAME_OVER:

    # Player turn
    if is_player_turn:
        waiting_for_move = True
        while waiting_for_move:
            turn_input = input("Please make a move (R1 R2 R3 for rows and A B C for columns: ").upper()
            if check_move_validity(turn_input, is_player_turn):
                is_player_turn = False
                waiting_for_move = False

    # NPC turn
    else:
        npc_move = random.choice(list(NPC_STAGE.keys()))
        print("NPC moving...")
        time.sleep(1)
        if check_move_validity(npc_move, is_player_turn):
            is_player_turn = True

    show_stage()
    IS_GAME_OVER = check_game_state()

