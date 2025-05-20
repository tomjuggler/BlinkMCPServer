const int LED_PIN = LED_BUILTIN;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  while (!Serial);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == '1') {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("on");
    } 
    else if (command == '0') {
      digitalWrite(LED_PIN, LOW);
      Serial.println("off");
    }
    
    while (Serial.available() > 0) Serial.read();
  }
}
