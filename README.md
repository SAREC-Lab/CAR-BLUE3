# Car - Blue 3

### Important Links
[Github Repository](https://github.com/SAREC-Lab/CAR-BLUE3/tree/main) <br />
[Trello Board](https://trello.com/b/wCxuc2UZ/main-project)

## Environment Setup

1. Clone this repo under directory `catkin_ws/src/`

2. Run `catkin_make` to install this package

## How to Run the Car

### Real Car

1. Run `roslaunch mushr_base teleop.launch`
2. Run `roslaunch CAR-BLUE3 path_publisher.launch`
    1. To specify the plan file, `roslaunch CAR-BLUE3 path_publisher.launch plan_file:='/path/to/plan.txt'`

### Simulation
1. `roslaunch mushr_sim teleop.launch`
2. `rosrun rviz rviz -d $HOME/catkin_ws/src/mushr/mushr_utils/rviz/default.rviz`
3. `roslaunch CAR-BLUE3 path_publisher.launch`

*Don’t forget: $ shutdown now*


### Push Code to the Car
1. Pull Code to the local repo
2. Connect to Car's wifi
3. Go to the parent directory `cd ..` and run `rsync -rlptzv --progress --delete --exclude=.git ./CAR-BLUE3 "robot@10.42.0.1:~/catkin_ws/src"`

## Documentation

### Domain Specific Language
We used JSON to format our task plans because JSON is a lightweight data formatting language that is easy for humans to read and write, and easy for machines to parse the input. Python, the language of our parser, has a json library which makes it easy to handle JSON objects and files. We utilize functions from this library to easily read in the task plan. 
Our JSON file has a command and a value. The command represents what the car will be doing. We realized that we can simplify our commands to "drive" "circle" and "stop" by sending in some other values as a part of the value array. For example, for drive we send in a distance and a direction where the direction is a binary value such that forward movement corresponds to 1 and reverse movement corresponds to 0. The same idea is used with circle where leftward movement is 1 and rightward movement is 0. We also realized that a turn is just a quarter circle so we used this knowledge to buff up our circle utils to take in the number of revolutions. Thus, as a part of our JSON input in the value array for command "circle" we have the radius, left/right direction, forward/reverse direction, and number of revolutions where a turn is 0.25 revolutions and a full circle is 1. For "stop", the value is just the number of seconds to remain stopped. 

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
D2, drive.py, stop.py, utils.py<br />
D3, turn.py, utils.py<br />
D4, circle.py, three_point.py, utils.py

### Testing
In order to test the program, we largely followed a trial-and-error style of approach; develop a segment of the code, then test it on the car, see what it does, then develop based on results. For example, for the simplest prompt - drive - we started by testing that the car would drive if prompted; after we knew it would drive, we tested if it would drive the right distance. After knowing it went the right distance, we tried going in different directions (in the case of reversing, due to our distance formula, it would reverse infinitely until it was interrupted on the first trial). We followed this method for each possible prompt - making sure the car would do its instructions for the correct duration, going the right distance, in the right direction, and at the right time. <br />
Upon having every possible prompt satisfied, we implemented it with the state machine, and imported it on the car. After a few more tests ensuring that the state machine was functional (using test JSON files as input), the project was effectively completed.

## Comments and Grades

Good job in running experiments with the physical car, the traceability matrix could be better formatted (as shown in the assignment doc)

** Grade: 100/100 **
