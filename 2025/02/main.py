from collections import namedtuple
from typing import List

import sys


Range = namedtuple("Range", ["lower", "upper"])


def is_invalid_id(number_string: str) -> bool:
    max_length_or_rep = len(number_string) // 2
    left = number_string[:max_length_or_rep]
    right = number_string[max_length_or_rep:]
    return left == right


def get_invalid_ids_in_range(id_range: Range) -> List[int | None]:
    invalid_ids = []
    for i in range(int(id_range.lower), int(id_range.upper) + 1):
        i_str = str(i)
        if is_invalid_id(i_str):
            invalid_ids.append(i)

    return invalid_ids


def is_invalid_id_part_2(number_string: str) -> bool:
    if is_invalid_id(number_string):
        return True

    max_length_or_rep = len(number_string) // 2
    for chunk_size in range(1, max_length_or_rep + 1):
        if len(number_string) % chunk_size == 0:
            chunks = [
                number_string[i : i + chunk_size]
                for i in range(0, len(number_string), chunk_size)
            ]
            first_element = chunks[0]
            all_same = all(element == first_element for element in chunks)
            if all_same:
                return True

    return False


def get_invalid_ids_in_range_part_2(id_range: Range) -> List[int | None]:
    invalid_ids = []
    for i in range(int(id_range.lower), int(id_range.upper) + 1):
        i_str = str(i)
        if is_invalid_id_part_2(i_str):
            invalid_ids.append(i)

    return invalid_ids


def get_ranges(ranges: str) -> List[Range]:
    return [Range(*range.split("-")) for range in ranges.split(",")]


def part_1():
    product_id_ranges_str = input("Enter range:")
    id_ranges = get_ranges(product_id_ranges_str)

    invalid_ids = []
    for id_range in id_ranges:
        invalid_ids_in_range = get_invalid_ids_in_range(id_range)
        invalid_ids.extend(invalid_ids_in_range)

    print(invalid_ids)

    print(f"Sum: {sum(invalid_ids)}")


def get_invalid_ids(id_ranges, func):
    invalid_ids = []
    for id_range in id_ranges:
        invalid_ids_in_range = func(id_range)
        invalid_ids.extend(invalid_ids_in_range)

    return invalid_ids


def main(args):
    product_id_ranges_str = input("Enter range:")
    id_ranges = get_ranges(product_id_ranges_str)
    invalid_ids = []

    if len(args) > 1 and args[1] == "2":
        print("Part 2:")
        invalid_ids = get_invalid_ids(id_ranges, get_invalid_ids_in_range_part_2)
    else:
        print("Part 1:")
        invalid_ids = get_invalid_ids(id_ranges, get_invalid_ids_in_range)

    print(invalid_ids)
    print(f"Sum: {sum(invalid_ids)}")


if __name__ == "__main__":
    args = sys.argv
    main(args)
