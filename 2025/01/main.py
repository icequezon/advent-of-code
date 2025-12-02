from typing import List


class Node:
    def __init__(self, left=None, right=None, value: int = 0):
        self.left = left
        self.right = right
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)


def create_dial(starting_number):
    zero = Node(None, None, 0)
    dial = None
    starting_dial = None

    if starting_number == 0:
        starting_dial = zero
    else:
        starting_dial = Node(None, None, starting_number)

    dial = starting_dial

    for _ in range(0, 99):
        if dial.value == 99:
            dial.right = zero
            zero.left = dial
            dial = dial.right
            continue

        if dial.right == None:
            dial.right = Node(dial, None, dial.value + 1)
            dial = dial.right

    dial.right = starting_dial
    starting_dial.left = dial

    return dial.right, zero


def move_dial(action, dial):
    if not action:
        return
    direction = action[0]
    number = int(action[1:])
    for _ in range(0, number):
        if direction == "L":
            dial = dial.left
        else:
            dial = dial.right
    return dial


def move_dial_method_0x434C49434B(action, dial, zero):
    count = 0
    if not action:
        return dial, 0
    direction = action[0]
    number = int(action[1:])
    for _ in range(0, number):
        if dial is zero:
            count += 1
        if direction == "L":
            dial = dial.left
        else:
            dial = dial.right
    return dial, count


def get_password(actions: List[str]) -> int:
    password = 0
    dial, zero = create_dial(50)
    curr_dial = dial
    for action in actions:
        curr_dial = move_dial(action, curr_dial)
        print(f"{action} to point to {curr_dial}")
        if curr_dial is zero:
            password += 1

    return password


def get_password_method_0x434C49434B(actions: List[str]) -> int:
    password = 0
    dial, zero = create_dial(50)
    curr_dial = dial
    for action in actions:
        curr_dial, count = move_dial_method_0x434C49434B(action, curr_dial, zero)
        print(f"{action} to point to {curr_dial}")
        password += count

    return password


def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read()

    # password = get_password(input.split("\n"))
    password = get_password_method_0x434C49434B(input.split("\n"))
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
