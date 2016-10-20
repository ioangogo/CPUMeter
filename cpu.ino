// A Cpu meter, Copyright Ioan Loosley

int meter  = 11;   // blue LED in Digital Pin 9 (PWM)
int old = 0;
int failcount = 1000;
void setup(){
  Serial.begin(9600);
  pinMode(meter,OUTPUT);  // tell arduino it's an output
  // test and set all the outputs to low
  digitalWrite(meter,LOW);
  Serial.setTimeout(300);
  for(int x = 255;x =< 0;x--){analogWrite(meter,x);delay(100); }
}
  
void loop(){
  int msg;
  
  msg = Serial.read();
  
  int x = int(msg);
  if(x == -1){
    return;
    }
  
  analogWrite(meter,x);old=x;Serial.println(x,HEX);
}
