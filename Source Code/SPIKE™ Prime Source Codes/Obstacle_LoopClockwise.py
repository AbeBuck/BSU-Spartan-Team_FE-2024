from FE_Functions import *

def obstacleLoopClockwise(recordListInput):
    driveMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [1], False, 500);
    steerMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [1], False, 5);
    visionMotor = Motor(Port.E, Direction.CLOCKWISE, [1], False, 5);
    
    selfDrivingCar = FutureEngineers(steerMotor, driveMotor, visionMotor);

    parkingPresence, trafficSign, recordListValue = "", "", [];

    timer.reset();
    # steerMotor.run_target(1000, 0, Stop.HOLD, True);
    visionMotor.run_target(1000, 100, Stop.HOLD, False);

    if (recordListInput == ["", "", "", ""]):
        parkingPresence = ifParking(650);
        recordListValue.append(parkingPresence);
        print("n" + parkingPresence, end = " ");
    else:
        parkingPresence = recordListInput[0];

    selfDrivingCar.street(-400, 0, 650, 600);
    trafficSign = selfDrivingCar.streetDetect(-100, 0, 600); # dapat ay total of -500

    if (recordListInput == ["", "", "", ""]):
        if (trafficSign == "None"):
            print("false", end = " ");
            trafficSign = trafficSignColor();

        recordListValue.append(trafficSign);
        print("n" + trafficSign, end = " ");
    else:
        trafficSign = recordListInput[1];

    if (trafficSign == "Red"):
        # n? nRed

        selfDrivingCar.smartStop(0);
        selfDrivingCar.street(50, 0, 300, 290);
        driveMotor.hold();
        visionMotor.run_target(1000, 0, Stop.HOLD, False);
        selfDrivingCar.turn(-1, 76, 65, 900, 550);
        selfDrivingCar.streetStall(-100, 90, 700, 650, 800);
        selfDrivingCar.street(950, 0, 900, 750);

        if (recordListInput == ["", "", "", ""] or recordListInput[3] == "Green"):
            visionMotor.run_target(1000, 100, Stop.HOLD, False);
            selfDrivingCar.turn(1, -95, 30, 850, 750);
            # selfDrivingCar.turn(1, -90, 30, 750, 700)
            selfDrivingCar.streetStall(200, -90, 700, 500, 800);

            if (recordListInput == ["", "", "", ""]):
                if (parkingPresence == "Normal"):
                    parkingPresence = ifParking(600);
                    parkingPresenceBypass = 0;
                else:
                    parkingPresence = "Normal";
                    parkingPresenceBypass = 1;
                
                recordListValue.append(parkingPresence);
                print("f" + parkingPresence, end = " ");

            else:
                if (parkingPresence == "Normal"):
                    parkingPresenceBypass = 0;
                else:
                    parkingPresenceBypass = 1;

                parkingPresence = recordListInput[2];

            selfDrivingCar.street(-350, 6, 800, 600);
            trafficSign = selfDrivingCar.streetDetect(-180, 0, 600); # dapat ay total of -530

            if (recordListInput == ["", "", "", ""]):
                if (trafficSign == "None"):
                    print("false", end = " ");
                    trafficSign = trafficSignColor();
                
                recordListValue.append(trafficSign);
                print("f" + trafficSign);
            else:
                trafficSign = recordListInput[3];

            if (trafficSign == "Red" or trafficSign == "None"):
                # nNormal nRed fNormal fRed
                # nParking nRed fNormal fRed
                # nNormal nRed fParking fRed

                driveMotor.hold();
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(10, 0, 300, 290);
                driveMotor.hold();
                selfDrivingCar.turn(-1, 86, 65, 800, 450);
                selfDrivingCar.smartStop(90);
                selfDrivingCar.streetLine(700, 90, 900, 850);

        else:
            # nNormal nRed f? fRed/None
            # nParking nRed f? fRed/None

            selfDrivingCar.street(60, 15, 800, 750);
            selfDrivingCar.streetLine(350, 0, 900, 850);
            hub.imu.reset_heading(90);

        if (trafficSign == "Red" or trafficSign == "None"):
            selfDrivingCar.turn(1, 50, 30, 850, 550);
            selfDrivingCar.street(470, 60, 850, 750);
            visionMotor.run_target(1000, 100, Stop.HOLD, False);
            selfDrivingCar.turn(1, 90, 30, 750, 550);
            selfDrivingCar.streetStall(50, 90, 550, 500, 500);

        else:
            # nNormal nRed f? fGreen
            # nParking nRed f? fGreen

            if ((parkingPresence == "Parking") or parkingPresenceBypass):
                # nParking nRed fNormal fGreen
                # nNormal nRed fParking fGreen

                # selfDrivingCar.street(-50, 0, 620, 600);
                driveMotor.hold();
                # selfDrivingCar.street(1, 0, 800, 750);
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 30, 750, 450);
                selfDrivingCar.street(100, 80, 850, 800);
                selfDrivingCar.streetLine(500, 90, 900, 850);

                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.street(400, 90, 800, 750);
                selfDrivingCar.streetStall(200, 90, 750, 550, 500);

            else:
                # nNormal nRed fNormal fGreen

                driveMotor.hold();
                selfDrivingCar.street(180, 0, 900, 850);
                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.turn(1, 85, 30, 850, 750);
                selfDrivingCar.drive(500, 950, 850, -8, 0);
                selfDrivingCar.turn(1, 120, 40, 850, 750);
                selfDrivingCar.street(700, 120, 850, 800);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 40, 800, 600);
                selfDrivingCar.streetStall(10, 90, 500, 500, 400);

    else:
        # n? nGreen

        if (parkingPresence == "Parking"):
            # nParking nGreen
            
            if (recordListInput == ["", "", "", ""]):
                recordListValue.append("Normal");
                print("fNormal", end = " ");

            # selfDrivingCar.street(-70, 0, 600, 550);
            driveMotor.hold();
            visionMotor.run_target(1000, 0, Stop.HOLD, False)
            selfDrivingCar.turn(1, 93, 30, 750, 650);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, 92, 650, 550);
            driveMotor.hold();

            visionMotor.run_target(1000, 15, Stop.HOLD, False)
            selfDrivingCar.street(500, 92, 750, 650);

            if (recordListInput == ["", "", "", ""]):
                trafficSign = trafficSignColor();
                # trafficSign = "None";
                recordListValue.append(trafficSign);
                print("f" + trafficSign, end = " ");
            else:
                trafficSign = recordListInput[3];

            if (trafficSign == "Red"):
                # nParking nGreen fNormal fRed
                print("");
                
                visionMotor.run_target(1000, 0, Stop.HOLD, False)
                # selfDrivingCar.street(500, 180, 800, 600);
                # selfDrivingCar.streetStall(100, 180, 500, 300, 400);
                selfDrivingCar.turnDuration(490, 180, 30, 700, 550);
                selfDrivingCar.streetStall(100, 180, 350, 300, 400);

                selfDrivingCar.street(-300, 0, 750, 650);
                driveMotor.hold();
                selfDrivingCar.turn(1, -90, 30, 850, 750);
                selfDrivingCar.streetLine(200, -90, 900, 850);

                selfDrivingCar.turn(1, -130, 30, 850, 750);
                selfDrivingCar.street(300, -130, 850, 750);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.turn(1, -90, 30, 750, 550);
                selfDrivingCar.streetStall(100, -90, 550, 500, 500);

            elif (trafficSign == "Green"):
                # nParking nGreen fNormal fGreen
                print("");

                visionMotor.run_target(1000, 0, Stop.HOLD, False);
                selfDrivingCar.street(370, 90, 900, 850);
                selfDrivingCar.turn(1, 60, 30, 750, 650);
                selfDrivingCar.street(70, 60, 750, 750);
                selfDrivingCar.turn(1, 90, 30, 750, 650);
                selfDrivingCar.street(300, 90, 850, 750);
                selfDrivingCar.turn(1, 120, 30, 850, 750);

                selfDrivingCar.street(300, 120, 850, 750);
                visionMotor.run_target(1000, 100, Stop.HOLD, False);
                selfDrivingCar.turn(1, 90, 30, 850, 650);
                selfDrivingCar.streetStall(200, 90, 650, 500, 400);

            else:
                # nParking nGreen fNormal fNone false f

                selfDrivingCar.street(300, 92, 900, 850);

                trafficSign = trafficSignColor();
                recordListValue[3] = trafficSign;
                print("false f" + trafficSign);

                if (trafficSign == "Red"):
                    # nParking nGreen fNormal false fRed

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(200, 92, 900, 850);
                    # selfDrivingCar.street(500, 180, 800, 600);
                    # selfDrivingCar.streetStall(100, 180, 500, 300, 500);
                    selfDrivingCar.turnDuration(490, 180, 30, 700, 550);
                    selfDrivingCar.streetStall(100, 180, 350, 300, 400);

                    selfDrivingCar.street(-310, 0, 750, 650);
                    driveMotor.hold();
                    selfDrivingCar.turn(1, -130, 30, 850, 750);
                    selfDrivingCar.street(310, -120, 850, 750);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 550);
                    selfDrivingCar.streetStall(200, -90, 700, 550, 500);

                else:
                    # nParking nGreen fNormal false fGreen

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.street(70, 90, 760, 750);
                    selfDrivingCar.turn(1, 60, 30, 750, 650);
                    selfDrivingCar.street(70, 60, 750, 750);
                    selfDrivingCar.turn(1, 90, 30, 750, 650);
                    selfDrivingCar.street(300, 90, 850, 750);
                    selfDrivingCar.turn(1, 120, 30, 850, 750);

                    selfDrivingCar.street(300, 120, 850, 750);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 850, 650);
                    selfDrivingCar.streetStall(200, 90, 650, 500, 400);

        else:
            # nNormal nGreen

            driveMotor.hold();
            selfDrivingCar.street(130, 0, 850, 800);
            visionMotor.run_target(1000, 3, Stop.HOLD, False);
            selfDrivingCar.turn(1, 91, 30, 800, 600);
            driveMotor.hold();
            selfDrivingCar.streetLine(-100, hub.imu.heading(), 700, 550);
            driveMotor.hold();
            selfDrivingCar.drive(700, 850, 750, -8, 4);

            if (recordListInput == ["", "", "", ""]):
                driveMotor.hold();
                visionMotor.run_target(1000, (90 - hub.imu.heading()), Stop.HOLD, True);

                distanceLowest = 2000;
                timer.reset();

                while (timer.time() < 200):
                    if (distanceSensor.distance() < distanceLowest):
                        distanceLowest = distanceSensor.distance();

                if (recordListInput == ["", "", "", ""]):
                    if (distanceLowest < 1400):
                        parkingPresence = "Parking";
                    else:
                        parkingPresence = "Normal"

                    recordListValue.append(parkingPresence);
                    print("f" + parkingPresence, end = " ");
                else:
                    parkingPresence = recordListInput[2];

            else:
                pass;

            if (parkingPresence == "Parking"):
                # nNormal nGreen fParking

                selfDrivingCar.turn(1, 180, 30, 850, 750);
                driveMotor.hold();
                selfDrivingCar.streetStall(-350, 180, 900, 850, 800);

                visionMotor.run_target(1000, -100, Stop.HOLD, False);
                selfDrivingCar.street(250, 0, 800, 600);

                trafficSign = selfDrivingCar.streetDetect(150, 0, 600); # dapat ay total of 500

                if (recordListInput == ["", "", "", ""]):
                    if (trafficSign == "None"):
                        print("false", end = " ");
                        trafficSign = trafficSignColor();
                    
                    recordListValue.append(trafficSign);
                    print("f" + trafficSign);
                else:
                    trafficSign = recordListInput[3];

                if (trafficSign == "Red"):
                    # nNormal nGreen fParking fRed

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 650);
                    selfDrivingCar.streetLine(300, -90, 900, 850);

                    selfDrivingCar.turn(1, -130, 30, 850, 750);
                    selfDrivingCar.street(360, -120, 850, 750);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 550);
                    selfDrivingCar.streetStall(100, -90, 550, 500, 500);

                else:
                    # nNormal nGreen fParking fGreen

                    driveMotor.hold();
                    selfDrivingCar.streetStall(-300, 0, 800, 750, 500);
                    
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 650, 550);
                    selfDrivingCar.street(700, -90, 900, 850);
                    selfDrivingCar.turn(1, -55, 30, 850, 750);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 850, 750);
                    selfDrivingCar.streetStall(100, -90, 750, 600, 500);

            else:
                # nNormal nGreen fNormal

                if (recordListInput == ["", "", "", ""]):
                    visionMotor.run_target(1000, 30, Stop.HOLD, True);
                    trafficSign = selfDrivingCar.cameraScan(70, 100);
                    recordListValue.append(trafficSign);
                    print("f" + trafficSign);
                else:
                    trafficSign = recordListInput[3];
                
                if (trafficSign == "Red"):
                    # nNormal nGreen fNormal fRed

                    visionMotor.run_target(1000, -100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 180, 30, 750, 650);
                    driveMotor.hold();
                    selfDrivingCar.streetStall(-350, 180, 900, 850, 500);

                    selfDrivingCar.street(430, 0, 900, 850);
                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 850, 650);
                    selfDrivingCar.streetLine(300, -90, 900, 850);

                    selfDrivingCar.turn(1, -130, 30, 850, 750);
                    selfDrivingCar.street(390, -120, 850, 750);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, -90, 30, 750, 550);
                    selfDrivingCar.streetStall(100, -90, 550, 500, 500);

                else:
                    # nNormal nGreen fNormal fGreen

                    visionMotor.run_target(1000, 0, Stop.HOLD, False);
                    selfDrivingCar.drive(1000, 950, 850, -3, -1);
                    selfDrivingCar.turn(1, 120, 30, 850, 750);
                    selfDrivingCar.street(700, 120, 800, 700);
                    visionMotor.run_target(1000, 100, Stop.HOLD, False);
                    selfDrivingCar.turn(1, 90, 30, 850, 650);
                    selfDrivingCar.streetStall(10, 90, 650, 500, 400);

    selfDrivingCar.motorClose();

    if (recordListValue == []):
        return recordListInput;
    else:    
        return recordListValue;

# try:
#     recordListValue = ["", "", "", ""];
#     for i in range (2):
#         print("\n");
#         hub.imu.reset_heading(0);
#         recordListValue = obstacleLoopClockwise(recordListValue);
# except:
#     pass;
# finally:
#     print(recordListValue);
#     print(timer.time());
