# Markov Decision Process - Pathfinding Algorithm for Autonomous Drone



### Scenario
Given an nxn map with empty, start, goal, and hazard positions (denoted with 0, 1, 2, & 3 respectively), find the utility (value) and the optimal move (policy) at each position. A drone uses this information to delivery its payload to the goal position, beginning at the start position. Additionally, the drone can fly North, South, East, West and can use an extra propulsion system, requiring two times as much battery power, to counteract the force of the wind. When the drone is traveling at a normal speed, there is a 70% chance that the drone moves in the desired direction and a 30% chance the drone flies sideways (15% chance for each side). When the drone is utilizing the extra proulsion system, there is an 80% chance the drone moves in the desired direction a 20% chance the drone flies sideways (10% chance for each side).
