volatile int pulseCount = 0;
unsigned long lastPulseTime = 0;
unsigned long timeout = 1000;  // 1 second = end of pulse train

void setup() {
  pinMode(2, INPUT);
  attachInterrupt(digitalPinToInterrupt(2), countPulse, FALLING);

  Serial.begin(9600);  // Serial to Raspberry Pi over USB
  Serial.println("[READY] Insert a coin...");
}

void loop() {
  if (pulseCount > 0 && millis() - lastPulseTime > timeout) {
    Serial.print("COIN:");
    Serial.println(pulseCount);  // Send pulse count to Pi
    
    pulseCount = 0;  // Reset
    Serial.println("[READY] Insert next coin...");
  }
}

void countPulse() {
  pulseCount++;
  lastPulseTime = millis();
}
