int irPin1 = 6;
int irPin2 = 8;
int irVal1;
int irVal2;
void setup() {
  // put your setup code here, to run once:
  pinMode(irPin1, INPUT);
  pinMode(irPin2, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  irVal1 = digitalRead(irPin1);
  irVal2 = digitalRead(irPin2);

  if(irVal1==0){
    Serial.print("Someone Entered");
    delay(1000);
  }
  else if(irVal2==0){
    Serial.print("Someone Exited");
    delay(1000);
  }
}
