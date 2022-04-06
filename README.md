# lx-16a_ros
This repository explains how to implement the LX-16A Python Library in ROS environment.

## Test and configure the motors
Download the following program and install it.
[Download from here](https://www.dropbox.com/sh/b3v81sb9nwir16q/AAD61bT8Ot2bpV0MpLxbgn7Ta/LX-16A%20Bus%20Servo/Bus%20Servo%20Terminal%20V1.7.exe?dl=0
)

Once installed the program. Select the port and clic on "Open Port".

Connect one motor at once. Assign an unique ID (per motor) and click on save.

## Control your motors
1.- Clone your repo into your catkin workspace
```
cd ~/catkin_ws/src
git clone https://github.com/ShikurM56/lx-16a_ros.git
cd ~/catkin_ws/
catkin_make
```
2.- Go to your scripts folder, and be sure that _angle_publisher.py_ and _main.py_ are green color. It means that they are executable files.
```
cd ~/catkin_ws/src/lx-16a_ros/scripts/
ls
```
3.- If they aren't green color, change it:
```
cd ~/catkin_ws/src/lx-16a_ros/scripts/
sudo chmod +x angle_publisher.py
sudo chmod +x main.py
```

## Try your own implementations, with two or more motors.
```
You can change the function servoMode to motorMode, and give a value from -1000 to 1000 to activate it.
```
