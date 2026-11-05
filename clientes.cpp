#include <Wifi.h>
#include <Httpcliente.h>

const char* ssid "nome-da-rede";
const char* password = "senha-wifi";

//Tem que colocar o IP do py na rede abaixo
const char* serverUrl "http://192.168.1.100:5000/api/dados";

const char DISPOSITIVO_ID "Esp32_Cliente1";
const char TIPO_SENSOR = "temperatura"; //colocar o sensor aqui