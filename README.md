# Markov Decision Process - Reinforcement Learning Algorithm for Autonomous Drone

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
  - <img width="500" src="https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/db3f7b1d-2090-41d7-9590-ac318efb7951">

### Demo (6x6 Grid):
**Map:**
<br>
<img width="200" alt="map" src="https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/b2d5506c-8855-4bd9-b240-49154bf98161">
<br>
**Value Iteration - Reinforcement Learning:**
<br>  


https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/51a81d89-79ce-412f-b691-356575b8e39b



**Policies:**
<br>


https://github.com/varoon-enjeti/mdp-pathfinder/assets/97761722/8ed820d0-f9cd-49f3-8ab7-e7522f75e923



### Legend:
- **Map:**
  - **0:** Empty Position
  - **1:** Start Position
  - **2:** Goal Position
  - **3:** Hazard Position
- **Actions:**
  - **0:** No Move
  - **1:** South with Special Propulsion OFF
  - **2:** West with Special Propulsion OFF
  - **3:** North with Special Propulsion OFF
  - **4:** East with Special Propulsion OFF
  - **5:** South with Special Propulsion ON
  - **6:** West with Special Propulsion ON
  - **7:** North with Special Propulsion ON
  - **8:** East with Special Propulsion ON













