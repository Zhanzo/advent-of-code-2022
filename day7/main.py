import re


class Directory:
    def __init__(self, name, parent_directory=None):
        self.name = name
        self.size = 0
        self.subdirectories = []
        self.parent_directory = parent_directory

    def get_size(self):
        return sum(x.get_size() for x in self.subdirectories) + self.size

    def find_matching_size(self):
        curr_size = self.get_size()
        if curr_size <= 100000:
            return curr_size + sum(x.find_matching_size() for x in self.subdirectories)
        else:
            return 0 + sum(x.find_matching_size() for x in self.subdirectories)

    def find_minimal_dir(self, min_dir_size, to_remove):
        my_size = self.get_size()
        if my_size >= to_remove:
            if self.subdirectories:
                return min(my_size, min(x.find_minimal_dir(min_dir_size, to_remove) for x in self.subdirectories))
            else:
                return min(my_size, min_dir_size)
        else:
            return min_dir_size

    def get_child(self, name):
        for child in self.subdirectories:
            if child.name == name:
                return child


def get_commands():
    with open("commands.txt") as file:
        return file.readlines()


def run_commands(commands, root):
    current_dir = root

    for command in commands:
        if match := re.match(r"\$ cd ([a-z]+)", command):
            current_dir = current_dir.get_child(match.group(1))
        if match := re.match(r"dir ([a-z]+)", command):
            current_dir.subdirectories.append(
                Directory(match.group(1), current_dir))
        elif re.match(r"\$ cd \.\.", command):
            current_dir = current_dir.parent_directory
        elif match := re.match(r"(\d+) ", command):
            current_dir.size += int(match.group(1))


def find_min_dir_to_remove(root):
    current_size = root.get_size()
    to_remove = current_size - 40000000

    print(root.find_minimal_dir(current_size, to_remove))


def main():
    commands = get_commands()
    root = Directory("/")
    run_commands(commands, root)
    print(root.find_matching_size())
    find_min_dir_to_remove(root)


if __name__ == "__main__":
    main()
