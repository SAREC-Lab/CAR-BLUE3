## Risks

### Risk 01
**Issue:** 
- Sending data from turtlebot to car.
- Our group has not yet worked with a physical turtlebot and we have never
  before tried to communicate across multiple ros systems. 

**Solution:**
- Setup pub/sub communication where the turtlebot publishes the command and the
  car subscribes to it to receive the desired command. 
- First, the car's ROS\_MASTER\_URI must be set to the turtlebot i.e.
  http://$TURTLEBOT\_IP:11311. 
- Next, the turtlebot and car will be able to see each other's topics including
  the new communication topic to send the command. 
- Then, simply publish messages from turtlebot that the car subscribes to. 

### Risk 02
**Issue:** 
- Sending user data to turtlebot (relative coordinates.
- Our group does not have a lot of experience with sockets or the sending of
  data from one place to another. 

**Solution:**
- Use python sockets to develop a connection between us as the user and the
  turtlebot. 
- The turtlebot will act as the server and the user will be the client that
  connects to it and sends the relative coordinates message.

### Risk 03
**Issue**
- Developing front-end UI for sending coordinates.
- Our group does not have a lot of experience with front-end development. 

**Solution:**
- Look into using tkinter or other simple TUIs. 
