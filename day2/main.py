import typing


def get_rounds() -> typing.List[typing.List[str]]:
    rounds: typing.List[typing.List[str]] = []

    with open("rounds.txt") as file:
        for line in file.readlines():
            rounds.append(line.split())

    return rounds


def calculate_scores(rounds: typing.List[typing.List[str]]):
    beats = {"X": "C", "Y": "A", "Z": "B"}
    score = {"X": 1, "Y": 2, "Z": 3}
    conversion = {"X": "A", "Y": "B", "Z": "C"}
    total_score = 0

    for round in rounds:
        your_move = round[1]
        opponent_move = round[0]
        move_score = score[your_move]

        if beats[your_move] == opponent_move:
            total_score += move_score + 6
        elif conversion[your_move] == opponent_move:
            total_score += move_score + 3
        else:
            total_score += move_score

    return total_score


def calculate_scores2(rounds: typing.List[typing.List[str]]):
    beats = {"A": "C", "B": "A", "C": "B"}
    loses = {"A": "B", "B": "C", "C": "A"}
    score = {"A": 1, "B": 2, "C": 3}
    total_score = 0

    for round in rounds:
        opponent_move = round[0]
        goal = round[1]

        # lose
        if goal == "X":
            your_move = beats[opponent_move]
            total_score += score[your_move]
        # draw
        elif goal == "Y":
            total_score += score[opponent_move] + 3
        # win
        else:
            your_move = loses[opponent_move]
            total_score += score[your_move] + 6

    return total_score


def main():
    rounds = get_rounds()
    print(calculate_scores(rounds))
    print(calculate_scores2(rounds))


if __name__ == "__main__":
    main()
