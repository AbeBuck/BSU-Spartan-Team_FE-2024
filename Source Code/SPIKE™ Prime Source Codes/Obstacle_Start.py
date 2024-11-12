from FE_Functions import *

def hubCustomDisplay(hubCustomDisplayHub, hubCustomDisplayIcon):
    hubCustomDisplayBrightness = list(range(0, 100, 10)) + list(range(100, 0, -10))
    hubCustomDisplayHub.display.animate([hubCustomDisplayIcon * i / 100 for i in hubCustomDisplayBrightness], 30);

def hubCustomLight(hubCustomLightHub, hubCustomLightColor):
    hubCustomLightBrightness = list(range(0, 10, 1)) + list(range(10, 0, -1));
    hubCustomLightHub.light.animate([hubCustomLightColor * (0.5 * sin(i / 15 * pi) + 0.5) for i in hubCustomLightBrightness], 40);

def obstacleStart():
    driveMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 500);
    steerMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1], False, 5);
    visionMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5);

    selfDrivingCar = FutureEngineers(steerMotor, driveMotor, visionMotor);

    _robotDirection, linePresence, parkingPresence, trafficSign = 0, "", "", "";
    
    hub.imu.reset_heading(0);
    driveMotor.reset_angle(0);
    driveMotor.hold();
    steerMotor.run_target(1000, 0, Stop.HOLD, False);
    timer.reset();

    visionMotor.run_until_stalled(-1000, Stop.HOLD);
    distanceLeft = distanceSensor.distance();
    visionMotor.run_until_stalled(1000, Stop.HOLD);
    distanceRight = distanceSensor.distance();

    print("Left/Right:", distanceLeft, distanceRight);

    # 52    776
    # 446   389
    # 2000  48

    # 2000 47

    # kapag nLeftStart fParking, dist = 400

    if (distanceLeft < 200):
        print("LEFT", end = " ");

        linePresence = selfDrivingCar.streetDetermineIfLine(200, 0, 600);
        driveMotor.hold();
        print(linePresence)

        if (linePresence == "Line"):
            visionMotor.run_target(1000, 100, Stop.HOLD, False);
            selfDrivingCar.street(-140, 0, 650, 600);
            
            trafficSign = trafficSignColor();
            print(trafficSign, end = " ");

            selfDrivingCar.street(-240, 0, 610, 600);

        else:
            selfDrivingCar.street(-250, 0, 650, 600);

        selfDrivingCar.street(-160, 0, 600, 550);
        driveMotor.hold();

        visionMotor.run_target(1000, -91, Stop.HOLD, False);
        selfDrivingCar.turn(1, 90, 30, 750, 650);
        driveMotor.hold();

        if (trafficSign == ""):
            trafficSign = selfDrivingCar.streetDetect(-50, 90, 380);
            driveMotor.hold();

            if (trafficSign == "None"):
                print("false", trafficSign);
                wait(200);
                trafficSign = trafficSignColor();

            print(trafficSign);

        else:
            selfDrivingCar.streetDetect(-50, 90, 380);
            driveMotor.hold();

        if (trafficSign == "Red"):
            # LEFT Red

            visionMotor.run_target(1000, 0, Stop.HOLD, False);
            selfDrivingCar.streetStall(-200, 90, 500, 350, 500);

            visionMotor.run_target(1000, -100, Stop.HOLD, False);
            selfDrivingCar.street(840, 2, 750, 550);
            driveMotor.hold();

            parkingPresence = ifParking(600);

            if (parkingPresence == "Parking"):
                print("PARKING COUNTERCLOCKWISE");
                _robotDirection = -1;

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(-560, 0, 700, 500);
                driveMotor.hold();

                selfDrivingCar.turn(1, -90, 30, 750, 450);
                selfDrivingCar.streetLine(1, -90, 750, 750);
                hubCustomLight(hub, Color.BLUE);
                
                selfDrivingCar.street(250, -130, 800, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.streetStall(300, -90, 700, 600, 500);
                
            else:
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(-200, 0, 600, 500);
                selfDrivingCar.smartStop(0);
                driveMotor.reset_angle(0);

                linePresence = selfDrivingCar.turnDetermineIfLine(-90, 30, 750, 400);
                print(linePresence, end = " ");

                if (linePresence == "Line"):
                    _robotDirection = 1;
                else:
                    _robotDirection = selfDrivingCar.streetDetermineTheLine(-90, 700);
                
                if (_robotDirection == -1):
                    print("NORMAL COUNTERCLOCKWISE");

                    driveMotor.hold();
                    hubCustomLight(hub, Color.BLUE);
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-600, -90, 700, 600);
                    driveMotor.hold();
                    
                    selfDrivingCar.turn(1, -150, 30, 850, 750);
                    selfDrivingCar.street(120, -150, 800, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 700);
                    selfDrivingCar.streetStall(10, -90, 550, 500, 500);

                else:
                    print("CLOCKWISE");
                    
                    hubCustomLight(hub, Color.ORANGE);
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -140, 30, 850, 750);
                    selfDrivingCar.street(30, -140, 800, 700);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 600);
                    selfDrivingCar.streetStall(10, -90, 550, 500, 500);

        else:
            # LEFT Green

            visionMotor.run_target(1000, 0, Stop.HOLD, False);
            selfDrivingCar.turn(-1, 10, 55, 650, 450);
            selfDrivingCar.smartStop(0);

            parkingPresence = ifParking(650);

            if (parkingPresence == "Parking"):
                print("PARKING CLOCKWISE");
                _robotDirection = 1;

                selfDrivingCar.turn(1, 40, 30, 750, 500);
                selfDrivingCar.street(190, 40, 600, 550);
                selfDrivingCar.turn(1, 0, 40, 750, 550);
                selfDrivingCar.streetLine(300, 0, 850, 800);

                hubCustomLight(hub, Color.ORANGE);                
                selfDrivingCar.turn(1, 35, 30, 850, 750);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 0, 30, 750, 600);
                selfDrivingCar.streetStall(50, 0, 580, 540, 500);
                
            else:
                _robotDirection = selfDrivingCar.streetDetermineTheLine(-2, 800);

                if (_robotDirection == 1):
                    print("NORMAL CLOCKWISE");
                    
                    driveMotor.hold();
                    hubCustomLight(hub, Color.ORANGE);
                    selfDrivingCar.street(-600, 0, 700, 600);
                    driveMotor.hold();
                    
                    selfDrivingCar.turn(1, 40, 30, 850, 750);
                    selfDrivingCar.street(210, 40, 800, 700);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 0, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 0, 550, 500, 500);
                    
                else:
                    print("COUNTERCLOCKWISE");

                    hubCustomLight(hub, Color.BLUE);
                    selfDrivingCar.turn(1, 40, 30, 850, 750);
                    selfDrivingCar.street(200, 40, 800, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 0, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 0, 550, 500, 600);

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        
    elif (distanceRight < 200):
        print("RIGHT", end = " ");

        linePresence = selfDrivingCar.streetDetermineIfLine(200, 0, 600);
        driveMotor.hold();
        print(linePresence)

        if (linePresence == "Line"):
            visionMotor.run_target(1000, -100, Stop.HOLD, False);
            selfDrivingCar.street(-140, 0, 650, 600);
            
            trafficSign = trafficSignColor();
            print(trafficSign, end = " ");

            selfDrivingCar.street(-290, 0, 610, 600);

        else:
            selfDrivingCar.street(-300, 0, 650, 600);

        selfDrivingCar.street(-160, 0, 600, 550);
        driveMotor.hold();

        visionMotor.run_target(1000, 91, Stop.HOLD, False);
        selfDrivingCar.turn(1, -90, 30, 750, 650);
        driveMotor.hold();

        if (trafficSign == ""):
            trafficSign = selfDrivingCar.streetDetect(-200, -90, 380);
            driveMotor.hold();

            if (trafficSign == "None"):
                print("false", trafficSign);
                wait(200);
                trafficSign = trafficSignColor();

            print(trafficSign);

        else:
            selfDrivingCar.streetDetect(-150, -90, 380);
            driveMotor.hold();

        if (trafficSign == "Green"):
            # RIGHT GREEN

            visionMotor.run_target(1000, 0, Stop.HOLD, False);
            selfDrivingCar.streetStall(-100, -90, 650, 350, 500);

            visionMotor.run_target(1000, 100, Stop.HOLD, False);
            selfDrivingCar.street(810, 0, 750, 550);
            driveMotor.hold();

            parkingPresence = ifParking(600);

            if (parkingPresence == "Parking"):
                print("PARKING CLOCKWISE");
                _robotDirection = 1;

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(-550, 0, 700, 500);
                driveMotor.hold();

                selfDrivingCar.turn(1, 89, 30, 750, 450); # dapat 90 heading
                selfDrivingCar.streetLine(1, 85, 750, 750); # ^^^
                hubCustomLight(hub, Color.ORANGE);
                
                selfDrivingCar.street(100, 120, 850, 800);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.streetStall(400, 90, 800, 600, 500);
                
            else:
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(-200, 0, 600, 500);
                selfDrivingCar.smartStop(0);
                driveMotor.reset_angle(0);

                linePresence = selfDrivingCar.turnDetermineIfLine(87, 30, 750, 400); # dapat 90 heading
                print(linePresence, end = " ");

                if (linePresence == "Line"):
                    _robotDirection = -1;
                else:
                    _robotDirection = selfDrivingCar.streetDetermineTheLine(82, 700); # ^^^
                
                if (_robotDirection == 1):
                    print("NORMAL CLOCKWISE");

                    driveMotor.hold();
                    hubCustomLight(hub, Color.ORANGE);
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-550, 90, 700, 600);
                    driveMotor.hold();
                    
                    selfDrivingCar.turn(1, 130, 30, 850, 750);
                    selfDrivingCar.street(130, 130, 800, 700);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 90, 550, 500, 500);

                else:
                    print("COUNTERCLOCKWISE");
                    
                    hubCustomLight(hub, Color.BLUE);
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 130, 30, 850, 750);
                    selfDrivingCar.street(100, 130, 800, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 90, 550, 500, 500);

        else:
            # RIGHT RED

            visionMotor.run_target(1000, 0, Stop.HOLD, False);
            selfDrivingCar.street(50, -90, 400, 350);
            selfDrivingCar.turn(-1, -1, 55, 650, 450);
            selfDrivingCar.smartStop(0);

            parkingPresence = ifParking(650);

            if (parkingPresence == "Parking"):
                print("PARKING COUNTERCLOCKWISE");
                _robotDirection = -1;

                selfDrivingCar.turn(1, -40, 30, 750, 500);
                selfDrivingCar.street(180, -40, 600, 550);
                selfDrivingCar.turn(1, -2, 40, 750, 550);
                selfDrivingCar.streetLine(300, -5, 850, 800);

                hubCustomLight(hub, Color.BLUE);                
                selfDrivingCar.turn(1, -35, 30, 850, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 0, 30, 850, 650);
                selfDrivingCar.streetStall(100, 0, 620, 600, 500);
                
            else:
                _robotDirection = selfDrivingCar.streetDetermineTheLine(-4, 800);

                if (_robotDirection == -1):
                    print("NORMAL COUNTERCLOCKWISE");
                    
                    driveMotor.hold();
                    hubCustomLight(hub, Color.BLUE);
                    selfDrivingCar.street(-600, 0, 700, 600);
                    driveMotor.hold();
                    
                    selfDrivingCar.turn(1, -50, 30, 850, 750);
                    selfDrivingCar.street(250, -50, 800, 700);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 0, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 0, 550, 500, 500);
                    
                else:
                    print("CLOCKWISE");

                    hubCustomLight(hub, Color.ORANGE);
                    selfDrivingCar.turn(1, -50, 30, 850, 750);
                    selfDrivingCar.street(250, -50, 800, 700);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 0, 30, 750, 700);
                    selfDrivingCar.streetStall(10, 0, 550, 500, 600);

    else:
        print("MIDDLE", end = " ");

        timer.reset();

        while (timer.time() < 800):
            steerMotor.run_target(1000, 0, Stop.HOLD, False);
            visionMotor.run_target(1000, 0, Stop.HOLD, False);

        hub.speaker.beep(500);
        timer.reset();

        _robotDirection = 0;
        _distanceLowest = 2000;

        while (timer.time() < 500):
            if (distanceSensor.distance() < _distanceLowest):
                _distanceLowest = distanceSensor.distance();

            wait(50);

        print("FINAL: ", _distanceLowest);

        if (_distanceLowest < 1150 and _distanceLowest > 850):
            print("Laps: 0\t\t\b\b\b\b\bfStart");

            errorSummation = 0;
            errorPrevious = 0;
            driveMotor.run(1000);

            while True:
                errorSummation, errorPrevious, errorCorrection = pid((0 - hub.imu.heading()), 0.8, 0.000005, 0.7, 1, errorSummation, errorPrevious);
                steerMotor.run_target(1000, errorCorrection, Stop.HOLD, False);

                groundColorSensorSat = colorSensorIntHSV(groundColorSensor, 1);

                if (groundColorSensorSat > 30):
                    groundColorSensorHueHighest = 0;

                    while (groundColorSensorSat > 15):
                        groundColorSensorHue = colorSensorIntHSV(groundColorSensor, 0);
                        groundColorSensorSat = colorSensorIntHSV(groundColorSensor, 1);

                        if (groundColorSensorHue > groundColorSensorHueHighest):
                            hub.speaker.beep(500);
                            groundColorSensorHueHighest = groundColorSensorHue;

                    break;

            hub.speaker.beep(500);
            
            if (groundColorSensorHueHighest > 190 and groundColorSensorHueHighest < 290):
                _robotDirection = -1;
                hubCustomLight(hub, Color.BLUE);
            else:
                _robotDirection = 1;
                hubCustomLight(hub, Color.ORANGE);

            visionMotor.run_target(1000, 90 * _robotDirection, Stop.HOLD, False);
            selfDrivingCar.street(500, 0, 800, 500);
            selfDrivingCar.streetStall(150, 0, 500, 450, 500);

        else:
            trafficSign = trafficSignColor();
            print("Laps: 0\t\t\b\b\b\bnStart", trafficSign.upper(), end = " ");

            if (trafficSign == "Red"):
                # Red

                selfDrivingCar.street(265, 0, 800, 750);
                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 89, 30, 750, 350);
                selfDrivingCar.streetStall(1, 92, 350, 300, 500);
                
                parkingPresence = ifParking(400);

                if (parkingPresence == "Parking"):
                    # Red Parking Counterclockwise

                    print("PARKING COUNTERCLOCKWISE");
                    _robotDirection = -1;

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-570, 0, 700, 500);
                    driveMotor.hold();

                    selfDrivingCar.turn(1, -90, 30, 750, 450);
                    selfDrivingCar.streetLine(1, -90, 850, 850);
                    hubCustomLight(hub, Color.BLUE);
                    
                    selfDrivingCar.street(230, -130, 850, 800);
                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.streetStall(300, -90, 850, 650, 500);
                    
                else:
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-280, 0, 600, 500);
                    selfDrivingCar.smartStop(0);

                    linePresence = selfDrivingCar.turnDetermineIfLine(-90, 30, 750, 650);
                    print(linePresence, end = " ");
                    
                    if (linePresence == "No Line"):
                        linePresence = selfDrivingCar.streetDetermineIfLine(50, -90, 650);
                    else:
                        selfDrivingCar.street(50, -90, 650, 650);

                    if (linePresence == "Line"):
                        # Red Clockwise

                        print("CLOCKWISE");
                        _robotDirection = 1;

                        visionMotor.run_target(1000, 0, Stop.HOLD, False);
                        hubCustomLight(hub, Color.ORANGE);
                        selfDrivingCar.turn(1, -130, 30, 750, 650);
                        selfDrivingCar.street(350, -130, 800, 750);
                        visionMotor.run_target(1000, 100, Stop.HOLD, False);
                        selfDrivingCar.turn(1, -90, 30, 750, 500);
                        selfDrivingCar.streetStall(10, -90, 700, 600, 500);

                    else:
                        # Red Normal Counterclockwise

                        print("NORMAL COUNTERCLOCKWISE");
                        _robotDirection = -1;

                        visionMotor.run_target(1000, 0, Stop.HOLD, False);
                        hubCustomLight(hub, Color.BLUE);
                        selfDrivingCar.turn(1, -130, 30, 750, 450);
                        selfDrivingCar.street(370, -130, 800, 750);
                        visionMotor.run_target(1000, -100, Stop.HOLD, False);
                        selfDrivingCar.turn(1, -90, 30, 750, 500);
                        selfDrivingCar.streetStall(10, -90, 700, 600, 500);

            elif (trafficSign == "Green" or trafficSign == "None"):
                # Green

                selfDrivingCar.street(240, 0, 800, 750);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.turn(1, -89, 32, 750, 350);
                selfDrivingCar.streetStall(1, -92, 350, 300, 500);
                
                parkingPresence = ifParking(400);

                if (parkingPresence == "Parking"):
                    # Green Parking Clockwise

                    print("PARKING CLOCKWISE");
                    _robotDirection = 1;

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-530, 0, 700, 500);
                    driveMotor.hold();

                    selfDrivingCar.turn(1, 90, 30, 750, 450);
                    selfDrivingCar.streetLine(100, 90, 850, 800);
                    hubCustomLight(hub, Color.ORANGE);
                    
                    # selfDrivingCar.street(200, 115, 850, 800);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.streetStall(400, 90, 800, 600, 500, 300);

                else:
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(-280, 0, 700, 500);
                    selfDrivingCar.smartStop(0);
                    
                    linePresence = selfDrivingCar.turnDetermineIfLine(90, 30, 750, 650);
                    print(linePresence, end = " ");
                    
                    if (linePresence == "No Line"):
                        linePresence = selfDrivingCar.streetDetermineIfLine(50, 90, 650);
                    else:
                        selfDrivingCar.street(50, 90, 650, 650);

                    if (linePresence == "Line"):
                        # Green Counterclockwise

                        print("COUNTERCLOCKWISE");
                        _robotDirection = -1;

                        visionMotor.run_target(1000, 0, Stop.HOLD, False);
                        hubCustomLight(hub, Color.BLUE);
                        selfDrivingCar.turn(1, 120, 30, 750, 450);
                        selfDrivingCar.street(300, 120, 800, 750);
                        visionMotor.run_target(1000, -100, Stop.HOLD, False);
                        selfDrivingCar.turn(1, 90, 30, 750, 600);
                        selfDrivingCar.streetStall(100, 90, 700, 600, 500);

                    else:
                        # Green Normal Clockwise

                        print("NORMAL CLOCKWISE");
                        _robotDirection = 1;

                        visionMotor.run_target(1000, 0, Stop.HOLD, False);
                        hubCustomLight(hub, Color.ORANGE);
                        selfDrivingCar.turn(1, 120, 30, 750, 450);
                        selfDrivingCar.street(370, 120, 800, 750);
                        visionMotor.run_target(1000, 100, Stop.HOLD, False);
                        selfDrivingCar.turn(1, 90, 30, 750, 500);
                        selfDrivingCar.streetStall(10, 90, 700, 600, 500);

    selfDrivingCar.motorClose();

    return _robotDirection;
    
# obstacleStart();