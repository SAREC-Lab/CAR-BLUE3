# Car - Blue 3

## Project 02

### Traceability
#### Requirements
R1: Map out the required area (in this case, a portion of the 2nd floor of Stinson-Remick) manually using the MUSHR car </br>
R2: Using the map, get the car to autonomously drive from one point on the map to another </br>

#### Design Definitions
D1: Connect a controller to the car in order to drive it manually </br>
D2: Drive the car with LIDAR on to create a map of the area </br>
D3: Use the map to analyze the area around the car </br>
D4: Get the car to move based on the noise around it </br>

#### Trace Matrix
R1, D1 </br>
R1, D2 </br>
R2, D3 </br>
R2, D4 </br>

D1, no files assocaited </br>
D2, (map files) </br>
D3, (drive file, map files) </br>
D4, (drive file, map files) </br>

### Testing

To start, we got the PS4 controller linked to our MUSHR car, allowing us to drive it manually; once that was enabled, we drove it around the classroom with LIDAR enabled in order to check if it could detect hazards around it. In doing so, we figured out that any hazards that were either too thin or above/below the LIDAR (i.e. the chairs around the room) were not properly detected; knowing this, we took it into the hallway to build our map. </br>
Since the hallway had no hazards and was otherwise just a series of walls, we used it as our ‘maze’ for this project. While testing, we found that the LIDAR could pick up (with a bit more time to process) the railing overlooking the main atrium, but could not properly pick up the glass barriers separating some of the side rooms. Still, we navigated it around the hallways enough to generate a proper map for later usage. </br>
After cleaning up the map by adding some more defined walls in unmapped areas (i.e. at forks or at the staircase), we tested usage of the map within the simulator. At this point, we hit a wall; technical issues with the car kept us from being able to proceed any further. We attempted to use a program that took in any points of noise to determine the best direction for the car to move in then direct it that way, but the simulator was either virtually unusable, or the LIDAR would not return any points of data beyond the initial set. 

#Comments: Without a demo, there are definitely no ways of assessing if the solution is right but the approach looks good, given all the effort and constraints, no points are deducted. Grade: 100/100

