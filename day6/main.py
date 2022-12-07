def get_datastream() -> str:
    with open("datastream.txt") as file:
        return file.read()


def find_marker(datastream: str, limit) -> int:
    last_chars = []

    for index, char in enumerate(datastream):
        if len(last_chars) < limit:
            last_chars.append(char)
        else:
            unique = True
            for letter in last_chars:
                if last_chars.count(letter) > 1:
                    unique = False
                    break
            if unique:
                return index
            else:
                last_chars.pop(0)
                last_chars.append(char)

    return 0


def main():
    datastream = get_datastream()
    print(find_marker(datastream, 4))
    print(find_marker(datastream, 14))


if __name__ == "__main__":
    main()
