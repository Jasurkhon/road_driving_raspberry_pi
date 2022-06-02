import wiringpi

class Motors:
    #DC Motors
    IN1_PIN = 1
    IN2_PIN = 4
    IN3_PIN = 5
    IN4_PIN = 6
    
    MAX_SPEED = 45
    MIN_SPEED = 0
    
    SOFT_PWM_OUTPUT = 4

    speed = 40

    def __init__(self):
        wiringpi.wiringPiSetup()
        pass

    def initDCMotor(self):
        wiringpi.pinMode(self.IN1_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN2_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN3_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN4_PIN, self.SOFT_PWM_OUTPUT)

        wiringpi.softPwmCreate(self.IN1_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN2_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN3_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN4_PIN, self.MIN_SPEED, self.MAX_SPEED)
    
    def moveForward(self, speed):
        wiringpi.softPwmWrite(self.IN1_PIN, speed)
        wiringpi.softPwmWrite(self.IN2_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, speed)
        wiringpi.softPwmWrite(self.IN4_PIN, self.MIN_SPEED)

    def  moveRight(self):
        wiringpi.softPwmWrite(self.IN1_PIN, int(self.MAX_SPEED-10))
        wiringpi.softPwmWrite(self.IN2_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN4_PIN, int(self.MAX_SPEED-10))

    def moveLeft(self):
        wiringpi.softPwmWrite(self.IN1_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN2_PIN, int(self.MAX_SPEED-10))
        wiringpi.softPwmWrite(self.IN3_PIN, int(self.MAX_SPEED-10))
        wiringpi.softPwmWrite(self.IN4_PIN, self.MIN_SPEED)

    def stop(self):
        wiringpi.softPwmWrite(self.IN1_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN2_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN4_PIN, self.MIN_SPEED)

   
