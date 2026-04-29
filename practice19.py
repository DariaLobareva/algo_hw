def place_towers(houses, radius=4):
    towers = []
    for house in sorted(houses):
        if not towers or house > towers[-1] + radius:
            towers.append(house + radius)
    return towers
 

houses = [1, 5, 10, 14, 17, 25, 30, 35]
towers = place_towers(houses)
print(len(towers), towers)