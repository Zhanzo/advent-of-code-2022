import re


def get_instructions():
    with open("instructions.txt") as file:
        return file.readlines()


def calculate_signal_strength_sum(instructions) -> int:
    cycle = 1
    x = 1
    signal_strength_sum = 0
    for instruction in instructions:
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength_sum += cycle * x

        cycle += 1

        if match := re.match(r"addx (-?\d+)", instruction):
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strength_sum += cycle * x

            cycle += 1
            x += int(match.group(1))

    return signal_strength_sum


def draw(instructions):
    x = 1
    y = 0
    i = 0
    width = 40
    height = 6
    display = [["." for _ in range(width)] for __ in range(height)]
    for instruction in instructions:
        if i in [x - 1, x, x + 1]:
            display[y][i] = "#"

        i += 1
        if i == width:
            i = 0
            y += 1

        if match := re.match(r"addx (-?\d+)", instruction):
            if i in [x - 1, x, x + 1]:
                display[y][i] = "#"

            x += int(match.group(1))
            i += 1

            if i == width:
                i = 0
                y += 1

    for row in display:
        for col in row:
            print(col, end="")
        print()


def main():
    instructions = get_instructions()
    print(calculate_signal_strength_sum(instructions))
    draw(instructions)


if __name__ == "__main__":
    main()
