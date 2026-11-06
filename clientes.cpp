#include <Wifi.h>
#include <Httpcliente.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11 //Em caso de sensor temp e umidade

const char* ssid "nome-da-rede";
const char* password = "senha-wifi";

//Tem que colocar o IP do py na rede abaixo
const char* serverUrl "http://192.168.1.100:5000/api/dados";

const char DISPOSITIVO_ID "Esp32_Cliente1";
const char TIPO_SENSOR = "temperatura"; //colocar o sensor aqui

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado ao Wi-Fi!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    float valorSensor = 24.5; //atualizar de acordo com o valor real do sensor