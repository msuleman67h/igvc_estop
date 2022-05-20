# IGVC Emergency Stop      
 This package allows to implement the E Stop with brakes functionality. It creates a node that listens to e stop signal from arduino and upon button press sends signal to `pure_pursuit` node that sets all the velocity values to zero, making the car stop.    
    
## Requires    
 Following are the requirements for the package.    
- Python 2.7    
- ROS Melodic  
    
## Building the package 
```commandline 
catkin build  
``` 
or   
```commandline 
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
rosparam set "estop_topic_name" "gem_estop" 
rosrun igvc_estop estop_listener.py 
```    
 Before running `rosrun`, make sure `roscore` is running.  
  
## Usage 
The node `estop_btn_event_listener` will listen to the rostopic (default=`"gem_estop"`) mentioned in the file `estop_listener_node.launch`. If the topic `gem_estop` value is set to true, `estop_btn_event_listener`sends signal to `pure_pursuit` node that sets all the velocity values to zero, making the car stop.    