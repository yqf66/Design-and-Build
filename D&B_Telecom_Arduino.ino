#include <Wire.h> 
#include <Servo.h>
#include <SoftwareSerial.h>
// 定义引脚
Servo myservo;
SoftwareSerial BT(1,0); // 接HC05发送脚与D1接口连接，HC05接收脚与D0接口连接
char val;  // 存储接收的数据
int servoPin = 47;
int motorPin1 = 11;  // IN1连接到Arduino引脚11
int motorPin2 = 10;  // IN2连接到Arduino引脚10
int motorPin3 = 9;  // IN3连接到Arduino引脚9
int motorPin4 = 8;  // IN4连接到Arduino引脚8
const int trigPin0 = 52;
const int echoPin0 = 50;
const int trigPin1 = 4;
const int echoPin1 = 5;
const int trigPin2 = 6;  
const int echoPin2 = 7;
const int button=37;
int speedPin1 = 3;  
int speedPin2 = 2;  
int buttonState=0;
const int S0 = 28;
const int S1 = 30;
const int S2 = 24;
const int S3 = 26;
const int OUT = 32;
const int LEDp=45;
const int LEDn=43;
const int TLEDp=40;
const int TLEDn=42;
int red = 0; 
int green = 0; 
int blue = 0; 
char colour;
int loopTime=0;
float tempdistance0=0.00;
float tempdistance1=0.00;
float tempdistance2=0.00;
void setup() {
  Serial.begin(9600);   
  BT.begin(9600);
  myservo.attach(servoPin);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  Serial.begin(9600);
  pinMode(trigPin0, OUTPUT);
  pinMode(echoPin0, INPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(speedPin1, OUTPUT);
  pinMode(speedPin2, OUTPUT);
  pinMode(button,INPUT);
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(OUT, INPUT);
  pinMode(LEDp,OUTPUT);
  pinMode(LEDn,OUTPUT);
  pinMode(TLEDp,OUTPUT);
  pinMode(TLEDn,OUTPUT);
   // 配置 TCS3200 工作模式和输出类型
  digitalWrite(S0, HIGH);
  digitalWrite(S1, HIGH); 
}

void loop() {
  // put your main  code here, to run repeatedly:
  // 把串口监视器接收到的数据发送给蓝牙模块
   if (Serial.available()) {
          val = Serial.read();
          BT.print(val);
    }
       // 把蓝牙模块接收到的数据发送到串口监视器
   if (BT.available()) {
          val = BT.read();
          Serial.print(val);
   }
  digitalWrite(LEDp,LOW);
  digitalWrite(LEDn,LOW);
  digitalWrite(TLEDp,LOW);
  digitalWrite(TLEDn,LOW);
  float distance0=Distance0();
  float distance1=Distance1();
  float distance2=Distance2();
  if(loopTime<6){
    loopTime++;
    if(loopTime==1){
    tempdistance0=distance0;
    tempdistance1=distance1;
    tempdistance2=distance2;
  }
  }
  buttonState=digitalRead(button);
  if(buttonState==LOW){
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  }
  if(buttonState==HIGH){
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  analogWrite(speedPin1, 90); 
  analogWrite(speedPin2, 90);
  Serial.println(loopTime);
  Serial.println(distance0);
  Serial.println(distance1);
  Serial.println(distance2);
  if(loopTime==6){
    Serial.println(abs(tempdistance0-distance0));
    Serial.println(abs(tempdistance1-distance1));
    Serial.println(abs(tempdistance2-distance2));
    loopTime=0;
    if(abs(tempdistance0-distance0)<5&&abs(tempdistance1-distance1)<5&&abs(tempdistance2-distance2)<5){
      digitalWrite(LEDp,HIGH);
      digitalWrite(LEDn,LOW);
      digitalWrite(motorPin1, LOW);                                                                                           
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, HIGH);
      analogWrite(speedPin1, 90); 
      analogWrite(speedPin2, 90); 
      Serial.println("倒退");
      delay(300);
      if(distance1>distance2){
       fixRight();
      }
      if(distance1<distance2){
       fixLeft();
      }
    }
  }
  if(distance0<13){
  if(distance1>25||distance2>25){
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, HIGH);
  analogWrite(speedPin1, 90); 
  analogWrite(speedPin2, 90); 
  Serial.println("倒退");
  delay(250);
  if(distance1>distance2){
    turnLeft();
  }
  if(distance1<distance2){
    turnRight();
  }}
  else{
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, HIGH);
    analogWrite(speedPin1, 110); 
    analogWrite(speedPin2, 110);
    delay(900);
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    Serial.println("停");
    //take photo
    myservo.write(0);
    delay(1000);  // 等待1秒
    myservo.write(23);
    delay(1000);
    myservo.write(45);
    delay(1000);  // 等待1秒
    // 将舵机旋转到90度（中间位置）
    myservo.write(67);
    delay(1000);
    myservo.write(90);
    delay(1000);  // 等待1秒
    myservo.write(113);
    delay(1000);
    myservo.write(135);
    delay(1000);  // 等待1秒
    // 将舵机旋转到180度（最大角度）
    myservo.write(157); 
    delay(1000);
    myservo.write(180);
    delay(1000);
    myservo.write(0);
   // 等待1秒
    delay(1000);
    if(distance1>distance2){
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, HIGH); 
    analogWrite(speedPin1, 150);             
    analogWrite(speedPin2, 150);
    Serial.println("左转");
    delay(650);
  }
  if(distance1<distance2){
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, LOW);
    analogWrite(speedPin1, 150); 
    analogWrite(speedPin2, 150); 
    Serial.println("右转");
    delay(650);
  }}}}
  delay(200);
} 

float Distance0(){
  digitalWrite(trigPin0, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin0, LOW);
  // 读取Echo引脚的脉冲宽度
  long duration0 = pulseIn(echoPin0, HIGH);
  // 将脉冲宽度转换为距离（单位：厘米）
  float distance0 = duration0 * 0.034 / 2;
  return distance0;
}
float Distance1(){
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  // 读取Echo引脚的脉冲宽度
  long duration1 = pulseIn(echoPin1, HIGH);
  // 将脉冲宽度转换为距离（单位：厘米）
  float distance1 = duration1 * 0.034 / 2;
  return distance1;
}
float Distance2(){
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  // 读取Echo引脚的脉冲宽度
  long duration2 = pulseIn(echoPin2, HIGH);
  // 将脉冲宽度转换为距离（单位：厘米）
  float distance2 = duration2 * 0.034 / 2;
  return distance2;
}
void turnLeft(){
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH); 
  analogWrite(speedPin1, 110);             
  analogWrite(speedPin2, 110);
  Serial.println("左转");
  delay(350);
}
void turnRight(){
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  analogWrite(speedPin1, 110); 
  analogWrite(speedPin2, 110); 
  Serial.println("右转");
  delay(350);
}
void fixLeft(){
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  analogWrite(speedPin1, 95); 
  analogWrite(speedPin2, 95); 
  Serial.println("左边过窄，修正");
  delay(70);
}
void fixRight(){
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH); 
  analogWrite(speedPin1, 95); 
  analogWrite(speedPin2, 95);
  Serial.println("右边过窄，修正");
  delay(70);
}
