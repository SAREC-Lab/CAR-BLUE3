# Car - Blue 3

## Environment Setup

1. Clone this repo under directory `catkin_ws/src/`

2. Run `catkin_make` to install this package

## How to Run the Car

1. Run `roslaunch mushr_base teleop.launch` or `roslaunch mushr_sim teleop.launch` for simulation
2. Run `roslaunch CAR-BLUE3 path_publisher.launch`
    1. To specify the plan file, `roslaunch CAR-BLUE3 path_publisher.launch plan_file:='/path/to/plan.txt'`

*Don’t forget: $ shutdown now*

### Important Links
[Github Repository](https://github.com/SAREC-Lab/CAR-BLUE3/tree/main) <br />
[Trello Board](https://trello.com/b/wCxuc2UZ/main-project)

### Requirements and Designs
R1: Create a state machine to handle any driving orders given to a MUSHR car<br />
D1: Create code that parses & distributes movement plans to the state machine<br />
D2: The car can move forward and backward from input<br />
D3: The car can make simple turns from input<br />
D4: More complex movements, such as three-point turns and moving in a circle

### Trace Matrix
R1, D1<br />
R1, D2<br />
R1, D3<br />
R1, D4<br />

D1, controller.py, parser.py, instruction.py, plan_runner.py<br />
D2, drive.py, stop.py<br />
D3, turn.py<br />
D4, circle.py, three_point.py
