from typing import List


def get_banks(input:str) -> List[str]:
    return input.split("\n")


def get_max_joltage_per_bank(bank: str) -> int:
    max = list(bank[:2])
    for idx in range(2 , len(bank)):
        c = bank[idx]
        i = int(c)
        if i >= int(max[1]):
            max[1] = c
        if (int(max[1]) > int(max[0])) and idx < len(bank) - 1:
            max[0] = max[1]
            max[1] = bank[idx+1]
    
    return int("".join(max))


def get_max_joltage_per_bank_with_batt_length(bank: str, batt_length: int) -> int:
    max_joltage = ["0"] * batt_length
    bank_len = len(bank)
    for idx in range(0, bank_len):
        c = bank[idx]
        i = int(c)
        max_jolt_len = len(max_joltage)
        for max_jolt_diff in range(0, max_jolt_len):
            max_jolt_idx = (max_jolt_len-1) - max_jolt_diff
            if i > int(max_joltage[max_jolt_idx]) and max_jolt_diff < (bank_len - idx):
                max_joltage[max_jolt_idx] = c
                if max_jolt_diff > 0:
                    max_joltage[max_jolt_idx+1] = "0"

    return int("".join(max_joltage))


def get_maximum_joltage(banks: List[str], batt_length=2) -> int:
    max = 0
    for bank in banks:
        if not bank:
            continue
        max_in_bank = get_max_joltage_per_bank_with_batt_length(bank, batt_length)
        max += max_in_bank
    return max


def main():
    input = ""
    with open("input.txt") as f:
        input = f.read()
    banks = get_banks(input)

    part_1_max = get_maximum_joltage(banks, 2)
    print(f"Part 1 Answer: {part_1_max}")
    part_2_max = get_maximum_joltage(banks, 12)
    print(f"Part 2 Answer: {part_2_max}")


if __name__ == "__main__":
    main()
