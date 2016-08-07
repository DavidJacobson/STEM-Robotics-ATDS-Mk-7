# STEM-Robotics-ATDS-Mk-7
This is the code that powered "Reggie" the automatic turret. This was written for The STEM Institute's Robotics class.
He was presented at the closing ceremony at City College


We were team Turbo Encabulators, inspired by the infamous techno-jargon video. 
Reggie the ATDS (Autmoatic Turret Defense System) was our project for the class. I handled all of the programming
and a fair amount of the assembly. We met our deadline and were able to present Reggie at the STEM closing ceremony. 

Reggie moves 180 degrees on the X-axis, stopping every 10 degrees to the check for a target. The assessment is conducted by an ultrasonic
sensor, which is attached to the nose of the turret. If a target is within firing range, the 2nd servo (the Y-axis servo) will adjust to
an appropriate height, and begin firing mode. 

To fire a pellet, a high torque motor is turned on. This motor turns a custom 3D printed gear which has exactly six teeth. Those teeth 
lock into a pinion, which compresses a spring and eventually fires.

Reggie also boasts a demo mode, where he spins around gracefully, showing off his different components and construction.

To build Reggie we used the following:


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

The approach I took was to be 'modular', that is, try to take advantage of Python's objects and model classes after physical components on the robot.
I used Git to track changes, and also backed things up off-site so if we accidentally shorted the pi (which may or may not have happened)
or damaged its storage in anyway, the code would remain safe.

I had a bottom-up design - I started by getting base functionality for each piece of the robot before linking together more complex procedures.
I spent the first week and a half finding and adapting, or even writing from scratch, the classes that would power Reggie.

I went through several huge hurdles trying to get the code to function. The first was a depreciated library that was referenced in nearly all tutorials I read. 
I struggled with cryptic errors before ditching the library and finding work arounds. 

One example of a serious issue was RPi.GPIO's inability to properly control multiple servos. The truth is - I may have been 
programming them incorrectly, but having the Arduino's API was extremely convenient, as it allowed me to specify the angle I wanted, not just the duty cycle. 

##Assembly
Our budget was tight, but our expectations were high, so we made due with what we could. Reggie's base was a sheet of cardboard, lathered in hot glue to keep breadboards and a quadpod in place. The quadpod was custom built out of metal elbows and wooden sticks. Originally all the peripherals were powered by the Pi, but when we pulled too much current we had to resort to an external battery pack. We put the high torque motor & Y-axis servo (it was significantly larger) on it. 

In Reggie's first sketch we included an analog controller to act as a failsafe, allowing the user to override Reggie should he fire at a friendly target. This was abandoned in favor of a large red switch. It was much simpler, faster to use, and easier to implement in the alloted time frame. 

Reggie's assembly was done in a very experimental way. Things would be added, tested, and phased out if not sufficient for the specifications. As a result of this, the wiring was kept on a breadboard instead of being permanently put together. This ended up being a hugely beneficial design choice when I had to swap out servos at the last minute. 

We used a battery pack (a secondary, backup one) as the base for the turret on the quadpod. This allowed us to conserve space and at the same time follow best practices with the addition of a failsafe. The idea of adding several failsafe systems had been so entrenched in our minds, there was no way we could have avoided it. "Redundancy is Key."

Here are some pictures:
