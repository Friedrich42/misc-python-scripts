/*
  Projet d'apprentissage d'un objet connecté (IoT)  pour réaliser une sonde de température
  ESP8266 + DHT22 + LED + MQTT + Home-Assistant
  Projets DIY (http://www.projetsdiy.fr) - Mai 2016
  Licence : MIT
*/
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define wifi_ssid "Tor_2G"
#define wifi_password "makeithappen"

#define mqtt_server "192.168.1.55"
#define mqtt_user "alarm"      // if exist
#define mqtt_password "alarm"  //idem

#define temperature_topic "s/t"  // Topic temperature
#define humidity_topic "s/h"        // Topic humidity

// Buffer to decode MQTT messages
char message_buff[100];

long lastMsg = 0;   
long lastRecu = 0;
bool debug = true;  // Display log message if True

// Create objects 
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(9600);     
  pinMode(D8,OUTPUT);     //Pin 8 for Relay module
  setup_wifi();           //Connect to Wifi network
  client.setServer(mqtt_server, 1883);    // Configure MQTT connexion
  client.setCallback(callback);           // callback function to execute when a MQTT message   
}

void callback(char* topic, byte* payload, unsigned int length) {

  int i = 0;
  if ( debug ) {
    Serial.println("Message recu =>  topic: " + String(topic));
    Serial.print(" | length: " + String(length,DEC)+ "\n");
  }
  // create character buffer with ending null terminator (string)
  for(i=0; i<length; i++) {
    message_buff[i] = payload[i];
  }
  message_buff[i] = '\0';
  
  String msgString = String(message_buff);
  if ( debug ) {
    Serial.println("Payload: " + msgString);
  }
  
  if ( msgString == "ON" ) {
    digitalWrite(D8,HIGH);  
  } else if (msgString == "OFF") {
    digitalWrite(D8,LOW);  
  }
}

//Connecting to wifi
void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(wifi_ssid);

  WiFi.begin(wifi_ssid, wifi_password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi OK ");
  Serial.print("=> ESP8266 IP address: ");
  Serial.print(WiFi.localIP());
  Serial.println();
}

//Reconnection
void reconnect() {

  while (!client.connected()) {
    Serial.print("Connecting to MQTT broker ...");
    if (client.connect("ESP8266Client", mqtt_user, mqtt_password)) {
      Serial.println("OK");
    } else {
      Serial.print("KO, error : ");
      Serial.print(client.state());
      Serial.println(" Wait 5 secondes before to retry");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  // Send a message every 20 secs
  if (now - lastMsg > 1000 * 20) {
    lastMsg = now;
    // Read humidity
    float h = 4203;
    // Read temperature in Celcius
    float t = 42;

    client.publish(temperature_topic, String(t).c_str(), true);   // Publish temperature on temperature_topic
    client.publish(humidity_topic, String(h).c_str(), true);      // and humidity
  }
  if (now - lastRecu > 100 ) {
    lastRecu = now;
    client.subscribe("s/q");
  }
}
