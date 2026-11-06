#include <Wifi.h>
#include <Httpcliente.h>

const char* ssid "nome-da-rede";
const char* password = "senha-wifi";

//Tem que colocar o IP do py na rede abaixo
const char* serverUrl "http://192.168.1.100:5000/api/dados";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nESP32_01 conectado ao Wi-Fi!");
}

void loop() {
    if (Wifi.status == WL_CONNECTED) {
        int valorLuz = analogRead(LDR_PIN);

    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonPayload = "{\"cliente_id\":\"ESP32_01\",\"temperatura\":" + String(temp) + ",\"humidade\":" + String(hum) + "}";

    int httpResponseCode = http.POST(jsonPayload);
    Serial.print("Envio ESP32_02 - Status HTTP: ");
    Serial.println(httpResponseCode);
    http.end();
  }
  delay(5000); // Envia a cada 5 segundos
}

