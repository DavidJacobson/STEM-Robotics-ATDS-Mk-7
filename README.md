# STEM-Robotics-ATDS-Mk-7
This is the code that powered "Reggie" the automatic turret. This was written for The STEM Institute's Robotics class.


We were team Turbo Encabulators, inspired by the infamous techno-jargon video. 
Reggie the ATDS (Autmatic Turret Defense System) was our project for the class. I handled all of the programming
and a fair amount of the assembly. We met our deadline and were able to present at the STEM closing ceremony. 

Reggie moves 180 degrees on the X-axis, stopping every 10 degrees to the check for a target. The assessment is conducted by an ultrasonic
sensor, which is attached to the nose of the turret. If a target is within firing range, the 2nd servo (the Y-axis servo) will adjust to
an appropriate height, and begin firing mode. 

To fire a pellet, a high torque motor is turned on. This motor turns a custom 3D printed gear which has exactly six teeth. Those teeth 
lock into a pinion, which compresses a spring and eventually fires.

Reggie also boasts a demo mode, where he spins around gracefully, showing off his diferent components and construction.

To build Reggie we used the follwing:


|Quantity| Material            |
|--------|-----------------------
| 1    | Raspberry Pi         |
| 1    | Arduino              |
| 2    | 3V Servos            |
| 1    | High powered Servo   |
| 2    | 7 Segment Displays   |
| 1    | High Torque Motor    |
| ~$50 | 3D printing filament |
| ∞    | Time for debugging   |

In reality he was constructed over the course of three weeks. We spent, on average, 4 hours a day on him; 3 in the morning, and one in the afternoon.
As the deadline approached, I took to staying later in the night, trying desperately to finish things up.


##Programming

The approach I took was to be 'modular', that is, try to take advantage of Python's objects and model classes after physical compenents on the robot.
I used Git to track changes, and also backed things up off-site so if we accidentally shorted the pi (which may or may not have happened)
or damaged its storage in anyway, the code would remain safe.

I had a bottom-up design - I started by getting base functionality for each piece of the robot before linking together more complex procedures.
I spent the first week and a half finding and adapting, or even writing from scratch, the classes that would power Reggie.

I went through several huge hurdles trying to get the code to function. The first was a depreciated library that was referenced in nearly all tutorials I read. 
I struggled with cryptic errors before ditching the library and finding work arounds. 

One example of a serious issue was RPi.GPIO's inability to properly control multiple servos. The truth is -  
