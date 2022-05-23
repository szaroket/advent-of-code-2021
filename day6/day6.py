# Day 6: Lanternfish
from collections import Counter, deque

NUMBER_OF_DAYS = 256


def read_data():
    with open("data.txt", "r") as f:
        data = [int(x) for x in f.read().split(",")]
    return data


def calculate_number_of_fish_from_data(data):
    return dict(Counter(sorted(data)))


def get_full_fish_list(list_of_fish):
    fish_dict = {i: 0 for i in range(9)}
    for fish in list_of_fish:
        fish_dict[fish] = list_of_fish[fish]
    return fish_dict


def rotate_dict(fish_dict):
    values = deque(fish_dict.values())
    values.rotate(-1)
    return dict(zip(fish_dict.keys(), values))


def create_fish(fish_dict):
    for day in range(0, NUMBER_OF_DAYS):
        # checking if there is fish with 0 level
        fish_at_zero = fish_dict[0]
        # rotate values in dict
        fish_dict = rotate_dict(fish_dict)
        # calculate fish with level 6
        fish_dict[6] = fish_dict[6] + fish_at_zero
        print(f"Day {day + 1}: {fish_dict}")
    return fish_dict


def calculate_number_of_fish(fish_dict):
    return sum(fish_dict.values())


if __name__ == "__main__":
    fish = read_data()
    list_of_fish = calculate_number_of_fish_from_data(fish)
    fish_dict = get_full_fish_list(list_of_fish)
    print(f"The initial state of number of fish: {fish_dict}")
    last_fish_dict = create_fish(fish_dict)
    print(f"Total number of fish: {calculate_number_of_fish(last_fish_dict)}")
