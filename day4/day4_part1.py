# Day 4: Giant Squid
import numpy as np

BINGO_SIZE = 5
MARKED_FIELD = -1


def create_list_of_boards(data):
    boards = [[int(num) for num in line.split()] for line in data]
    list_of_boards = [
        np.array(boards[line : line + BINGO_SIZE]) for line in range(0, len(boards), 5)
    ]
    return list_of_boards


def create_list_of_drawn_numbers(data):
    return data.split(",")


def read_data():
    with open("data.txt", "r") as f:
        data = [line.strip() for line in f if line.strip()]
    list_of_drawn_numbers = data.pop(0)
    drawn_numbers = create_list_of_drawn_numbers(list_of_drawn_numbers)
    list_of_boards = create_list_of_boards(data)
    return drawn_numbers, list_of_boards


def mark_number_on_board(number, board):
    print(f"====== Checking number: {number} ======\n")
    # board[board == number] = MARKED_FIELD
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == number:
                board[row][col] = MARKED_FIELD
    print(board)


def check_if_bingo(board):
    print(f"====== Checking if bingo ======\n")
    all_row_marked = any([len(np.unique(row)) == 1 for row in board])
    all_column_marked = any([len(np.unique(row)) == 1 for row in board.T])
    return all_row_marked or all_column_marked


def mark_number(drawn_numbers, list_of_boards):
    for number in drawn_numbers:
        for board in list_of_boards:
            mark_number_on_board(int(number), board)
            if drawn_numbers.index(number) >= 4 and check_if_bingo(board):
                return board, int(number)


def calculate_sum_of_unmarked_fields(board):
    return sum([int(value) for value in board.flatten() if value != MARKED_FIELD])


def final_result(num1, num2):
    return num1 * num2


if __name__ == "__main__":
    drawn_numbers, list_of_boards = read_data()
    print(f"Drawn numbers: {drawn_numbers}")
    print(f"Bingo boards: {list_of_boards}")
    board, number = mark_number(drawn_numbers, list_of_boards)
    print(f"Bingo win board: {board} and number: {number}")
    unmarked_fields_sum = calculate_sum_of_unmarked_fields(board)
    print(f"Sum of unmarked fields: {unmarked_fields_sum}")
    result = final_result(unmarked_fields_sum, number)
    print(f"Final result: {result}")
