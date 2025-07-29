#include <Servo.h>

const byte numChars = 32;
char receivedChars[numChars];
boolean newData = false;

// Servo objects for each coin type
Servo servo1;
Servo servo5;
Servo servo10;
Servo servo20;

// Define servo pins
const int SERVO_1_PIN = 5;
const int SERVO_5_PIN = 6;
const int SERVO_10_PIN = 7;
const int SERVO_20_PIN = 8;

// Common angles and delay
const int PUSH_ANGLE = 180;
const int RESET_ANGLE = 0;
const int DISPENSE_TIME = 1;

void setup() {
  Serial.begin(9600);
  Serial.println("<Multi-Coin Dispenser Ready>");

  // Attach servos
  servo1.attach(SERVO_1_PIN);
  servo5.attach(SERVO_5_PIN);
  servo10.attach(SERVO_10_PIN);
  servo20.attach(SERVO_20_PIN);

  // Set initial position
  servo1.write(PUSH_ANGLE);
  servo5.write(PUSH_ANGLE);
  servo10.write(PUSH_ANGLE);
  servo20.write(PUSH_ANGLE);
}

void loop() {
  recvWithEndMarker();
  if (newData) {
    newData = false;

    String command = String(receivedChars);
    command.trim();

    if (command == "1") {
      dispenseCoin(servo1, 1);
    } else if (command == "5") {
      dispenseCoin(servo5, 5);
    } else if (command == "10") {
      dispenseCoin(servo10, 10);
    } else if (command == "20") {
      dispenseCoin(servo20, 20);
    } else {
      Serial.print("[ERROR] Unknown coin value: ");
      Serial.println(command);
    }
  }
}

void recvWithEndMarker() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();

    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    } else {
      receivedChars[ndx] = '\0';
      ndx = 0;
      newData = true;
    }
  }
}

void dispenseCoin(Servo &s, int value) {
  Serial.print("[DISPENSING ");
  Serial.print(value);
  Serial.println(" PESO COIN]");
  
  for (int pos = PUSH_ANGLE; pos >= RESET_ANGLE; pos--) {
    s.write(pos);
    delay(DISPENSE_TIME); // Smaller delay = faster movement
  }

  for (int pos = RESET_ANGLE; pos <= PUSH_ANGLE; pos++)
  {
    s.write(pos);
    delay(DISPENSE_TIME);
  }

  

}
