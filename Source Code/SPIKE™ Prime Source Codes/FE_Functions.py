from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.iodevices import PUPDevice
from pybricks.parameters import Axis, Button, Color, Direction, Icon, Port, Side, Stop
from pybricks.tools import wait, Matrix, StopWatch
from umath import sin, pi, floor

hub = PrimeHub();
timer = StopWatch();

hub.system.set_stop_button([Button.BLUETOOTH]);
hub.speaker.volume(100);
hub.display.off();
hub.light.off();

groundColorSensor = ColorSensor(Port.A);
distanceSensor = UltrasonicSensor(Port.C);
cameraColorSensor = ColorSensor(Port.F);

distanceSensor.lights.on(0);

def colorSensorIntHSV(colorSensorPort, colorSensorReturnValue = -1):
    if (colorSensorReturnValue == -1):
        return [int(str(colorSensorPort.hsv()).split(",")[0].split("=")[1]), int(str(colorSensorPort.hsv()).split(",")[1].split("=")[1]), int(str(colorSensorPort.hsv()).split(",")[2].split("=")[1].split(")")[0])];
    elif (colorSensorReturnValue == 0):
        return int(str(colorSensorPort.hsv()).split(",")[0].split("=")[1]);
    elif (colorSensorReturnValue == 1):
        return int(str(colorSensorPort.hsv()).split(",")[1].split("=")[1]);
    elif (colorSensorReturnValue == 2):
        return int(str(colorSensorPort.hsv()).split(",")[2].split("=")[1].split(")")[0]);

def trafficSignColor():
    tscHue = colorSensorIntHSV(cameraColorSensor, 0);
    tscSat = colorSensorIntHSV(cameraColorSensor, 1);
    tscVal = colorSensorIntHSV(cameraColorSensor, 2);

    if (tscSat > 50):
        if (tscVal > 80):
            return "Green"; 
        else:
            return "Red"; 
    else:
        # print("Hue/Val: " + str(tscHue) + "/" + str(tscVal), end = " ");

        return "None";

def ifParking(ipDistanceTarget, ipDuration = 0):
    if (ipDuration == 0):
        if (distanceSensor.distance() < ipDistanceTarget):
            return "Parking";
        else:
            return "Normal";

    else:
        ipDistanceLowest = 2000;
        ipTimer = StopWatch();

        while (ipTimer.time() < ipDuration):
            ipDistance = distanceSensor.distance();

            if (ipDistance < ipDistanceLowest):
                ipDistanceLowest = ipDistance;

        if (ipDistanceLowest < ipDistanceTarget):
            return "Parking";
        else:
            return "Normal";

def pid(pidError, pidKp, pidKi, pidKd, pidKc, pidErrorSummation, pidErrorPrevious):
    pidProportion = pidError * pidKp;
    pidErrorSummation += pidError;
    pidIntegral = pidErrorSummation * pidKi;
    pidDerivative = (pidError - pidErrorPrevious) * pidKd;
    pidErrorPrevious = pidError;

    return pidErrorSummation, pidErrorPrevious, (pidKc * (pidProportion + pidIntegral + pidDerivative));

def pidPos(pidpLimit, pidpError, pidpKp, pidpKi, pidpKd, pidpKc, pidpErrorSummation, pidpErrorPrevious):
    pidpProportion = pidpError * pidpKp;

    # pidpErrorSummation += pidpError;
    pidpErrorSummation += 10 if (pidpError > 10) else pidpError;

    pidpIntegral = pidpErrorSummation * pidpKi;
    pidpDerivative = (pidpError - pidpErrorPrevious) * pidpKd;
    pidpErrorPrevious = pidpError;
    pidpValue = pidpKc * (pidpProportion + pidpIntegral + pidpDerivative);

    return pidpErrorSummation, pidpErrorPrevious, pidpValue if (pidpValue <= pidpLimit) else pidpLimit;

def pidNeg(pidnLimit, pidnError, pidnKp, pidnKi, pidnKd, pidnKc, pidnErrorSummation, pidnErrorPrevious):
    pidnProportion = pidnError * pidnKp;

    # pidnErrorSummation += pidnError;
    pidnErrorSummation += -10 if (pidnError < -10) else pidnError;

    pidnIntegral = pidnErrorSummation * pidnKi;
    pidnDerivative = (pidnError - pidnErrorPrevious) * pidnKd;
    pidnErrorPrevious = pidnError;
    pidnValue = pidnKc * (pidnProportion + pidnIntegral + pidnDerivative);

    return pidnErrorSummation, pidnErrorPrevious, pidnValue if (pidnValue >= pidnLimit) else pidnLimit;

def pidIntegralRate(pidirError, pidirKp, pidirKi, pidirKd, pidirKc, pidirIntegralRate, pidirErrorSummation, pidirErrorPrevious):
    pidirProportion = pidirError * pidirKp;
    pidirErrorSummation += pidirIntegralRate * abs(pidirError) / pidirError if (abs(pidirError) > pidirIntegralRate) else pidirError;
    pidirIntegral = pidirErrorSummation * pidirKi;
    pidirDerivative = (pidirError - pidirErrorPrevious) * pidirKd;
    pidirErrorPrevious = pidirError;
    pidirValue = pidirKc * (pidirProportion + pidirIntegral + pidirDerivative);

    return pidirErrorSummation, pidirErrorPrevious, pidirValue if (pidirValue >= -47) else -47;

def linearMap(lmInput, lmInputMin, lmInputMax, lmOutputMin, lmOutputMax):
    return ((((lmOutputMax - lmOutputMin) * (lmInput - lmInputMin)) / (lmInputMax - lmInputMin)) + lmOutputMin);

def linearMapPos(lmpInput, lmpInputMin, lmpInputMax, lmpOutputMin, lmpOutputMax):
    lmpValue = (((lmpOutputMax - lmpOutputMin) * (lmpInput - lmpInputMin)) / (lmpInputMax - lmpInputMin)) + lmpOutputMin;

    return lmpOutputMax if (lmpValue < lmpOutputMax) else lmpValue;

def linearMapNeg(lmnInput, lmnInputMin, lmnInputMax, lmnOutputMin, lmnOutputMax):
    lmnValue = (((lmnOutputMax - lmnOutputMin) * (lmnInput - lmnInputMin)) / (lmnInputMax - lmnInputMin)) + lmnOutputMin;

    return lmnOutputMax if (lmnValue > lmnOutputMax) else lmnValue;

class FutureEngineers:
    def __init__(self, steeringMotor, drivingMotor, visionMotor):
        self.drivingMotor = drivingMotor;
        self.steeringMotor = steeringMotor;
        self.visionMotor = visionMotor;

        self.trafficSignMidpoint = 80;
        self.streetErrorKp = 0.8;
        self.streetErrorKi = 0.000005;
        self.streetErrorKd = 0.7;

        self.drivingMotor.control.limits(2000, 1000, 1000);
        self.steeringMotor.control.limits(2000, 20000, 1000);
        self.visionMotor.control.limits(2000, 20000, 1000);

        # 65 backwards limit
    
    def smartStop(self, smartStopHeadingTarget):
        # print("START:", self.steeringMotor.angle(), "\tH:", hub.imu.heading(), end = "\t\b\b\b\b\b");
        smartStopSpeed = self.drivingMotor.speed();
        self.drivingMotor.hold();

        smartStopErrorSummation, smartStopErrorPrevious, smartStopErrorCorrection = 0, 0, 0;

        if (smartStopSpeed > 0):
            while (self.drivingMotor.speed() > 0):
                smartStopErrorSummation, smartStopErrorPrevious, smartStopErrorCorrection = pidIntegralRate(smartStopHeadingTarget - hub.imu.heading(), 2.5, 0.0005, 2.5, 1, 15, smartStopErrorSummation, smartStopErrorPrevious);
                self.steeringMotor.run_target(1000, smartStopErrorCorrection, Stop.HOLD, False);

        else:
            while (self.drivingMotor.speed() < 0):
                smartStopErrorSummation, smartStopErrorPrevious, smartStopErrorCorrection = pidIntegralRate(smartStopHeadingTarget - hub.imu.heading(), 2.5, 0.001, 2.5, -1, 15, smartStopErrorSummation, smartStopErrorPrevious);
                self.steeringMotor.run_target(1000, smartStopErrorCorrection, Stop.HOLD, False);

    def turn(self, turnDirection, turnHeadingTarget, turnSteerLimit, turnSpeedInitial, turnSpeedFinal):
        turnError, turnSpeed, turnErrorSummation, turnErrorPrevious, turnErrorCorrection = 0, 0, 0, 0, 0;
        # forward limit = 30;
        # backward limit = 55;

        turnHeadingStart = hub.imu.heading();
        turnHeadingDifference = turnHeadingTarget - turnHeadingStart;

        if (turnDirection > 0):
            if (turnHeadingTarget > turnHeadingStart):
                turnHeadingTarget -= 12;

                while (hub.imu.heading() < turnHeadingTarget):
                    turnError = turnHeadingTarget - hub.imu.heading();
                    turnSpeed = linearMap(turnError, turnHeadingDifference, 0, turnSpeedInitial, turnSpeedFinal);
                    turnErrorSummation, turnErrorPrevious, turnErrorCorrection = pidPos(turnSteerLimit, turnError, 2.5, 0.0001, 1.4, 1, turnErrorSummation, turnErrorPrevious);

                    self.drivingMotor.run(turnSpeed);
                    self.steeringMotor.run_target(1000, turnErrorCorrection, Stop.HOLD, False);

            else:
                turnSteerLimit *= -1;
                turnHeadingTarget += 12;

                while (hub.imu.heading() > turnHeadingTarget):
                    turnError = turnHeadingTarget - hub.imu.heading();
                    turnSpeed = linearMap(turnError, turnHeadingDifference, 0, turnSpeedInitial, turnSpeedFinal);
                    turnErrorSummation, turnErrorPrevious, turnErrorCorrection = pidNeg(turnSteerLimit, turnError, 2.5, 0.0001, 1.4, 1, turnErrorSummation, turnErrorPrevious);

                    self.drivingMotor.run(turnSpeed);
                    self.steeringMotor.run_target(1000, turnErrorCorrection, Stop.HOLD, False);

        else:
            turnSpeedInitial *= -1;
            turnSpeedFinal *= -1;

            if (turnHeadingTarget > turnHeadingStart):
                turnSteerLimit *= -1;

                while (hub.imu.heading() < turnHeadingTarget):
                    turnError = turnHeadingTarget - hub.imu.heading();
                    turnSpeed = linearMap(turnError, turnHeadingDifference, 0, turnSpeedInitial, turnSpeedFinal);
                    turnErrorSummation, turnErrorPrevious, turnErrorCorrection = pidNeg(turnSteerLimit, turnError, 2.5, 0, 1.4, -1, turnErrorSummation, turnErrorPrevious);

                    self.drivingMotor.run(turnSpeed);
                    self.steeringMotor.run_target(1000, turnErrorCorrection, Stop.HOLD, False);

            else:
                while (hub.imu.heading() > turnHeadingTarget):
                    turnError = turnHeadingTarget - hub.imu.heading();
                    turnSpeed = linearMap(turnError, turnHeadingDifference, 0, turnSpeedInitial, turnSpeedFinal);
                    turnErrorSummation, turnErrorPrevious, turnErrorCorrection = pidPos(turnSteerLimit, turnError, 2.5, 0.0001, 1.4, -1, turnErrorSummation, turnErrorPrevious);

                    self.drivingMotor.run(turnSpeed);
                    self.steeringMotor.run_target(1000, turnErrorCorrection, Stop.HOLD, False);

        hub.speaker.beep(500);

    def turnDuration(self, turnDurationDuration, turnDurationHeadingTarget, turnDurationSteerLimit, turnDurationSpeedInitial, turnDurationSpeedFinal):
        turnDurationError, turnDurationSpeed, turnDurationErrorSummation, turnDurationErrorPrevious, turnDurationErrorCorrection = 0, 0, 0, 0, 0;

        turnDurationHeadingStart = hub.imu.heading();
        turnDurationHeadingDifference = turnDurationHeadingTarget - turnDurationHeadingStart;
        turnDurationMotorAngleStart = self.drivingMotor.angle();
        turnDurationMotorAngleTarget = turnDurationMotorAngleStart + turnDurationDuration;

        if (turnDurationDuration > 0):
            if (turnDurationHeadingTarget > turnDurationHeadingStart):
                while (self.drivingMotor.angle() < turnDurationMotorAngleTarget):
                    turnDurationSpeed = linearMap(self.drivingMotor.angle(), turnDurationMotorAngleStart, turnDurationMotorAngleTarget, turnDurationSpeedInitial, turnDurationSpeedFinal);
                    turnDurationErrorSummation, turnDurationErrorPrevious, turnDurationErrorCorrection = pidPos(turnDurationSteerLimit, (turnDurationHeadingTarget - hub.imu.heading()), 2.5, 0.0001, 1.4, 1, turnDurationErrorSummation, turnDurationErrorPrevious);

                    self.drivingMotor.run(turnDurationSpeed);
                    self.steeringMotor.run_target(1000, turnDurationErrorCorrection, Stop.HOLD, False);

            else:
                turnDurationSteerLimit *= -1;
                
                while (self.drivingMotor.angle() < turnDurationMotorAngleTarget):
                    turnDurationSpeed = linearMap(self.drivingMotor.angle(), turnDurationMotorAngleStart, turnDurationMotorAngleTarget, turnDurationSpeedInitial, turnDurationSpeedFinal);
                    turnDurationErrorSummation, turnDurationErrorPrevious, turnDurationErrorCorrection = pidNeg(turnDurationSteerLimit, (turnDurationHeadingTarget - hub.imu.heading()), 2.5, 0.0001, 1.4, 1, turnDurationErrorSummation, turnDurationErrorPrevious);

                    self.drivingMotor.run(turnDurationSpeed);
                    self.steeringMotor.run_target(1000, turnDurationErrorCorrection, Stop.HOLD, False);

        else:
            turnDurationSpeedInitial *= -1;
            turnDurationSpeedFinal *= -1;

            if (turnDurationHeadingTarget > turnDurationHeadingStart):
                turnDurationSteerLimit *= -1;

                while (self.drivingMotor.angle() > turnDurationMotorAngleTarget):
                    turnDurationSpeed = linearMap(self.drivingMotor.angle(), turnDurationMotorAngleStart, turnDurationMotorAngleTarget, turnDurationSpeedInitial, turnDurationSpeedFinal);
                    turnDurationErrorSummation, turnDurationErrorPrevious, turnDurationErrorCorrection = pidNeg(turnDurationSteerLimit, (turnDurationHeadingTarget - hub.imu.heading()), 2.5, 0, 1.4, -1, turnDurationErrorSummation, turnDurationErrorPrevious);

                    self.drivingMotor.run(turnDurationSpeed);
                    self.steeringMotor.run_target(1000, turnDurationErrorCorrection, Stop.HOLD, False);

            else:
                while (self.drivingMotor.angle() > turnDurationMotorAngleTarget):
                    turnDurationSpeed = linearMap(self.drivingMotor.angle(), turnDurationMotorAngleStart, turnDurationMotorAngleTarget, turnDurationSpeedInitial, turnDurationSpeedFinal);
                    turnDurationErrorSummation, turnDurationErrorPrevious, turnDurationErrorCorrection = pidPos(turnDurationSteerLimit, (turnDurationHeadingTarget - hub.imu.heading()), 2.5, 0.0001, 1.4, -1, turnDurationErrorSummation, turnDurationErrorPrevious);

                    self.drivingMotor.run(turnDurationSpeed);
                    self.steeringMotor.run_target(1000, turnDurationErrorCorrection, Stop.HOLD, False);

        hub.speaker.beep(500);

    def turnDetermineIfLine(self, turnIfLineHeadingTarget, turnIfLineSteerLimit, turnIfLineSpeedInitial, turnIfLineSpeedFinal):
        gcsSatHighest, turnIfLineError, turnIfLineSpeed, turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = 0, 0, 0, 0, 0, 0;

        turnIfLineHeadingStart = hub.imu.heading();
        turnIfLineHeadingDifference = turnIfLineHeadingTarget - turnIfLineHeadingStart;

        if (turnIfLineHeadingTarget > turnIfLineHeadingStart):
            turnIfLineHeadingTarget -= 12;

            while (hub.imu.heading() < turnIfLineHeadingTarget):
                turnIfLineError = turnIfLineHeadingTarget - hub.imu.heading();
                turnIfLineSpeed = linearMap(turnIfLineError, turnIfLineHeadingDifference, 0, turnIfLineSpeedInitial, turnIfLineSpeedFinal);
                turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = pidPos(turnIfLineSteerLimit, turnIfLineError, 2.5, 0.0001, 1.4, 1, turnIfLineErrorSummation, turnIfLineErrorPrevious);

                self.drivingMotor.run(turnIfLineSpeed);
                self.steeringMotor.run_target(1000, turnIfLineErrorCorrection, Stop.HOLD, False);

                if (colorSensorIntHSV(groundColorSensor, 1) > gcsSatHighest):
                    gcsSatHighest = colorSensorIntHSV(groundColorSensor, 1);

        else:
            turnIfLineSteerLimit *= -1;
            turnIfLineHeadingTarget += 12;

            while (hub.imu.heading() > turnIfLineHeadingTarget):
                turnIfLineError = turnIfLineHeadingTarget - hub.imu.heading();
                turnIfLineSpeed = linearMap(turnIfLineError, turnIfLineHeadingDifference, 0, turnIfLineSpeedInitial, turnIfLineSpeedFinal);
                turnIfLineErrorSummation, turnIfLineErrorPrevious, turnIfLineErrorCorrection = pidNeg(turnIfLineSteerLimit, turnIfLineError, 2.5, 0.0001, 1.4, 1, turnIfLineErrorSummation, turnIfLineErrorPrevious);

                self.drivingMotor.run(turnIfLineSpeed);
                self.steeringMotor.run_target(1000, turnIfLineErrorCorrection, Stop.HOLD, False);

                if (colorSensorIntHSV(groundColorSensor, 1) > gcsSatHighest):
                    gcsSatHighest = colorSensorIntHSV(groundColorSensor, 1);

        if (gcsSatHighest > 35):
            return "Line";
        else:
            return "No Line";

    def street(self, streetDuration, streetHeadingTarget, streetSpeedInitial, streetSpeedFinal):
        streetSpeed, streetErrorSummation, streetErrorPrevious, streetErrorCorrection = 0, 0, 0, 0;
        streetErrorKp, streetErrorKi, streetErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        if (streetDuration < 0):
            streetSpeedInitial *= -1;
            streetSpeedFinal *= -1;

        streetHeadingStart = hub.imu.heading();
        streetMotorAngleStart = self.drivingMotor.angle();
        streetMotorAngleTarget = streetMotorAngleStart + streetDuration;

        if (abs(streetHeadingTarget - streetHeadingStart) <= 30):
            if (streetDuration > 0):
                while (self.drivingMotor.angle() < streetMotorAngleTarget):
                    streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                    streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pid((streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, 1, streetErrorSummation, streetErrorPrevious);
                    
                    self.drivingMotor.run(streetSpeed);
                    self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);
                
            else:
                while (self.drivingMotor.angle() > streetMotorAngleTarget):
                    streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                    streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pid((streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, -1, streetErrorSummation, streetErrorPrevious);
                    
                    self.drivingMotor.run(streetSpeed);
                    self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);

        else:
            if (streetHeadingTarget > streetHeadingStart):
                if (streetDuration > 0):
                    while (self.drivingMotor.angle() < streetMotorAngleTarget):
                        streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidPos(30, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, 1, streetErrorSummation, streetErrorPrevious);
                        
                        self.drivingMotor.run(streetSpeed);
                        self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);
                    
                else:
                    while (self.drivingMotor.angle() > streetMotorAngleTarget):
                        streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidNeg(-30, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, -1, streetErrorSummation, streetErrorPrevious);
                        
                        self.drivingMotor.run(streetSpeed);
                        self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);

            else:
                if (streetDuration > 0):
                    while (self.drivingMotor.angle() < streetMotorAngleTarget):
                        streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidNeg(-30, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, 1, streetErrorSummation, streetErrorPrevious);
                        
                        self.drivingMotor.run(streetSpeed);
                        self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);
                    
                else:
                    while (self.drivingMotor.angle() > streetMotorAngleTarget):
                        streetSpeed = linearMap(self.drivingMotor.angle(), streetMotorAngleStart, streetMotorAngleTarget, streetSpeedInitial, streetSpeedFinal);
                        streetErrorSummation, streetErrorPrevious, streetErrorCorrection = pidPos(30, (streetHeadingTarget - hub.imu.heading()), streetErrorKp, streetErrorKi, streetErrorKd, -1, streetErrorSummation, streetErrorPrevious);
                        
                        self.drivingMotor.run(streetSpeed);
                        self.steeringMotor.run_target(1000, streetErrorCorrection, Stop.HOLD, False);

    def streetStall(self, streetStallDurationInitial, streetStallHeadingTarget, streetStallSpeedInitial, streetStallSpeedFinal, streetStallDurationFinal, streetStallTorque = 0):
        streetStallSpeed, streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = 0, 0, 0, 0;
        streetStallErrorKp, streetStallErrorKi, streetStallErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        streetStallMotorAngleStart = self.drivingMotor.angle();
        streetStallMotorAngleTarget = streetStallMotorAngleStart + streetStallDurationInitial;

        if (streetStallTorque == 0):
            if (streetStallDurationInitial > 0):
                streetStallTorque = 200;
            else:
                streetStallTorque = 300;

        if (streetStallDurationInitial > 0):
            while (self.drivingMotor.angle() < streetStallMotorAngleTarget):
                streetStallSpeed = linearMap(self.drivingMotor.angle(), streetStallMotorAngleStart, streetStallMotorAngleTarget, streetStallSpeedInitial, streetStallSpeedFinal);
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, streetStallErrorKi, streetStallErrorKd, 1, streetStallErrorSummation, streetStallErrorPrevious);

                self.drivingMotor.run(streetStallSpeed);
                self.steeringMotor.run_target(1000, streetStallErrorCorrection, Stop.HOLD, False);

            self.drivingMotor.control.limits(torque = streetStallTorque); # bawal ang 100
            self.drivingMotor.run(streetStallSpeedFinal);
            hub.speaker.beep(500);

            while (self.drivingMotor.speed() > 150):
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, streetStallErrorKi, streetStallErrorKd, 1, streetStallErrorSummation, streetStallErrorPrevious);

                self.steeringMotor.run_target(1000, streetStallErrorCorrection, Stop.HOLD, False);

        else:
            streetStallSpeedInitial *= -1;
            streetStallSpeedFinal *= -1;

            while (self.drivingMotor.angle() > streetStallMotorAngleTarget):
                streetStallSpeed = linearMap(self.drivingMotor.angle(), streetStallMotorAngleStart, streetStallMotorAngleTarget, streetStallSpeedInitial, streetStallSpeedFinal);
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, streetStallErrorKi, streetStallErrorKd, -1, streetStallErrorSummation, streetStallErrorPrevious);

                self.drivingMotor.run(streetStallSpeed);
                self.steeringMotor.run_target(1000, streetStallErrorCorrection, Stop.HOLD, False);

            self.drivingMotor.control.limits(torque = streetStallTorque);
            self.drivingMotor.run(streetStallSpeedFinal);
            hub.speaker.beep(500);

            while (self.drivingMotor.speed() < streetStallSpeedFinal / 1.5):
                streetStallErrorSummation, streetStallErrorPrevious, streetStallErrorCorrection = pid((streetStallHeadingTarget - hub.imu.heading()), streetStallErrorKp, streetStallErrorKi, streetStallErrorKd, -1, streetStallErrorSummation, streetStallErrorPrevious);

                self.steeringMotor.run_target(1000, streetStallErrorCorrection, Stop.HOLD, False);

        hub.speaker.beep(300, streetStallDurationFinal);
        self.drivingMotor.hold();
        self.drivingMotor.reset_angle(0);
        self.drivingMotor.control.limits(torque = 1000);
        hub.imu.reset_heading(0);

    def streetLine(self, streetLineDuration, streetLineHeadingTarget, streetLineSpeedInitial, streetLineSpeedFinal):
        streetLineSpeed, streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = 0, 0, 0, 0;
        streetLineErrorKp, streetLineErrorKi, streetLineErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        streetLineDirection = abs(streetLineDuration) / streetLineDuration;
        streetLineMotorAngleStart = self.drivingMotor.angle();
        streetLineMotorAngleTarget = streetLineMotorAngleStart + streetLineDuration;

        if (streetLineDuration > 0):
            while (self.drivingMotor.angle() < streetLineMotorAngleTarget):
                streetLineSpeed = linearMap(self.drivingMotor.angle(), streetLineMotorAngleStart, streetLineMotorAngleTarget, streetLineSpeedInitial, streetLineSpeedFinal);
                streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = pid(streetLineHeadingTarget - hub.imu.heading(), streetLineErrorKp, streetLineErrorKi, streetLineErrorKd, 1, streetLineErrorSummation, streetLineErrorPrevious);

                self.drivingMotor.run(streetLineSpeed);
                self.steeringMotor.run_target(1000, streetLineErrorCorrection, Stop.HOLD, False);

        else:
            streetLineSpeedInitial *= -1;
            streetLineSpeedFinal *= -1;

            while (self.drivingMotor.angle() > streetLineMotorAngleTarget):
                streetLineSpeed = linearMap(self.drivingMotor.angle(), streetLineMotorAngleStart, streetLineMotorAngleTarget, streetLineSpeedInitial, streetLineSpeedFinal);
                streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = pid(streetLineHeadingTarget - hub.imu.heading(), streetLineErrorKp, streetLineErrorKi, streetLineErrorKd, -1, streetLineErrorSummation, streetLineErrorPrevious);

                self.drivingMotor.run(streetLineSpeed);
                self.steeringMotor.run_target(1000, streetLineErrorCorrection, Stop.HOLD, False);
                
        self.drivingMotor.run(streetLineSpeedFinal);
        hub.speaker.beep(500);
        
        while (colorSensorIntHSV(groundColorSensor, 1) < 50):
            streetLineErrorSummation, streetLineErrorPrevious, streetLineErrorCorrection = pid(streetLineHeadingTarget - hub.imu.heading(), streetLineErrorKp, streetLineErrorKi, streetLineErrorKd, streetLineDirection, streetLineErrorSummation, streetLineErrorPrevious);

            self.steeringMotor.run_target(1000, streetLineErrorCorrection, Stop.HOLD, False);

    def streetDetect(self, streetDetectDuration, streetDetectHeadingTarget, streetDetectSpeed):
        streetDetectErrorSummation, streetDetectErrorPrevious, streetDetectErrorCorrection = 0, 0, 0;
        streetDetectErrorKp, streetDetectErrorKi, streetDetectErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        streetDetectMotorAngleStart = self.drivingMotor.angle();
        streetDetectMotorAngleTarget = streetDetectMotorAngleStart + streetDetectDuration;
        streetDetectValue = "None";

        hub.speaker.beep(500);

        if (streetDetectDuration > 0):
            self.drivingMotor.run(streetDetectSpeed);

            while (self.drivingMotor.angle() < streetDetectMotorAngleTarget):
                streetDetectErrorSummation, streetDetectErrorPrevious, streetDetectErrorCorrection = pid((streetDetectHeadingTarget - hub.imu.heading()), streetDetectErrorKp, streetDetectErrorKi, streetDetectErrorKd, 1, streetDetectErrorSummation, streetDetectErrorPrevious);
                self.steeringMotor.run_target(1000, streetDetectErrorCorrection, Stop.HOLD, False);

                if (colorSensorIntHSV(cameraColorSensor, 1) > 50):
                    if (colorSensorIntHSV(cameraColorSensor, 2) > self.trafficSignMidpoint):
                        streetDetectValue = "Green";
                    else:
                        streetDetectValue = "Red";

        else:
            self.drivingMotor.run(0 - streetDetectSpeed);

            while (self.drivingMotor.angle() > streetDetectMotorAngleTarget):
                streetDetectErrorSummation, streetDetectErrorPrevious, streetDetectErrorCorrection = pid((streetDetectHeadingTarget - hub.imu.heading()), streetDetectErrorKp, streetDetectErrorKi, streetDetectErrorKd, -1, streetDetectErrorSummation, streetDetectErrorPrevious);
                self.steeringMotor.run_target(1000, streetDetectErrorCorrection, Stop.HOLD, False);

                if (colorSensorIntHSV(cameraColorSensor, 1) > 50):
                    if (colorSensorIntHSV(cameraColorSensor, 2) > self.trafficSignMidpoint):
                        streetDetectValue = "Green";
                    else:
                        streetDetectValue = "Red";

        hub.speaker.beep(500);
        
        return streetDetectValue;

    def streetDetermineTheLine(self, streetTheLineHeadingTarget, streetTheLineSpeed):
        gcsSat, gcsHue, gcsHueHighest, streetTheLineErrorSummation, streetTheLineErrorPrevious, streetTheLineErrorCorrection = 0, 0, 0, 0, 0, 0;
        streetTheLineErrorKp, streetTheLineErrorKi, streetTheLineErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        streetTheLineDirection = abs(streetTheLineSpeed) / streetTheLineSpeed;

        self.drivingMotor.run(streetTheLineSpeed);

        while True:
            streetTheLineErrorSummation, streetTheLineErrorPrevious, streetTheLineErrorCorrection = pid((streetTheLineHeadingTarget - hub.imu.heading()), streetTheLineErrorKp, streetTheLineErrorKi, streetTheLineErrorKd, streetTheLineDirection, streetTheLineErrorSummation, streetTheLineErrorPrevious);
            self.steeringMotor.run_target(1000, streetTheLineErrorCorrection, Stop.HOLD, False);

            gcsSat = colorSensorIntHSV(groundColorSensor, 1);

            if (gcsSat > 30):
                while (gcsSat > 15):
                    gcsHue = colorSensorIntHSV(groundColorSensor, 0);
                    gcsSat = colorSensorIntHSV(groundColorSensor, 1);

                    if (gcsHue > gcsHueHighest):
                        hub.speaker.beep(500);
                        gcsHueHighest = gcsHue;
                    
                break;

        hub.speaker.beep(500);

        if (gcsHueHighest > 190 and gcsHueHighest < 290):
            return -1;
        else:
            return 1;

    def streetDetermineIfLine(self, streetIfLineDuration, streetIfLineHeadingTarget, streetIfLineSpeed):
        gcsSat, gcsSatHighest, streetIfLineErrorSummation, streetIfLineErrorPrevious, streetIfLineErrorCorrection = 0, 0, 0, 0, 0;
        streetIfLineErrorKp, streetIfLineErrorKi, streetIfLineErrorKd = self.streetErrorKp, self.streetErrorKi, self.streetErrorKd;

        streetIfLineMotorAngleStart = self.drivingMotor.angle();
        streetIfLineMotorAngleTarget = streetIfLineMotorAngleStart + streetIfLineDuration;
        
        self.drivingMotor.run(streetIfLineSpeed);

        while (self.drivingMotor.angle() < streetIfLineMotorAngleTarget):
            streetIfLineErrorSummation, streetIfLineErrorPrevious, streetIfLineErrorCorrection = pid((streetIfLineHeadingTarget - hub.imu.heading()), streetIfLineErrorKp, streetIfLineErrorKi, streetIfLineErrorKd, 1, streetIfLineErrorSummation, streetIfLineErrorPrevious);
            self.steeringMotor.run_target(1000, streetIfLineErrorCorrection, Stop.HOLD, False);

            gcsSat = colorSensorIntHSV(groundColorSensor, 1);

            if (gcsSat > gcsSatHighest):
                gcsSatHighest = gcsSat;

        if (gcsSatHighest > 35):
            return "Line";
        else:
            return "No Line";

    def drive(self, driveDuration, driveSpeedInitial, driveSpeedFinal, driveSteerInitial, driveSteerFinal):
        driveSpeed, driveSteer = 0, 0;

        driveMotorAngleStart = self.drivingMotor.angle();
        driveMotorAngleTarget = driveMotorAngleStart + driveDuration;

        if (driveSteerInitial != driveSteerFinal):
            if (driveDuration > 0):
                while (self.drivingMotor.angle() < driveMotorAngleTarget):
                    driveSpeed = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal);
                    driveSteer = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSteerInitial, driveSteerFinal);

                    self.drivingMotor.run(driveSpeed);
                    self.steeringMotor.run_target(1000, driveSteer, Stop.HOLD, False);

            else:
                while (self.drivingMotor.angle() > driveMotorAngleTarget):
                    driveSpeed = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal);
                    driveSteer = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSteerInitial, driveSteerFinal);

                    self.drivingMotor.run(driveSpeed);
                    self.steeringMotor.run_target(1000, driveSteer, Stop.HOLD, False);

        else:
            if (driveDuration > 0):
                while (self.drivingMotor.angle() < driveMotorAngleTarget):
                    driveSpeed = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal);

                    self.drivingMotor.run(driveSpeed);
                    self.steeringMotor.run_target(1000, driveSteerInitial, Stop.HOLD, False);

            else:
                while (self.drivingMotor.angle() > driveMotorAngleTarget):
                    driveSpeed = linearMap(self.drivingMotor.angle(), driveMotorAngleStart, driveMotorAngleTarget, driveSpeedInitial, driveSpeedFinal);

                    self.drivingMotor.run(driveSpeed);
                    self.steeringMotor.run_target(1000, driveSteerInitial, Stop.HOLD, False);

    def driveLine(self, driveLineDuration, driveLineSpeedInitial, driveLineSpeedFinal, driveLineSteerInitial, driveLineSteerFinal):
        driveLineSpeed, driveLineSteer = 0, 0;
        
        driveLineMotorAngleStart = self.drivingMotor.angle();
        driveLineMotorAngleTarget = driveLineMotorAngleStart + driveLineDuration;

        if (driveLineSteerInitial != driveLineSteerFinal):
            if (driveLineDuration > 0):
                while (self.drivingMotor.angle() < driveLineMotorAngleTarget):
                    driveLineSpeed = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSpeedInitial, driveLineSpeedFinal);
                    driveLineSteer = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSteerInitial, driveLineSteerFinal);

                    self.drivingMotor.run(driveLineSpeed);
                    self.steeringMotor.run_target(1000, driveLineSteer, Stop.HOLD, False);

            else:
                while (self.drivingMotor.angle() > driveLineMotorAngleTarget):
                    driveLineSpeed = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSpeedInitial, driveLineSpeedFinal);
                    driveLineSteer = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSteerInitial, driveLineSteerFinal);

                    self.drivingMotor.run(driveLineSpeed);
                    self.steeringMotor.run_target(1000, driveLineSteer, Stop.HOLD, False);

        else:
            if (driveLineDuration > 0):
                while (self.drivingMotor.angle() < driveLineMotorAngleTarget):
                    driveLineSpeed = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSpeedInitial, driveLineSpeedFinal);

                    self.drivingMotor.run(driveLineSpeed);
                    self.steeringMotor.run_target(1000, driveLineSteerInitial, Stop.HOLD, False);

            else:
                while (self.drivingMotor.angle() > driveLineMotorAngleTarget):
                    driveLineSpeed = linearMap(self.drivingMotor.angle(), driveLineMotorAngleStart, driveLineMotorAngleTarget, driveLineSpeedInitial, driveLineSpeedFinal);

                    self.drivingMotor.run(driveLineSpeed);
                    self.steeringMotor.run_target(1000, driveLineSteerInitial, Stop.HOLD, False);

        self.drivingMotor.run(driveLineSpeedFinal);
        self.steeringMotor.run_target(1000, driveLineSteerFinal, Stop.HOLD, False);
        hub.speaker.beep(500);

        while (colorSensorIntHSV(groundColorSensor, 1) < 50):
            pass;

    def motorClose(self):
        self.drivingMotor.close();
        self.steeringMotor.close();
        self.visionMotor.close();

    def hold(self):
        self.drivingMotor.hold();
        wait(500);
        e

    def cameraScan(self, cameraScanAngle, cameraScanSpeed):
        # cameraScanHueLowest = colorSensorIntHSV(cameraColorSensor, 0);
        cameraScanSatHighest = colorSensorIntHSV(cameraColorSensor, 1);
        cameraScanValLowest = colorSensorIntHSV(cameraColorSensor, 2);
        
        if (self.visionMotor.angle() < cameraScanAngle):
            while (self.visionMotor.angle() < (cameraScanAngle - 2)):
                self.visionMotor.run_target(cameraScanSpeed, cameraScanAngle, Stop.HOLD, False);

                cameraScanSat = colorSensorIntHSV(cameraColorSensor, 1);
                cameraScanVal = colorSensorIntHSV(cameraColorSensor, 2);
                
                # if (colorSensorIntHSV(cameraColorSensor, 0) < cameraScanHueLowest):
                #     cameraScanHueLowest = colorSensorIntHSV(cameraColorSensor, 0);
                if (cameraScanSat > cameraScanSatHighest):
                    cameraScanSatHighest = cameraScanSat;
                if (cameraScanVal < cameraScanValLowest):
                    cameraScanValLowest = cameraScanVal;

                hub.speaker.beep(500);

        else:
            while (self.visionMotor.angle() > (cameraScanAngle + 2)):
                self.visionMotor.run_target(cameraScanSpeed, cameraScanAngle, Stop.HOLD, False);

                cameraScanSat = colorSensorIntHSV(cameraColorSensor, 1);
                cameraScanVal = colorSensorIntHSV(cameraColorSensor, 2);

                # if (colorSensorIntHSV(cameraColorSensor, 0) < cameraScanHueLowest):
                #     cameraScanHueLowest = colorSensorIntHSV(cameraColorSensor, 0);
                if (cameraScanSat > cameraScanSatHighest):
                    cameraScanSatHighest = cameraScanSat;
                if (cameraScanVal < cameraScanValLowest):
                    cameraScanValLowest = cameraScanVal;

                hub.speaker.beep(500);

        if (cameraScanSatHighest > 50):
            if (cameraScanValLowest > self.trafficSignMidpoint):
                return "Green";
            else:
                return "Red";
        else:
            return "None";