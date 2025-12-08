def count_fresh(ingredients_ranges):
    count = 0
    sorted_ingredients = sorted(ingredients_ranges, key=lambda pair: (int(pair.split('-')[0]), int(pair.split('-')[1])))
    start, end = map(lambda x: int(x), sorted_ingredients[0].split("-"))

    for x in range(1, len(sorted_ingredients)):
        """
        num_in_range = (int_ranges[1] - int_ranges[0]) + 1
        count += num_in_range
        if prev_min_max and is_fresh([prev_min_max], sorted_ingredient.split('-')[0]):
             diff = int(prev_min_max.split('-')[1]) - int_ranges[0] + 1
             count -= diff
        prev_min_max = sorted_ingredient
        """
        sorted_ingredient = sorted_ingredients[x]
        #print(sorted_ingredient)
        curr_min, curr_max = list(map(lambda x: int(x), sorted_ingredient.split('-')))
        # 1 - 10 start end
        # 2 - 5 curr_min, curr_max
        # 4 - 11
        # 12 - 15
        if curr_min <= end:
            if curr_max >= end:
                end = curr_max
        else:
            count += (end - start) + 1
            start = curr_min
            end = curr_max
        print(start, end, count)

    count += (end-start)+1
    return count

def is_fresh(ingredients_ranges, ingredient):
    for ingredients_range in ingredients_ranges:
        min_s, max_s = ingredients_range.split("-")
        min = int(min_s)
        max = int(max_s)
        ingredient_num = int(ingredient)
        if ingredient_num >= min and ingredient_num <= max:
            return True
    return False


def process_database(input:str):
    lines = input.split("\n")
    lines.pop()
    ingredients_range = []
    ingredients = []
    is_already_ingredient = False
    for line in lines:
        if line == "":
            is_already_ingredient = True
            continue
        if is_already_ingredient:
            ingredients.append(line)
            continue
        ingredients_range.append(line)

    return ingredients_range, ingredients


def main():
    input_data = None
    with open("input.txt", "r") as f:
        input_data = f.read()

    ingredients_range, ingredients = process_database(input_data)
    count = 0
    for ingredient in ingredients:
        if is_fresh(ingredients_range, ingredient):
            count += 1
    print(f"Fresh ingredients: {count}")

    count = count_fresh(ingredients_range)
    print(f"All Fresh ingredients from range: {count}")
    

if __name__ == "__main__":
    main()
