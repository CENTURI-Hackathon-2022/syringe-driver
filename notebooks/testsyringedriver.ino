#include <Stepper.h>
const int stepsPerRevolution = 32*64;  
Stepper myStepper(stepsPerRevolution, 9, 11, 10, 8);


void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorReading = analogRead(A0);
  int motorSpeed = map(sensorReading, 0, 1023, 0, 10);
  Serial.println(motorSpeed);
  
  if (motorSpeed > 8) {
    myStepper.setSpeed(5);
    myStepper.step(10);
  }
  if (motorSpeed < 2) {
    myStepper.setSpeed(5);
    myStepper.step(-10); 
  }
}
