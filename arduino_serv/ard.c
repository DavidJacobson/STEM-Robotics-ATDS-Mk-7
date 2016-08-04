/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo x_axis;  // create servo object to control a servo
Servo y_axis; 
Servo pellet;
int serv_num;
int ang;
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  x_axis.attach(9);
  y_axis.attach(11);
  pellet.attach(12);
  Serial.begin(9600);

  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

}

void loop() {

  while (Serial.available()==0) {             //Wait for user input

  }

  String serv = Serial.readStringUntil(',');
  serv_num = serv.toInt();
  ang = Serial.parseInt();
  Serial.println(serv);
  Serial.println(ang);
  if (serv_num==0){
      x_axis.write(ang);
    }
  else if (serv_num==1){
      y_axis.write(ang);
    }
   else if (serv_num==2){
     pellet.write(ang);
    }
  delay(15);
}

