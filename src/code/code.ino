// C++ code
//
const int pinoEntrada = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valorSensor = analogRead(pinoEntrada);
  int mapa = map(valorSensor, 0, 1023, 2, 2558);

  Serial.println(mapa);

  delay(20);
}