# Car - Blue 3

## Project 01

### Important Links
[Github Repository](https://github.com/SAREC-Lab/CAR-BLUE3/tree/main)
[Trello Board](https://trello.com/b/wCxuc2UZ/main-project)

### Requirements and Designs
R1: Create a state machine to handle any driving orders given to a MUSHR car
D1: Create code that parses & distributes movement plans to the state machine
D2: The car can move forward and backward from input
D3: The car can make simple turns from input
D4: More complex movements, such as three-point turns and moving in a circle

### Trace Matrix
R1, D1
R1, D2
R1, D3
R1, D4

D1, controller.py, parser.py, instruction.py, plan_runner.py
D2, drive.py, stop.py
D3, turn.py
D4, circle.py, three_point.py
