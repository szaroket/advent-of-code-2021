# Day 3: Binary Diagnostic
import numpy as np


def read_data():
    with open("data2.txt", "r") as f:
        data = [[int(num) for num in line.strip("\n\r")] for line in f]
    return np.array(data)


def transpose_matrix(matrix):
    return matrix.T


def binary_to_decimal(binary):
    return int("".join(str(x) for x in binary), 2)


def calculate_rating(matrix, par_to_remove_if_one, par_to_remove_if_zero):
    for row in range(len(matrix)):
        counts = np.bincount(matrix[row])
        if counts[0] == counts[1]:
            idx = np.argwhere(matrix[row] == par_to_remove_if_one)
        elif np.argmax(counts) == 1:
            idx = np.argwhere(matrix[row] == par_to_remove_if_one)
        else:
            idx = np.argwhere(matrix[row] == par_to_remove_if_zero)

        matrix = np.delete(matrix, idx, axis=1)
        if len(matrix[row]) == 1:
            break
    return transpose_matrix(matrix)


def calculate_final_result(oxygen, co2):
    return oxygen * co2


if __name__ == "__main__":
    matrix = read_data()
    t_matrix = transpose_matrix(matrix)
    oxygen_rating = calculate_rating(t_matrix, 0, 1)
    co2_rating = calculate_rating(t_matrix, 1, 0)
    oxygen_decimal = binary_to_decimal(oxygen_rating[0])
    co2_decimal = binary_to_decimal(co2_rating[0])
    print(f"oxygen_rating binary: {oxygen_rating}, decimal: {oxygen_decimal}")
    print(f"Gamma binary: {co2_rating}, decimal: {co2_decimal}")
    final_result = calculate_final_result(oxygen_decimal, co2_decimal)
    print(f"Final result is {final_result}")
