# Código por Flaybson Diniz

int VALOR = 0;
int LED = 13;

void setup() {                
	pinMode(LED, OUTPUT);     
	Serial.begin(115200);
}

void loop() {
	VALOR=Serial.read();
	if (VALOR=='1')
	{
		digitalWrite(LED,HIGH);
	}
	else if(VALOR=='2')
	{
		digitalWrite(LED,LOW);
	}
}

