## Use Case: Deliver Materials 

**ID**: 001

**Description**: The main turtlebot leads transport vehicles to deliver
materials. 

**Primary Actor(s)**: Main turtlebot

**Supporting Actor(s)**: Autonomous transport vehicles 

**Pre-Conditions**:

- Transport vehicles have materials loaded. 
- Main turtlebot system is active. 
- Transport vehicle systems are active. 

**Post-Conditions**:

- Success: The materials are delivered to the GPS location. 
- Failure: The GPS location is not reached or the materials are lost. 

**Trigger**: The main turtlebot receives the GPS location. 

### Success Story
1. All the vehicles are active and the materials are loaded. 
2. The main turtlebot receives the GPS location. 
3. The main turtlebot begins moving and scanning for obstacles with the LiDAR
   system. 
4. The autonomous transport vehicles move behind the main turtlebot. 
5. The vehicles reach the GPS location specified. 
6. The materials are unloaded by those requesting them. 
