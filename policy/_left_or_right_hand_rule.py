## Policy known by scan twist center control node
## can be either left or right hand rule. 

import math


class LeftOrRightHandRule:

    def __init__(self, type, turn_speed= 8.0):

        self.type = type
        self.direction = 1 if type=='LHR' else -1
        self.turn_speed = turn_speed
        self.decision = ''


    def step(self, space_ahead, angle_with_closet_obstacle):
        linear_x_factor = 0.
        angular_z = 0.

        if (space_ahead < 0.6):
            angular_z = self.direction * self.turn_speed            # Make turns. distance at front front less than 2 desired distance_to_wall
            self.decision = 'Turn'
            
        elif (space_ahead < 4):
            linear_x_factor = 0.2                                         # Ahead. distance at front less than 4 desired distance_to_wall
            self.decision = 'Ahead'
            
        elif (math.fabs(angle_with_closet_obstacle) < 2):        # Slow ahead
            linear_x_factor = 0.1
            self.decision = 'Slow ahead'
        else:
            linear_x_factor = 0.5                                # Full speed ahead
            self.decision = 'Full speed ahead'

        # self.pirnt_status()
        return linear_x_factor, angular_z
    
    def print_status():
        print("Decision: ")
        print(self.decision)
