import typing


def get_calorie_sums() -> typing.List[int]:
    calorie_sums: typing.List[int] = []

    with open("calories.txt") as file:
        temp_sum = 0
        for line in file.readlines():
            if line == "\n":
                calorie_sums.append(temp_sum)
                temp_sum = 0
            else:
                temp_sum += int(line)
        calorie_sums.append(temp_sum)

    return calorie_sums


def top_sums(calorie_sums: typing.List[int], num_sums) -> int:
    assert num_sums <= len(calorie_sums)
    calorie_sums.sort(reverse=True)
    return sum([calorie_sums[i] for i in range(num_sums)])


def main():
    calorie_sums = get_calorie_sums()
    print(max(calorie_sums))
    print(top_sums(calorie_sums, 3))


if __name__ == "__main__":
    main()
