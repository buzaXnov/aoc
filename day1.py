from operator import itemgetter

def argmax(items):
    index, element = max(enumerate(items), key=itemgetter(1))
    return index


def get_elf_calories(filename: str) -> dict:
    # Dividing all calories and creating a dictionary of lists
    all_elves: dict = dict()
    elf_num: int = 0
    elf_calories: list = list()
    file_ = open(filename, 'r')
    all_lines = file_.readlines()

    for line in all_lines:
        if line != '\n':
            elf_calories.append(int(line))
        else:
            all_elves[elf_num] = elf_calories.copy()
            elf_calories.clear()
            elf_num += 1

    all_elves[elf_num] = elf_calories.copy()
    elf_calories.clear()
    return all_elves


# def get_highest_calories_index(all_elves: dict) -> int:
if __name__ == "__main__":
    all_elves = get_elf_calories(filename="day1_puzzle.txt")

    calories_per_elf = [sum(all_elves[elf]) for elf in all_elves]
    max_index = argmax(calories_per_elf)
    print(f"Elf number {max_index + 1} has the most calories: {sum(all_elves[max_index])}")

    all_elves = dict(sorted(all_elves.items(), key=lambda item: sum(item[1]), reverse=True))
    top_three_indices = [x+1 for x in list(all_elves.keys())[:3]]    # plus 1 because of zero indexing
    top_three_values = [sum(x) for x in list(all_elves.values())[:3]]
    print(f"\nThe top three elves carrying the most calories in order are elves {top_three_indices} and in total they "
          f"carry {top_three_values} calories respectively.\nIn total {sum(top_three_values)} calories.")
