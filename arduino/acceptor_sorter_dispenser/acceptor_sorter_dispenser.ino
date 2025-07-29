#include <Servo.h>

// --- Coin Acceptor ---
volatile int pulseCount = 0;
int intervalCounter = 0;
const unsigned long intervalThreshold = 30;  // Adjustable delay ticks

// --- Sorter Servo ---
Servo sorter;
const int SORTER_SERVO_PIN = 3;
const int COIN_PIN = 2;

// --- Sorter Angles ---
const int CENTER = 75;
const int LEFT = 40;
const int RIGHT = 110;

// --- Dispenser Servos ---
Servo dispenser1, dispenser5, dispenser10, dispenser20;
const int DISPENSE_1_PIN = 5;
const int DISPENSE_5_PIN = 6;
const int DISPENSE_10_PIN = 9;
const int DISPENSE_20_PIN = 10;

void setup() {
  pinMode(COIN_PIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(COIN_PIN), incomingPulse, FALLING);

  Serial.begin(9600);

  // Attach servos
  sorter.attach(SORTER_SERVO_PIN);
  dispenser1.attach(DISPENSE_1_PIN);
  dispenser5.attach(DISPENSE_5_PIN);
  dispenser10.attach(DISPENSE_10_PIN);
  dispenser20.attach(DISPENSE_20_PIN);

  center_sorter();

  Serial.println("[READY] Insert a coin or send DISPENSE:x");
}

void loop() {
  intervalCounter++;

  // Coin sorting block
  if (intervalCounter >= intervalThreshold && pulseCount > 0) {
    Serial.print("[IMPULSES RECEIVED] → ");
    Serial.println(pulseCount);

    // Sort based on pulse count
    if (pulseCount == 1 || pulseCount == 5) {
      move_sorter("RIGHT");
    } else if (pulseCount == 2 || pulseCount == 10 || pulseCount == 20) {
      move_sorter("LEFT");
    } else {
      Serial.println("[WARN] Unknown coin value, skipping sort.");
    }

    pulseCount = 0;
    intervalCounter = 0;
    Serial.println("[READY] Insert next coin...");
  }

  // Serial command handling
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd.startsWith("DISPENSE:")) {
      int value = cmd.substring(9).toInt();
      dispense_coin(value);
    }
  }

  delay(10);  // Simple 10ms loop timer
}

void incomingPulse() {
  pulseCount++;
  intervalCounter = 0;
}

void move_sorter(String direction) {
  if (direction == "LEFT") {
    sorter.write(LEFT);
    Serial.println("[SORT] → LEFT");
  } else if (direction == "RIGHT") {
    sorter.write(RIGHT);
    Serial.println("[SORT] → RIGHT");
  }

  delay(800);  // Give time to sort
  center_sorter();
}

void center_sorter() {
  sorter.write(CENTER);
  delay(500);
  Serial.println("[SORT] → CENTER");
}

void dispense_coin(int denom) {
  Servo* servo = nullptr;
  String label = "";

  switch (denom) {
    case 1: servo = &dispenser1; label = "₱1"; break;
    case 5: servo = &dispenser5; label = "₱5"; break;
    case 10: servo = &dispenser10; label = "₱10"; break;
    case 20: servo = &dispenser20; label = "₱20"; break;
    default:
      Serial.println("[ERROR] Invalid DISPENSE denomination");
      return;
  }

  Serial.print("[DISPENSE] ");
  Serial.println(label);

  // Sweep to push coin
  servo->write(160);
  delay(500);
  servo->write(0);
  delay(500);
}
