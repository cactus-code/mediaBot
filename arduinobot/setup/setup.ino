int red_pin = 12;
int green_pin = 11;
int blue_pin = 10;

void setup() {
  Serial.begin(9600);
}

void set_rgb(int red_val,int green_val,int blue_val) {
  analogWrite(red_pin,red_val);
  analogWrite(green_pin,green_val);
  analogWrite(blue_pin,blue_val);
}

void loop() {
  char serialdata[80];
  int lf = 10;
  Serial.readBytesUntil(lf, serialdata, 80);
  set_rgb(serialdata,serialdata,serialdata);
}

