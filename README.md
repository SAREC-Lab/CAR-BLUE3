# Follow the Leader

### Important Links
[Github Repository](https://github.com/SAREC-Lab/CAR-BLUE3/tree/main) <br />
[Trello Board](https://trello.com/b/wCxuc2UZ/main-project) <br />

## Vision Statement
Follow the Leader uses a **main turtlebot** to guide other **autonomous vehicles**. The **main turtlebot** moves toward a **GPS location** sent to it from the user using a simple application. The **main turtlebot** then begins to move toward that direction, navigating with **LiDAR** technology to avoid obstacles. The other **autonomous vehicles** follow the **main turtlebot** after it has determined how to avoid the obstacles ahead. Usage examples include delivering materials with large **autonomous vehicles** that follow the guidance of the **main turtlebot**.

## Glossary
- Main Turtlebot: the turtlebot that will use LiDAR to lead the other
  autonomous vehicles; the main turtlebot is powered by ROS
- Autonomous Vehicle: a vehicle that is powered not by human action but by
  following the **main turtlebot**
- GPS Location: the coordinates on Earth based on satellites of the desired
  location to travel to 
- LiDAR: Light Detection and Ranging is a remote sensing method that uses
  pulsing lasers to measure ranges to objects around

## Requirements/Plan
1. Main turtlebot and autonomous vehicle will start lined up, turtlebot in front
2. User will send a set of X, Y coordinates (in meters) to the main turtlebot
3. Main turtlebot will navigate to the GPS Location using LiDAR
4. Using the main turtlebot's path, the autonomous vehicle will navigate to the GPS position where the main turtlebot finished

## Design/Architecture
Our project has four primary files: **main.py**, **nav.py**, **follow.py**, and **utils.py**.
- **main.py** constructs the primary UI for the project, presenting it to the user (for example, see *Interface* below). Data from main.py is published and subsequently passed into nav.py.
- **nav.py** controls the turtlebot. Taking the input from main.py, the program makes the base assumption that the turtlebot is at (0, 0) facing along the positive X-axis. Using ROS, it moves the turtlebot forward until either it reaches the appropriate X-coordinate, or hits an obstacle. In either case, it turns to face along the Y-axis once it reaches a stopping point, and proceeds to attempt to reach the Y-coordinate, until one of the aforementioned scenarios happens with the Y-coordinate. Along the way, it crafts a series of commands for the car to drive or turn, ultimately sending the plan to the car.
- **follow.py** controls the car. Taking the plan from nav.py, the car (roughly) follows along the turtlebot's path, using the plan given until it runs out of commands.
- **utils.py** contains the specifics of the drive commands for the car.

## Testing
Testing had a few main components: basic functionality, movement, communication, and detection. <br />
- *Basic functionality* focused on making sure we could parse inputs properly, and that the code itself didn't have any issues. Primarily, this involved the construction of the task plan for the car via the turtlebot's pathing, which we had to make multiple attempts at figuring out proper parameters for.<br />
- *Movement* focused on making sure both the turtlebot and car could move properly. We had experience with the car prior to the project, but none with the turtlebot. After learning how to make the turtlebot move properly, and doing some more specific measurements on the car's movement, particularly its turns, we moved on to communication.<br />
- *Communication* focused on getting instructions from the turtlebot to the car. We thought about a few different possibilities for this, before settling on a state machine-like task plan the turtlebot would build before sending the process to the car to execute upon.<br />
- *Detection* focused on navigating past obstacles in the turtlebot's path; the reason it is 'the turtlebot' and not 'the vehicles,' is because the turtlebot's plan would let the car navigate around obstacles without needing LiDAR active. Figuring out the most efficient way for the turtlebot to avoid obstacles while still making a competent plan for the car was tricky, though we managed to come up with a suitably functional method of keeping proper distance within the plan should an obstacle be detected.

## Interface
The interface is simple to use. All the user must do is enter a set of X-Y coordinates, separated by a comma, and submit. The program assumes the turtlebot's initial position as the effective origin point (0, 0). <br />

![IMG_3058](https://user-images.githubusercontent.com/78926321/145498040-2b8227b3-a391-4e31-9249-aef3a8b236d3.jpg)

## Demo

[![IMAGE ALT TEXT](http://img.youtube.com/vi/yrDb6ASoK2Y/0.jpg)](https://youtu.be/yrDb6ASoK2Y "Demo")
<br />
![IMG_3057](https://user-images.githubusercontent.com/78926321/145498103-fb40add2-ff4c-49fe-be2d-07391b3d0129.jpeg)
