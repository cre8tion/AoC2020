def find_manhattan_dist():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        instruction_lst = [[i[:1][0], "".join(i[1:])] for i in text_lst]

        # Initialise variables
        facing = "E"
        cood = [0, 0]
        turning = ["L", "R"]
        
        for i in instruction_lst:
            action = i[0]
            value = int(i[1])

            # Change the facing position of the ship
            if action in turning:
                facing = change_facing_pos(facing, action, value)

            # Setting the action as the facing direction
            elif action == "F":
                action = facing
            
            # Moving the ship into the direction of the action
            if action == "N":
                cood[1] += value
            
            elif action == "S":
                cood[1] -= value
            
            elif action == "W":
                cood[0] -= value
            
            elif action == "E":
                cood[0] += value
        
        # Calculating manhattan distance
        dist = abs(cood[0])+ abs(cood[1])
        return dist

def change_facing_pos(facing, action, value):
    # List in clockwise order
    direction_lst = ["N", "E", "S", "W"]
    # Indexes to rotate
    value /= 90

    # Rotate in reverse direction if turning left
    if action == "L":
        value = -value

    # Finding new index after rotation
    direction_idx = direction_lst.index(facing)
    direction_idx = (direction_idx + value) % 4

    # Returning new direction after rotation
    return direction_lst[direction_idx]

manhattan_dist = find_manhattan_dist()
print(manhattan_dist)