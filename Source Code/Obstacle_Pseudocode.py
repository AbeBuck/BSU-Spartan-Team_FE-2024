motorsInitialize();
sensorsInitialize();

sensors.hardCalibrate();

obstacle = camera.read();

if (obstacle == "Green"):
    robot.goLeft();
elif (obstacle == "Red"):
    robot.goRight();
else:
    robot.goStraight();

drivingDirection = colorSensor.read();
drivingLaps = 0;

if (drivingDirection == "Clockwise"):
    robot.turnRight();
else:
    robot.turnLeft();

while (drivingLaps < 3):
    drivingLaps += 0.25;
    obstacle = camera.read();

    if (obstacle == "Green"):
        robot.goLeft();
    elif (obstacle == "Red"):
        robot.goRight();
    else:
        robot.goStraight();

    parking = camera.read();

    if (parking == "True"):
        robot.avoidParking();

findParking();
robot.stop();