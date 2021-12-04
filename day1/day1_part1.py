# Day 1: Sonar Sweep - Part 1

def calculate_number_of_increases():
    with open("data.txt", "r") as f:
        data = f.read().splitlines()

    number_of_increases = 0
    for index in range(len(data) - 1):
        if int(data[index + 1]) > int(data[index]):
            number_of_increases += 1

    return number_of_increases


if __name__ == '__main__':
    print(calculate_number_of_increases())
