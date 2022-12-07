def get_assignments():
    with open("assignments.txt") as file:
        return [line.split(",") for line in file.readlines()]


def find_fully_overlapping_assignments(assignments):
    overlapping_sections = 0
    for assignment in assignments:
        first_start, first_stop = assignment[0].split("-")
        second_start, second_stop = assignment[1].split("-")

        first_range = [i for i in range(int(first_start), int(first_stop) + 1)]
        second_range = [i for i in range(int(second_start), int(second_stop) + 1)]

        if all(x in first_range for x in second_range) or all(
            x in second_range for x in first_range
        ):
            overlapping_sections += 1

    return overlapping_sections


def find_partially_overlapping_assignments(assignments):
    overlapping_sections = 0
    for assignment in assignments:
        first_start, first_stop = assignment[0].split("-")
        second_start, second_stop = assignment[1].split("-")

        first_range = [i for i in range(int(first_start), int(first_stop) + 1)]
        second_range = [i for i in range(int(second_start), int(second_stop) + 1)]

        if any(x in first_range for x in second_range) or any(
            x in second_range for x in first_range
        ):
            overlapping_sections += 1

    return overlapping_sections


def main():
    assignments = get_assignments()
    print(find_fully_overlapping_assignments(assignments))
    print(find_partially_overlapping_assignments(assignments))


if __name__ == "__main__":
    main()
