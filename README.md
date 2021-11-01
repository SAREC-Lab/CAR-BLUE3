# Car - Blue 3

## Project 02

### Traceability
#### Requirements
R1: Map out the required area (in this case, a portion of the 2nd floor of Stinson-Remick) manually using the MUSHR car </br>
R2: Using the map, get the car to autonomously drive from one point on the map to another </br>

#### Design Definitions
D1: Use RVis to 

#### Trace Matrix
R1, D1 </br>
R1, D2 </br>
R2, D3 </br>
R2, D4 </br>

D1, (file) </br>
D2, (file) </br>
D3, (file) </br>
D4, (file) </br>

### Testing

To start, we got the PS4 controller linked to our MUSHR car, allowing us to drive it manually; once that was enabled, we drove it around the classroom with LIDAR enabled in order to check if it could detect hazards around it. In doing so, we figured out that any hazards that were either too thin or above/below the LIDAR (i.e. the chairs around the room) were not properly detected; knowing this, we took it into the hallway to build our map. </br>
Since the hallway had no hazards and was otherwise just a series of walls, we used it as our ‘maze’ for this project. While testing, we found that the LIDAR could pick up (with a bit more time to process) the railing overlooking the main atrium, but could not properly pick up the glass barriers separating some of the side rooms. Still, we navigated it around the hallways enough to generate a proper map for later usage. </br>
After cleaning up the map by adding some more defined walls in unmapped areas (i.e. at forks or at the staircase), we tested usage of the map within the simulator. 
