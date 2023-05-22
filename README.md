# Markov Decision Process - Pathfinding Algorithm for Autonomous Drone



### Scenario
Given an nxn map with empty, start, goal, and hazard positions, find the utility (value) and the optimal move (policy) at each position. A drone uses this information to delivery its payload to the goal position, beginning at the start position. Additionally, the drone can fly North, South, East, West and can use an extra propulsion system, requiring two times as much battery power, to counteract the force of the wind. When the drone is traveling at a normal speed, there is a 70% chance that the drone moves in the desired direction and a 30% chance the drone flies sideways (15% chance for each side). When the drone is utilizing the extra proulsion system, there is an 80% chance the drone moves in the desired direction a 20% chance the drone flies sideways (10% chance for each side). Finally, if the drone flies over a hazardous position, then the drone crashes, and a negative utility of the drone repair cost is received.

### Approach
- **Markov Decision Process:**
  - Set of States s ∈ S
  - Set of Actions a ∈ A
  - Transition Function T(s, a, s’)
       - Probability that a from s leads to s’, i.e., P(s’| s, a)
       - Also called the model or the dynamics
  - Reward Function R(s, a, s’)
  - Start State
  - Terminal State (0.1% Convergence)
- **Value Iteration:**
  - Given a vector of values V<sub>k</sub>(s), run one iteration of expectimax on the state and repeat until convergence
  - **Basic Idea:** approximations get refined towards optimal values and policies general converge far before the values
  - <img src="[https://user-images.githubusercontent.com/link-to-your-image.png](https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/cc84e23f-fa0a-4384-a86b-05783f4efadb)" />



