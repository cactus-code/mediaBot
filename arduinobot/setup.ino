int pin = 13;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    switch (inByte) {
      case 'a':
      digitalWrite(pin, LOW);
      delay(100);
      digitalWrite(pin, HIGH);
      delay(100);
      digitalWrite(pin, LOW);
      delay(100);
      digitalWrite(pin, HIGH);
      delay(100);
      digitalWrite(pin, LOW);
    }
  }
}
