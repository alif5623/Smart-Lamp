// C++ code
//
void setup()
{
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{
  if (Serial.available() > 0) {
    char c = Serial.read();
    if(c =='1' || digitalRead(2) == 0){
      digitalWrite(7, HIGH);
    }else{
      digitalWrite(7, LOW);
    }
  }
}