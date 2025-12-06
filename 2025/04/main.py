def get_adjacent(toilet_map, x, y):
    adjacent = []
    toilet_map_width = len(toilet_map[0]) - 1
    toilet_map_height = len(toilet_map) - 1
    if x > 0 and y > 0:
        adjacent.append(toilet_map[y-1][x-1])
    if y > 0:
        adjacent.append(toilet_map[y-1][x])
    if x < toilet_map_width and y > 0:
        adjacent.append(toilet_map[y-1][x+1])
    if x > 0:
        adjacent.append(toilet_map[y][x-1])
    if x < toilet_map_width:
        adjacent.append(toilet_map[y][x+1])
    if x > 0 and y < toilet_map_height:
        adjacent.append(toilet_map[y+1][x-1])
    if y < toilet_map_height:
        adjacent.append(toilet_map[y+1][x])
    if x < toilet_map_width and y < toilet_map_height:
        adjacent.append(toilet_map[y+1][x+1])
    return adjacent

def update_toilet_map(toilet_map, removed_map):
    for y in range(len(toilet_map)):
        new_row = ""
        for x in range(len(toilet_map[0])):
            if removed_map[y][x]:
                new_row += '.'
            else:
                new_row += toilet_map[y][x]
        toilet_map[y] = new_row

def forklift(toilet_map):
    forklifted = 0
    removed_map = []
    for y in range(len(toilet_map)):
        removed_map.append([False]*len(toilet_map[y]))
        for x in range(len(toilet_map[0])):
            if toilet_map[y][x] != '@':
                continue
            adjacent = get_adjacent(toilet_map, x, y)
            tp_count = adjacent.count('@')
            can_be_forklifted = tp_count < 4
            if can_be_forklifted:
                forklifted += 1
                removed_map[y][x] = True
    return forklifted, removed_map


def main():
    input = None
    with open("input.txt", "r") as f:
        input = f.read()
    
    toilet_map = input.split("\n")
    toilet_map.pop()
    tp_forklifted, removed_map = forklift(toilet_map)
    update_toilet_map(toilet_map, removed_map)
    print(f"Forklifted: {tp_forklifted}")
    while True:
        forklifted, removed_map = forklift(toilet_map)
        if forklifted <= 0:
            break
        tp_forklifted += forklifted
        update_toilet_map(toilet_map, removed_map)
    print(f"Forklifted: {tp_forklifted}")

if __name__ == "__main__":
    main()
