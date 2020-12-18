def find_manhattan_dist():
    with open('input.txt') as fin:
        input_list = fin.readlines()
        text_lst = [i.replace("\n", "") for i in input_list]
        instruction_lst = [[i[:1][0], "".join(i[1:])] for i in text_lst]

        # Initialise variables
        waypoint = {"E": 10, "N": 1, "S": 0, "W": 0}
        cood = [0, 0]
        turning = ["L", "R"]
        movement = ["N", "S", "E", "W"]
        
        for i in instruction_lst:
            action = i[0]
            value = int(i[1])

            # Rotate the waypoint
            if action in turning:
                waypoint = rotate_waypoint(waypoint, action, value)

            # Move the ship with respect to the waypoint
            elif action == "F":
                for i in waypoint.keys():
                    cood = advance_waypoint(i, cood, waypoint[i], value)
            
            # Move the waypoint in the direction of action
            elif action in movement:
                waypoint = move_waypoint(waypoint, action, value)

        # Calculating manhattan distance
        dist = abs(cood[0])+ abs(cood[1])
        return dist

def move_waypoint(waypoint, action, value):
    waypoint[action] += value
    return waypoint

def advance_waypoint(action, coordinate, value, multiplier):
    # Advance the ship based on waypoint and mulitpler
    if action == "N":
        coordinate[1] += (value * multiplier)
            
    elif action == "S":
        coordinate[1] -= (value * multiplier)
            
    elif action == "W":
        coordinate[0] -= (value * multiplier)
            
    elif action == "E":
        coordinate[0] += (value * multiplier)
    
    return coordinate

def rotate_waypoint(waypoint, action, value):
    # List in clockwise order
    direction_lst = ["N", "E", "S", "W"]
    # Indexes to rotate
    value /= 90

    new_waypoint = {}
    
    # Rotate in reverse direction if turning left
    if action == "L":
        value = -value

    # Rotating the waypoint
    for direction in waypoint.keys():
        direction_idx = direction_lst.index(direction)
        direction_idx = (direction_idx + value) % 4
        new_direction = direction_lst[direction_idx]
        new_waypoint[new_direction] = waypoint[direction]
    
    return new_waypoint


manhattan_dist = find_manhattan_dist()
print(manhattan_dist)