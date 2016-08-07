/* Reggie servo control and serial parse
Credit to: Scott Fitzgerald for the Servo control aspect of this 
*/
#include <Servo.h>

Servo x_axis;  // create servo object to control a servo
Servo y_axis; 
Servo pellet;
int serv_num; // 0 - x axis 1 - y-axis 2-pellet_release. Not the actual pins used, easier to track like this. Use any PWM pins
int ang;      // angle to be passed via serial

void setup() {
  x_axis.attach(9); // actual pwm pins 
  y_axis.attach(11);
  pellet.attach(12);
  Serial.begin(9600); // usb

  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {

  while (Serial.available()==0) {             //Wait for serial

  }

  String serv = Serial.readStringUntil(','); // this gives the first half of the comma delimited data 
  serv_num = serv.toInt();
  ang = Serial.parseInt();
  Serial.println(serv); // For debugging via Arduino IDE
  Serial.println(ang); // do NOT attempt to run Arduino serial monitor while python has control of the serial... it will crash...
  if (serv_num==0){
      x_axis.write(ang);
    }
  else if (serv_num==1){
      y_axis.write(ang);
    }
   else if (serv_num==2){
     pellet.write(ang);
    }
  delay(15); // good practice 
}

