// C++ code
//
void setup()
{
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop()
{
  if (Serial.available() > 0) {
    char c = Serial.read();
    if(c =='1'){
      digitalWrite(7, HIGH);
    }else{
      digitalWrite(7, LOW);
    }

    // Perform any necessary actions with the received string
    // ...
  }}