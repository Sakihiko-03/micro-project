#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
String TextIn,TextL1,TextL2;
int green=13,aqua=11,orange=12;
void setup() {
  Serial.begin(9600);
  pinMode(green,OUTPUT);
  pinMode(aqua,OUTPUT);
  pinMode(orange,OUTPUT);
  lcd.begin();
}

void loop() {
  if (Serial.available())
      TextIn = Serial.readStringUntil('\n');
  else
      TextIn = "";

  if(TextIn=="N0")
      digitalWrite(green,LOW);
  if(TextIn=="N1")
      digitalWrite(green,HIGH);
  if(TextIn=="S0")
      digitalWrite(aqua,LOW);
  if(TextIn=="S1")
      digitalWrite(aqua,HIGH);
  if(TextIn=="D0")
      digitalWrite(orange,LOW);
  if(TextIn=="D1")
      digitalWrite(orange,HIGH);
      
  if (TextIn.startsWith("L1:")){
      TextL1 = TextIn.substring(3);
      lcd.setCursor(0,0);
      lcd.print(TextL1);
      }
  if (TextIn.startsWith("L2:")){
      TextL2 = TextIn.substring(3);
      lcd.setCursor(0,1);
      lcd.print(TextL2);
      delay(7000);
      lcd.clear();
      }
}
