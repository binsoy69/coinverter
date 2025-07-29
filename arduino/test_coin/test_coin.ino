volatile int pulseCount = 0;
unsigned long lastPulseTime = 0;
const unsigned long debounceDelay = 20; // milliseconds

void setup() {
  pinMode(2, INPUT_PULLUP); // Connect signal wire to pin 2
  attachInterrupt(digitalPinToInterrupt(2), countPulse, FALLING);
  Serial.begin(9600);
  Serial.println("Coin Acceptor Ready");
}

void loop() {
  static int lastReportedCount = 0;
  
  if (pulseCount != lastReportedCount) {
    Serial.print("Pulses detected: ");
    Serial.println(pulseCount);
    lastReportedCount = pulseCount;
  }
}

void countPulse() {
  // Debounce to avoid false triggering
  unsigned long currentTime = millis();
  if (currentTime - lastPulseTime > debounceDelay) {
    pulseCount++;
    lastPulseTime = currentTime;
  }
}
