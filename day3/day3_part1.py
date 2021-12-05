# Day 3: Binary Diagnostic
def read_data():
    with open("data1.txt", "r") as f:
        data = [[int(num) for num in line.strip("\n\r")] for line in f]
    return data


def transpose_matrix(matrix):
    return [
        [matrix[row][col] for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]


def binary_to_decimal(binary):
    return int("".join(str(x) for x in binary), 2)


def calculate_gamma_epsilon_rate(matrix):
    t_matrix = transpose_matrix(matrix)
    gamma_rate = []
    epsilon_rate = []
    for row in range(len(t_matrix)):
        number_of_one = 0
        for col in range(len(t_matrix[row])):
            if t_matrix[row][col] == 1:
                number_of_one += 1

        if number_of_one > len(t_matrix[row]) / 2:
            gamma_rate.append(1)
            epsilon_rate.append(0)
        else:
            gamma_rate.append(0)
            epsilon_rate.append(1)

    return gamma_rate, epsilon_rate


def calculate_final_result(gamma, epsilon):
    return gamma * epsilon


if __name__ == "__main__":
    matrix = read_data()
    gamma_binary, epsilon_binary = calculate_gamma_epsilon_rate(matrix)
    gamma_decimal = binary_to_decimal(gamma_binary)
    epsilon_decimal = binary_to_decimal(epsilon_binary)
    print(f"Gamma binary: {gamma_binary}, decimal: {gamma_decimal}")
    print(f"Gamma binary: {epsilon_binary}, decimal: {epsilon_decimal}")
    final_result = calculate_final_result(gamma_decimal, epsilon_decimal)
    print(f"Final result is {final_result}")
