#include <SPI.h>
#include "RF24.h"

//прототип взаимодействия Arduino Uno с базовой станцией

const char car_id = 'e45thd';

RF24 radio(9, 10); // можно использовать любые
const uint32_t pipe_w = 123456789; // адрес
const uint32_t pipe_r = 766657575; // адрес
byte massiv_w[1];
byte massiv_r[2];

// Реле модуль подключен к цифровому выводу 4
const int Relay = 4;
const int buttonPin = 6;

int buttonState = 0;
bool relayState = false;
bool stateStation = false;

void setup() 
{
  radio.begin();
  radio.setDataRate(RF24_250KBPS); // скорость обмена данными RF24_1MBPS или RF24_2MBPS
  radio.openWritingPipe(pipe_w); // открыть канал на отправку 
  radio.openReadingPipe(1,pipe_r); // открыть канал на приём
  radio.startListening(); // приём         
  pinMode(Relay, OUTPUT);
  pinMode(buttonPin, INPUT);
  digitalWrite(Relay, HIGH);  //выключено
  massiv_w[0] = car_id;
}

void loop() 
{
    if(radio.available() and !stateStation) {
        radio.read(massiv_r, 2);
  
        if (massiv_r[0] == 255 and massiv_r[1] == car_id) {
          relayState = true;
          stateStation = true;
        }
        else if (massiv_r[0] == 155 and massiv_r[1] == car_id) {
          relayState = false;
          stateStation = false;
          delay(10000);
        }
        else {
          radio.stopListening(); 
          radio.write(massiv_w, 1);
          radio.startListening();
        }   
    }
    
    if (relayState) {
      // turn on:
      if (buttonState == HIGH) {
        digitalWrite(Relay, LOW);
        delay(60); // обязательно
      }
    } else {
      // turn off:
      digitalWrite(Relay, HIGH);
      delay(60); // обязательно
    }      
}
