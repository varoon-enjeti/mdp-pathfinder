# Markov Decision Process - Pathfinding Algorithm for Autonomous Drone

### Scenario:
Given an nxn map with empty, start, goal, and hazard positions, find the utility (value) and the optimal move (policy) at each position. A drone uses this information to delivery its payload to the goal position, beginning at the start position. Additionally, the drone can fly North, South, East, West and can use an extra propulsion system, requiring two times as much battery power, to counteract the force of the wind. When the drone is traveling at a normal speed, there is a 70% chance that the drone moves in the desired direction and a 30% chance the drone flies sideways (15% chance for each side). When the drone is utilizing the extra proulsion system, there is an 80% chance the drone moves in the desired direction a 20% chance the drone flies sideways (10% chance for each side). Finally, if the drone flies over a hazardous position, then the drone crashes, and a negative utility of the drone repair cost is received.

### Approach:
- **Markov Decision Process:**
  - Set of States s ∈ S
  - Set of Actions a ∈ A
  - Transition Function T(s, a, s’)
       - Probability that a from s leads to s’, i.e., P(s’| s, a)
       - Also called the model or the dynamics
  - Reward Function R(s, a, s’)
  - Start State
  - Terminal State (0.1% Convergence)
- **Reinforcement Learning - Value Iteration:**
  - Given a vector of values V<sub>k</sub>(s), run one iteration of expectimax on the state and repeat until convergence
  - **Basic Idea:** approximations get refined towards optimal values and policies general converge far before the values
  - <img width="500" src="https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/0262239c-d97b-4ebd-800d-38d2f6637910">

### Demo (6x6 Grid):
**Map:**
<br>
<img width="200" alt="map" src="https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/a973afcf-bc03-4f69-b7eb-bff9528d9423">
<br>
**Value Iteration - Reinforcement Learning:**
<br>
![](https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/6d159966-b3cf-429d-96e1-b9e0f3789dce)
https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/6d159966-b3cf-429d-96e1-b9e0f3789dce
<br>
**Policies:**
<br>
![](https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/964d3711-7024-49e2-bb66-4f5ba79f95bb)













