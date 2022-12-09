def get_trees():
    trees = []
    with open("trees.txt") as file:
        for line in file.read().splitlines():
            trees.append([int(x) for x in line])
        return trees


def is_visible_north(trees, y, x) -> bool:
    is_visible = True
    for y2 in range(y):
        if trees[y][x] <= trees[y2][x]:
            is_visible = False
            break
    return is_visible


def is_visible_south(trees, y, x) -> bool:
    is_visible = True
    for y2 in range(y + 1, len(trees)):
        if trees[y][x] <= trees[y2][x]:
            is_visible = False
            break
    return is_visible


def is_visible_west(trees, y, x) -> bool:
    is_visible = True
    for x2 in range(x):
        if trees[y][x] <= trees[y][x2]:
            is_visible = False
            break
    return is_visible


def is_visible_east(trees, y, x) -> bool:
    is_visible = True
    for x2 in range(x + 1, len(trees[y])):
        if trees[y][x] <= trees[y][x2]:
            is_visible = False
            break
    return is_visible


def get_north_viewing_distance(trees, y, x) -> int:
    viewing_distance = 0
    for y2 in range(y - 1, -1, -1):
        viewing_distance += 1
        if trees[y][x] <= trees[y2][x]:
            break
    return viewing_distance


def get_south_viewing_distance(trees, y, x) -> int:
    viewing_distance = 0
    for y2 in range(y + 1, len(trees)):
        viewing_distance += 1
        if trees[y][x] <= trees[y2][x]:
            break
    return viewing_distance


def get_west_viewing_distance(trees, y, x) -> int:
    viewing_distance = 0
    for x2 in range(x - 1, -1, -1):
        viewing_distance += 1
        if trees[y][x] <= trees[y][x2]:
            break
    return viewing_distance


def get_east_viewing_distance(trees, y, x) -> int:
    viewing_distance = 0
    for x2 in range(x + 1, len(trees[y])):
        viewing_distance += 1
        if trees[y][x] <= trees[y][x2]:
            break
    return viewing_distance


def calculate_num_visible_trees(trees) -> int:
    num_visible_trees = 0
    for y in range(len(trees)):
        for x in range(len(trees[y])):
            if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[x]) - 1:
                num_visible_trees += 1
            else:
                if is_visible_north(trees, y, x) or is_visible_south(trees, y, x) or is_visible_west(trees, y, x) or is_visible_east(trees, y, x):
                    num_visible_trees += 1

    return num_visible_trees


def calculate_scenic_score(trees) -> int:
    max_scenic_score = 0
    for y in range(len(trees)):
        for x in range(len(trees[y])):
            if y == 0 or x == 0 or y == len(trees) - 1 or x == len(trees[x]) - 1:
                continue
            else:
                scenic_score = (get_north_viewing_distance(trees, y, x) * get_south_viewing_distance(
                    trees, y, x) * get_west_viewing_distance(trees, y, x) * get_east_viewing_distance(trees, y, x))
                max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score


def main():
    trees = get_trees()
    print(calculate_num_visible_trees(trees))
    print(calculate_scenic_score(trees))


if __name__ == "__main__":
    main()
