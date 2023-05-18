


# Tie-Breaking Rules:
# normal speed, boosted speed
# south, west, north, east

# Copies values from one nxn matrix to another, in order to prevent copying by reference
def copy_values(values, size):
    new = [[0 for j in range(6)] for i in range(size)]
    for y in range(size):
        for x in range(size):
            new[y][x] = values[y][x]
    return new

# Checks to see if the previous and current value boards converge by a factor of 0.1%
def converges(prev, curr, size):
    for y in range(size):
        for x in range(size):
            if abs(prev[y][x] - curr[y][x]) > 0.001:
                return False
    return True

# Calculates the next possible 8 moves and then sets values to the max of that move and policies to the direction of the max move
def calc_next_moves(curr_posn, values, policies, power_cost, discount, size):
    # Determine if neighboring positions are in range of the map
    s_range = True
    w_range = True
    n_range = True
    e_range = True

    if curr_posn[0]+1 > (size-1):
        s_range = False
    if curr_posn[1]-1 < 0:
        w_range = False
    if curr_posn[0]-1 < 0:
        n_range = False
    if curr_posn[1]+1 > (size-1):
        e_range = False

    # Based on if the neighboring positions are in range, calculate the viable neighboring positions
    s_posn = ()
    w_posn = ()
    n_posn = ()
    e_posn = ()

    if s_range:
        s_posn = (curr_posn[0]+1, curr_posn[1])
    else:
        s_posn = curr_posn

    if w_range:
        w_posn = (curr_posn[0], curr_posn[1]-1)
    else:
        w_posn = curr_posn

    if n_range:
        n_posn = (curr_posn[0]-1, curr_posn[1])
    else:
        n_posn = curr_posn

    if e_range:
        e_posn = (curr_posn[0], curr_posn[1]+1)
    else:
        e_posn = curr_posn

    # Calculate the utility at all neighboring positons while using no speed boost
    # direction_probability * (-1 * power_cost + (discount * values[next[y]][next[x]]))
    s = (0.7 * (-1 * power_cost + (discount * values[s_posn[0]][s_posn[1]]))) + \
        (0.15 * (-1 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.15 * (-1 * power_cost +
         (discount * values[e_posn[0]][e_posn[1]])))

    w = (0.7 * (-1 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.15 * (-1 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.15 * (-1 * power_cost +
         (discount * values[s_posn[0]][s_posn[1]])))

    n = (0.7 * (-1 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.15 * (-1 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.15 * (-1 * power_cost +
         (discount * values[e_posn[0]][e_posn[1]])))

    e = (0.7 * (-1 * power_cost + (discount * values[e_posn[0]][e_posn[1]]))) + \
        (0.15 * (-1 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.15 * (-1 * power_cost +
         (discount * values[s_posn[0]][s_posn[1]])))

    # Calculate the utility at all neighboring positions while using speed boost
    # direction_probability * (-2 * power_cost + (discount * values[next[y]][next[x]]))
    ss = (0.8 * (-2 * power_cost + (discount * values[s_posn[0]][s_posn[1]]))) + \
        (0.1 * (-2 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.1 * (-2 * power_cost +
         (discount * values[e_posn[0]][e_posn[1]])))

    ww = (0.8 * (-2 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.1 * (-2 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.1 * (-2 * power_cost +
         (discount * values[s_posn[0]][s_posn[1]])))

    nn = (0.8 * (-2 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.1 * (-2 * power_cost + (discount * values[w_posn[0]][w_posn[1]]))) + \
        (0.1 * (-2 * power_cost +
         (discount * values[e_posn[0]][e_posn[1]])))

    ee = (0.8 * (-2 * power_cost + (discount * values[e_posn[0]][e_posn[1]]))) + \
        (0.1 * (-2 * power_cost + (discount * values[n_posn[0]][n_posn[1]]))) + \
        (0.1 * (-2 * power_cost +
         (discount * values[s_posn[0]][s_posn[1]])))
        
    # Add all possible 8 moves to an list and find the move with the maximum utility
    moves = [s, w, n, e, ss, ww, nn, ee]
    max_val = max(moves)
    max_move = moves.index(max_val)

    # Set values at the current position to the maximum move value and policies at the current position to the maximum move direction
    values[curr_posn[0]][curr_posn[1]] = max_val
    policies[curr_posn[0]][curr_posn[1]] = max_move+1


# map : nxn matrix containing the positions of the start, goal, and hazard positions (denoted with 1,2,3 respectively)
# policies : empty nxn matrix that is updated with the best possible move after the function call
# values : empty nxn matrix that is updated with the utility value at each position on the board after the function call
# delivery_price : the utility earned for completing the robot delivery
# power_cost : the cost of power by the robot at each step
# robot_repair_cost : the negative utility that is earned when the robot ends up in a hazardous position
# discount : the discount at each step in the operation (gamma value)
# size : the n value for the nxn matrices provided by map, policies, and values
# --> returns the utility value at the start position
def robot_travel_planner(map, policies, values, delivery_price, power_cost, robot_repair_cost, discount, size):
    # Find Start, Goal, & Hazard Positions
    prev = copy_values(values, size)
    start = ()
    goal = ()
    rivals = []
    for y in range(size):
        for x in range(size):
            if map[y][x] == 1:
                start = (y, x)
            if map[y][x] == 2:
                goal = (y, x)
            if map[y][x] == 3:
                rivals.append((y, x))

    # Initialize Values with Rewards at Goal & Hazard Positions
    values[goal[0]][goal[1]] = delivery_price
    for r in rivals:
        values[r[0]][r[1]] = robot_repair_cost*-1
        
    # Loop Until Board Converges
    while True:
        for y in range(6):
            for x in range(6):
                curr_posn = (y, x)  
                if (curr_posn != goal) and (curr_posn not in rivals):
                    calc_next_moves(curr_posn, values,                  # Calculate the next moves for positions...
                                    policies, power_cost, discount, size)     # ...that are not goal or hazard positions
        if converges(prev, values, size):         # Stop looping and return if board converges
            break
        else:                               # Else, continue looping and keep track of previous values nxn matrix
            prev = copy_values(values, size)

    return values[start[0]][start[1]]   # Returns utility values at the start position
