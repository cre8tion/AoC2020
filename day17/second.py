# NGL Adapted solution

from itertools import product

def conway_cubes(dimension):
    p = dimension - 2

    def simulate(coord):
        # Finding nearby permutations to this coordinate 
        nearby_permutations = [range(a-1, a+2) for a in coord]
        
        # Generate nearby coordinates
        nearby_coordinates = product(*nearby_permutations)

        # Number of active cubes near this coordinate
        n = len(active_cubes & set(nearby_coordinates))

        # If n == 4 or 3 (including this coord), and this coord already active, this coord is active next cycle
        # Likewise, if 3 neighbours is active, this coord is active as well
        return (coord in active_cubes and n == 4) or (n == 3)

    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]

        # Set of coordinates for cubes in active state
        active_cubes = {(x,y) + (0,) * p for x,line in enumerate(text_lst) for y,char in enumerate(line) if char == '#'}

        # 6 Cycles
        for cycle in range(6):
            # Expanding pocket dimension in each cycle
            all_coords = product(range(-cycle-1, cycle+8), repeat=2+p)
            # Simulate transition in each cycle
            active_cubes = set(filter(simulate, all_coords))

        return len(active_cubes)


error_rate = conway_cubes(4)
print(error_rate)