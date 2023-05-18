# direction_probability * (-1*power_cost + (discount * values[y][x]))
# direction_probability * (-2*power_cost + (discount * values[y][x]))

# Tie-Breaking Rules:
# normal speed, boosted speed
# south, west, north, east


def copy_values(values, n):
    new = [[0 for j in range(6)] for i in range(n)]
    for y in range(n):
        for x in range(n):
            new[y][x] = values[y][x]
    return new


def converges(prev, curr):
    for y in range(n):
        for x in range(n):
            if abs(prev[y][x] - curr[y][x]) > 0.001:
                return False
    return True


def calc_next_moves(curr_posn, values, policies, power_cost, discount, size):
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

    curr_val = values[curr_posn[0]][curr_posn[1]]
    moves = [s, w, n, e, ss, ww, nn, ee]
    max_val = max(moves)
    max_move = moves.index(max_val)

    values[curr_posn[0]][curr_posn[1]] = max_val
    policies[curr_posn[0]][curr_posn[1]] = max_move+1


# map : 6x6 
def robot_travel_planner(map, policies, values, delivery_price, power_cost, robotrepair_cost, discount, n):
    # Find Start, Goal, & Hazard Positions
    prev = copy_values(values, n)
    start = ()
    goal = ()
    rivals = []
    for y in range(n):
        for x in range(n):
            if map[y][x] == 1:
                start = (y, x)
            if map[y][x] == 2:
                goal = (y, x)
            if map[y][x] == 3:
                rivals.append((y, x))

    # Initialize Values with Rewards at Goal & Hazard Positions
    values[goal[0]][goal[1]] = delivery_price
    for r in rivals:
        values[r[0]][r[1]] = robotrepair_cost*-1
        
    # Loop Until Board Converges
    while True:
        for y in range(6):
            for x in range(6):
                curr_posn = (y, x)  
                if (curr_posn != goal) and (curr_posn not in rivals):
                    calc_next_moves(curr_posn, values,                  # Calculate the next moves for positions...
                                    policies, power_cost, discount, n)     # ...that are not goal or hazard positions
        if converges(prev, values):         # Stop looping and return if board converges
            break
        else:                               # Else, continue looping and keep track of previous values 2D Array
            prev = copy_values(values, n)

    return values[start[0]][start[1]]
