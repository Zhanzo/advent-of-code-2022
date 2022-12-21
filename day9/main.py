class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}x{self.y}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if type(other) is type(self):
            return self.x == other.x and self.y == other.y
        return False


def get_movements():
    with open("movements.txt") as file:
        return [line.strip().split() for line in file.readlines()]


def find_movement(head_pos, tail_pos):
    # check near grid
    for y in range(-1, 2):
        for x in range(-1, 2):
            point = Point(tail_pos.x + x, tail_pos.y + y)
            if head_pos == point:
                return tail_pos

    # check column
    if head_pos.x == tail_pos.x:
        if head_pos.y > tail_pos.y:
            return Point(tail_pos.x, tail_pos.y + 1)
        else:
            return Point(tail_pos.x, tail_pos.y - 1)
    # check row
    elif head_pos.y == tail_pos.y:
        if head_pos.x > tail_pos.x:
            return Point(tail_pos.x + 1, tail_pos.y)
        else:
            return Point(tail_pos.x - 1, tail_pos.y)
    # check diagonals
    elif head_pos.y < tail_pos.y and head_pos.x < tail_pos.x:
        return Point(tail_pos.x - 1, tail_pos.y - 1)
    elif head_pos.y < tail_pos.y and head_pos.x > tail_pos.x:
        return Point(tail_pos.x + 1, tail_pos.y - 1)
    elif head_pos.y > tail_pos.y and head_pos.x > tail_pos.x:
        return Point(tail_pos.x + 1, tail_pos.y + 1)
    elif head_pos.y > tail_pos.y and head_pos.x < tail_pos.x:
        return Point(tail_pos.x - 1, tail_pos.y + 1)

    return tail_pos


def find_visited_positions(movements):
    length = 500
    visited_positions = set()
    head_pos = Point(0, length - 1)
    tail_pos = Point(0, length - 1)
    visited_positions.add(f"{tail_pos}")

    for movement in movements:
        direction = movement[0]
        steps = int(movement[1])

        for _ in range(steps):
            if direction == "U":
                head_pos.y -= 1
            elif direction == "D":
                head_pos.y += 1
            elif direction == "L":
                head_pos.x -= 1
            elif direction == "R":
                head_pos.x += 1

            tail_pos = find_movement(head_pos, tail_pos)
            visited_positions.add(f"{tail_pos}")

    return len(visited_positions)


def find_visited_positions_chain(movements):
    length = 500
    visited_positions = set()
    head_pos = Point(0, length - 1)
    tails = [Point(0, length - 1) for _ in range(9)]
    visited_positions.add(f"{tails[0]}")

    for movement in movements:
        direction = movement[0]
        steps = int(movement[1])

        for _ in range(steps):
            if direction == "U":
                head_pos.y -= 1
            elif direction == "D":
                head_pos.y += 1
            elif direction == "L":
                head_pos.x -= 1
            elif direction == "R":
                head_pos.x += 1

            tails[0] = find_movement(head_pos, tails[0])
            for index in range(1, 9):
                tails[index] = find_movement(tails[index - 1], tails[index])
            visited_positions.add(f"{tails[8]}")

    return len(visited_positions)


def main():
    movements = get_movements()
    print(find_visited_positions(movements))
    print(find_visited_positions_chain(movements))


if __name__ == "__main__":
    main()
