
# IGVC Emergency Stop  
  
This package allows to implement the E Stop with brakes functionality. It creates a node that listens to e stop signal from arduino and upon button press creates `pure_pursuit` node that takes over the `pure_pursuit` from Autoware.AI and sets all the velocity values to zero, making the car stop.

## Requires

Following are the requirements for the package.
- Python 2.7
- ROS Melodic
- autoware_msgs

## Building the package
The pacakge requires on `autoware_msgs` so the autoware needs to be sourced before building the package. 

```commandline
source <path-to-autoware>/install/setup.bash
catkin_make
```

## Running the package
### roslaunch 
To launch the package, simple use `roslaunch` command.
```commandline
source devel/setup.bash
roslaunch igvc_estop estop_listener_node.launch 
```
Using roslaunch won't require launching `roscore` separately.

### rosrun
To run the package, simple use `rosrun` command. 

```commandline
source devel/setup.bash
rosrun igvc_estop estop_listener.py
```

Before running `rosrun`, make sure `roscore` is running.