from functools import reduce

def process_input(input:str):
    input_map = []
    lines = [i for i in input.split("\n") if i]
    for line in lines:
        clean_data = [i for i in line.split(" ") if i]
        input_map.append(clean_data)
    operators = input_map.pop()

    return input_map, operators

def get_col_width_per_operator(operator_str):
    curr_size = 1
    sizes = []
    for i in range(1, len(operator_str)):
        if operator_str[i] != " ":
            sizes.append(curr_size-1)
            curr_size = 0
        curr_size += 1
    sizes.append(curr_size)
    return sizes

def slice_line_by_size(line, sizes):
    sliced = []
    for size in sizes:
        slice = line[:size]
        sliced.append(slice)
        line = line[size+1:]
    return sliced

def process_input_cephalod(input:str):
    lines = [i for i in input.split("\n") if i]
    transposed = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]
    return transposed


def do_operation(operator, values):
    if not values:
        return 0
    values = [i for i in values if i.strip()]
    if operator == "+":
        return reduce(lambda a, b: int(a) + int(b), values)
    if operator == "*":
        return reduce(lambda a, b: int(a) * int(b), values)
    raise Exception("No known operator.")

def calculate(input: str):
    input_map, operators = process_input(input)
    sum = 0
    for x in range(len(input_map[0])):
        final_value = 0
        op = operators[x]
        values = []
        for y in input_map:
            values.append(y[x])
        final_value = do_operation(op, values)
        sum += final_value
    return sum
        
def calculate_cephalod(input: str):
    input_map = process_input_cephalod(input)
    sum = 0
    prev_op = " "
    values = []
    for i in range(len(input_map)):
        op = input_map[i][-1]
        if op == "*" or op == "+":
            sum += do_operation(prev_op, values)
            prev_op = op
            values = ["".join(input_map[i][:-1])]
        else:
            values.append("".join(input_map[i][:-1]))
    sum += do_operation(prev_op, values)
    return sum

def main() -> None:
    input = None
    with open("input.txt", "r") as f:
        input = f.read()

    solution = calculate(input)
    print(f"Solution: {solution}")

    solution = calculate_cephalod(input)
    print(f"Solution 2: {solution}")

if __name__ == "__main__":
    main()
