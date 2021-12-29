// put your setup code here, to run once:
void setup() {
  //Begin the serial
  Serial.begin(9600);
  
  //Input into Analog0 from the sensor
  pinMode(A0, INPUT);
}


// put your main code here, to run repeatedly:
void loop() {
  //Read in from the information
  float sensor = analogRead(A0);
  
  //Calculate the celcius
  float celcius = ((sensor * (5.0/1024))-0.5)/0.01;
  
  //Print in the Serial
  Serial.println(celcius);
  
  //Delay it by 1000ms
  delay(1000);
}
