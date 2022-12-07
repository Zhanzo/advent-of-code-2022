import typing


def get_rucksacks() -> typing.List[str]:
    with open("rucksacks.txt") as file:
        return file.readlines()


def calculate_priority_sum(rucksacks: typing.List[str]) -> int:
    priority_sum = 0

    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        compartment1 = set(rucksack[:mid])
        compartment2 = set(rucksack[mid:])

        for item in compartment1:
            if item in compartment2:
                if item.isupper():
                    priority_sum += ord(item) - 38
                else:
                    priority_sum += ord(item) - 96

    return priority_sum


def calculate_badge_priority_sum(rucksacks: typing.List[str]) -> int:
    priority_sum = 0

    for index in range(0, len(rucksacks), 3):
        rucksack0 = rucksacks[index]
        rucksack1 = rucksacks[index + 1]
        rucksack2 = rucksacks[index + 2]

        for item in rucksack0:
            if item in rucksack1 and item in rucksack2:
                if item.isupper():
                    priority_sum += ord(item) - 38
                else:
                    priority_sum += ord(item) - 96
                break

    return priority_sum


def main():
    rucksacks = get_rucksacks()
    print(calculate_priority_sum(rucksacks))
    print(calculate_badge_priority_sum(rucksacks))


if __name__ == "__main__":
    main()
