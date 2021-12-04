# Day 2: Dive! - Part 1
def increase_horizontal(number):
    position["horizontal"] = position["horizontal"] + number
    print(f'Horizontal position is: {position["horizontal"]}')


def increase_depth(number):
    position["depth"] = position["depth"] + number
    print(f'Depth position is: {position["depth"]}')


def decrease_depth(number):
    position["depth"] = position["depth"] - number
    print(f'Depth position is: {position["depth"]}')


operations = {
    "forward": increase_horizontal,
    "down": increase_depth,
    "up": decrease_depth,
}
position = {"horizontal": 0, "depth": 0}


def read_data():
    with open("data1.txt", "r") as f:
        data = f.read().splitlines()
    return data


def prepare_data(data):
    list_of_commands = []
    for command in data:
        list_of_commands.append(command.split())
    return list_of_commands


def get_final_result():
    data = read_data()
    commands = prepare_data(data)
    for index in range(len(commands)):
        command = commands[index][0]
        number = int(commands[index][1])
        operations[command](number)

    return position["horizontal"] * position["depth"]


if __name__ == "__main__":
    print(get_final_result())
