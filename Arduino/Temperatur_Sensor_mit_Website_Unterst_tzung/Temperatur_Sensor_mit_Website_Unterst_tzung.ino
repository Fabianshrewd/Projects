#include <DHT.h>
#include <DHT_U.h>
#include <TMP36.h>
#include <dht11.h>
#include <SoftwareSerial.h>
#define RX 2
#define TX 3
#define DHTPIN 8
#define DHTTYPE DHT11
#define dht_apin 11 // Analog Pin sensor is connected to
dht11 dhtObject;
String AP = "HUAWEI-B535-A279";       // AP NAME
String PASS = "B9JJ7FT48Q5"; // AP PASSWORD
String API = "DJYW17FHGTQOUG9Y";   // Write API KEY
String HOST = "api.thingspeak.com";
String PORT = "80";
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
int valSensor = 1;
  
SoftwareSerial esp8266(RX,TX); 

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  esp8266.begin(115200);
  dht.begin();
  sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");
  pinMode(A0, INPUT);
}

void loop() {
  
 String getData = "GET /update?api_key="+ API +"&field1="+getTemperatureValue();
 sendCommand("AT+CIPMUX=1",5,"OK");
 sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
 sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
 esp8266.println(getData);delay(1500);countTrueCommand++;
 sendCommand("AT+CIPCLOSE=0",5,"OK");
 delay(5000);
}


String getTemperatureValue(){

  float t = dht.readTemperature();
  return String(t); 
  
}


String getHumidityValue(){

   dhtObject.read(dht_apin);
   Serial.print(" Humidity in %= ");
   int humidity = dhtObject.humidity;
   Serial.println(humidity);
   delay(50);
   return String(humidity); 
  
}

void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println("OYI");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }
