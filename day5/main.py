import re
import copy


def get_stacks_and_instructions():
    with open("stacks.txt") as file:
        max_stack_size = 0
        lines = file.readlines()
        for line in lines:
            if any(char.isdigit() for char in line):
                stacks = [[x] for x in line.split()]

                for row_index in range(1, len(line), 4):
                    for column_index in range(max_stack_size - 1, -1, -1):
                        if lines[column_index][row_index] != " ":
                            stacks[(row_index - 1) // 4].append(
                                lines[column_index][row_index]
                            )

                instructions = [
                    lines[index] for index in range(max_stack_size + 2, len(lines))
                ]
                return stacks, instructions

            else:
                max_stack_size += 1


def move_stack_items(stacks, instructions):
    for instruction in instructions:
        result = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)
        amount = int(result.group(1))
        src = int(result.group(2)) - 1
        dest = int(result.group(3)) - 1

        for _ in range(amount):
            elem = stacks[src].pop()
            stacks[dest].append(elem)

    for stack in stacks:
        print(stack[-1], end="")
    print()


def move_stack_items2(stacks, instructions):
    for instruction in instructions:
        result = re.search(r"move (\d+) from (\d+) to (\d+)", instruction)
        amount = int(result.group(1))
        src = int(result.group(2)) - 1
        dest = int(result.group(3)) - 1

        for i in range(-amount, 0, 1):
            elem = stacks[src].pop(i)
            stacks[dest].append(elem)

    for stack in stacks:
        print(stack[-1], end="")
    print()


def main():
    stacks, instructions = get_stacks_and_instructions()
    move_stack_items(copy.deepcopy(stacks), instructions)
    move_stack_items2(stacks, instructions)


if __name__ == "__main__":
    main()
