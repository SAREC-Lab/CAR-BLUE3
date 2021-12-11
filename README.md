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

## Design

## Testing

## Interface Example
![IMG_3058](https://user-images.githubusercontent.com/78926321/145498040-2b8227b3-a391-4e31-9249-aef3a8b236d3.jpg)

## Demo
[![IMAGE ALT TEXT](http://img.youtube.com/vi/yrDb6ASoK2Y/0.jpg)](https://youtu.be/yrDb6ASoK2Y "Demo")
![IMG_3057](https://user-images.githubusercontent.com/78926321/145498103-fb40add2-ff4c-49fe-be2d-07391b3d0129.jpeg)
