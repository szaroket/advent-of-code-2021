# Day 1: Sonar Sweep - Part 2


def read_data():
    with open("data2.txt", "r") as f:
        data = list(map(int, f.read().splitlines()))
    return data


def calculate_list_of_sums():
    list_of_sums = []
    data = read_data()
    for index in range(len(data) - 2):
        list_of_sums.append(data[index] + data[index + 1] + data[index + 2])
    return list_of_sums


def calculate_number_of_increases():
    data = calculate_list_of_sums()
    number_of_increases = 0
    for index in range(len(data) - 1):
        if int(data[index + 1]) > int(data[index]):
            number_of_increases += 1

    return number_of_increases


if __name__ == "__main__":
    print(calculate_number_of_increases())
