
***

BSU Spartan Team
====

This repository provides information pertaining to the robot of the BSU Spartan Team, a self-driving car designed and programmed by delegates from the Philippines, made for the World Robot Olympiad™ 2024 – Future Engineers Category (Self-Driving Cars) with the theme "Earth Allies". 

<img src = "https://github.com/NovusSpartans/NOVUS-SPARTIAT_BatStateUTNEU_Future-Engineers-2024/blob/main/Vehicle%20Photos/Main%20View%20(Novus%20Spartiat).jpg">

***

## The Team:


- Joseph Bernard Maala (Programmer)
- John Angelo Bautista (Builder)

***

## Content

* `Bills of Materials` contains the list of all the items necessary to build the robot.
* `Pictorial Diagram` contains 2 pictorial wiring diagrams of the whole robot including all of its components.
* `Source Code` contains 3 files of program for Obstacle Management.
* `Team Photos` contains multiple photos of the whole team.
* `Vehicle Chassis` contains 6 photos of the chassis of the vehicle from every sides.
* `Vehicle Photos` contains 6 photos of the vehicle from every sides and 1 main photo of the vehicle.
* `Video Performance` contains 2 video links showcasing each challenge round.
<br/><br/> 
* [1. Mobility Management](#1-mobility-management)
* [2. Sense Management](#2-sense-management)
* [3. Power Management](#3-power-management)
* [4. Obstacle Management](#4-obstacle-management)
* [5. Recommendations](#5-recommendations)

***

## Robot Specifications
Below are the specifications of the BSU Spartan Team's robot:
- **Dimensions**: 290mm (L) x 175mm (W) x 215mm (H)
- **Weight**: ?
- **Speed**: ?
- **Turning Radius**: >100mm
- **Working Voltage**: 7.6V–8.3V
- **Maximum Steer**: ?
- **Steering Torque**: ?
- **Drive System**: Rear-wheel drive (RWD)
- **Material**: LEGO® Technic 

***

## 1. Mobility Management

### 1.1 Motor Selection
Motor selection is a crucial part of building the robot since its maneuverability highly depends on it. LEGO® Education SPIKE™ Prime Set has two (2) available motors: SPIKE™ Medium Angular Motor and SPIKE™ Large Angular Motor, which will be referenced as SPIKE™ Medium Motor and SPIKE™ Large Motor respectively. These motors have a lot in common performance-wise and only differ in speed and torque. Based on tests performed with a provision of 7.2V power supply, here are the results: 
<br/>

    SPIKE™ Medium Motor            SPIKE™ Large Motor
     Speed: 135 RPM to 185 RPM       Speed: 135 RPM to 175 RPM
     Torque: 3.5 Ncm to 18 Ncm       Torque: 8 Ncm to 25 Ncm

    RPM – rotations per minute, Ncm – newton centimeter

The SPIKE™ Medium Motor was shown to be negligibly faster than the SPIKE™ Large Motor. However, the SPIKE™ Large Motor was able to provide a substantial amount of power compared to its counterpart. With these pieces of  information, the team had chosen to use SPIKE™ Large Motors for both driving and steering management, using two (2) SPIKE™ Large Motors in total for the mobility of the robot. 

### 1.2 Robot Driving Mechanism

The robot uses a parallel steering geometry; a front SPIKE™ Large Motor steers the front wheels of the robot parallel to each other. Meanwhile, the robot is propelled by a rear-wheel drive (RWD) transmission , where power from the rear SPIKE™ Large Motor drives the rear wheels, propelling the robot forward or backward. This steering geometry and transmission setup was chosen by the team because it is commonly used in the Future Engineers Category. Additionally, the team experimented and concluded that the RWD system offer better handling of the robot compared to the front-wheel drive (FWD).

### 1.3. Robot Design

The electrical components of the robot are mounted on a robot chassis made from LEGO® Technic. These materials were mostly from LEGO® Education SPIKE™ Prime Set and LEGO® Education SPIKE™ Prime Expansion Set, though a few were from LEGO® MINDSTORMS® Education EV3 Core Set and LEGO® MINDSTORMS® Education EV3 Expansion Set.

For the wheels of the robot, SPIKE™ Large Wheels are incorporated for the rear driving mechanism while EV3 Small Wheels are used for the steering mechanism of the robot. These wheels have a diameter of 88 mm and 43.2 mm respectively. The team decided to use large wheels for the robot's driving base since larger wheels have a higher circumference value compared to the small ones, thus covering longer distances per rotation and increasing the maximum speed limit of the robot. 

As for the weight distribution of the robot, the weight is focused on the rear side of the robot since this is where the driven wheels of the robot are. This is done through the placement of the robot's microcontrollers on the rear side of the robot. This weight distribution should enhance the traction of the said wheels, preventing them from slipping. 

***

## 2. Sense Management

Self-driving cars are highly dependent on their sensors in order to drive autonomously. That is why the robot consists of different sensors to properly execute its movements with regards to its position on the game field and obstacles surrounding it. Here are the components of the robot related to its sense management:

<img src = "https://github.com/user-attachments/assets/ea2a1038-9dbe-48ee-8ba0-cbdc14bb69af">

### 2.1.   SPIKE™ Color Sensor 
The SPIKE™ Color Sensor has the capacity to measure color RGB/HSV, reflection intensity, and ambient intensity. It has a sample rate of 100 Hz and an optimal reading distance of 16 mm. It has three (3) LEDs that can be turned on and off individually at different power levels, making it a possible light output. The team selected this color sensor due to its excellent performance in color detection, far better than the other color sensors the team have.

This color sensor is positioned on the front of the robot where it is facing downwards the game field. It is primarily used to read the colored lines on the game field, thus determining the driving direction of the robot. If it has detected the orange line first, the robot would know that the driving direction is clockwise, else if the first detected line was blue, the driving direction is counterclockwise. Additionally, the robot is able to know its position on some parts of the field that have a clear line to be read by the color sensor.

### 2.2.   SPIKE™ Distance Sensor
The SPIKE™ Distance Sensor has the ability to measure the distance to a surface in front of it with the use of ultrasonic technology. It has a sample rate of 100 Hz and a distance sensing range of 5 cm to 200 cm +/- 2 cm. It has an entrance angle of +/- 35° and has four (4) LEDs that can be turned on and off individually at different power levels, making it a possible light output. It sends inaudible high frequency sound waves from one “eye” while the other “eye” will measure how long it takes the sound waves to reflect through it.

This distance sensor is placed on the front of the robot, which is used to determine the position of the robot in respect to the wall in front of the sensor. This allows the robot to navigate safely within the game field, continuously checking if the robot is near the outer boundary wall in Open Challenge Rounds since the robot may not touch the said wall. In addition to that, it is also used to identify the position of the randomly placed parking boundaries and check if there is an obstacle in front of the robot in Obstacle Challenge Rounds.

### 2.3.   SPIKE™ Gyro Sensor
The built-in SPIKE™ Gyro Sensor can keep track of the angle the hub is currently facing. It consists of a three-axis accelerometer and three-axis gyroscope. The gyroscope part records the change of rotation of the hub and measures the total angle of rotation in degrees, enabling it to return the hub’s exact rotation angle around a given axis. Combined with the accelerometer, it allows the hub to determine its orientation and acceleration along a given axis. 

The robot relies on this gyro sensor for most of its movements, facilitating its accurate navigation across the whole game field. It enables the robot to follow a specific angle when moving, thus making it drive straight and turn into a particular angle efficiently. 

### 2.5.   Additional Information
Both the SPIKE™ Distance Sensor and AISTEAM Roof Vision Module are mounted to a SPIKE™ Large Motor. This enables these two sensors to rotate from a range of angle of 0° to 180°, covering a wide part of the surrounding area of the robot. The team has done this since the limited ports of the SPIKE™ Large Hub cannot provide more room for sensors around the robot. This motor serves as a helpful tool in the detection of the walls, obstacles, and overall surroundings of the robot while it is in the game field.

Another SPIKE™ Color Sensor is placed inside the shell of the robot. It is used to transfer and evaluate all of the essential data from the camera to the primary controller of the robot. It is mostly used in Obstacle Challenge Rounds, to detect the obstacles and the parking lot boundaries within the field.

***

## 3. Power Management

In the field of robotics, power management serves as the cornerstone that ensures the operation of an autonomous system. It serves as the brain and heart of the robot. Not only does it play a role in supplying data and energy to the various components, but it also plays a role in optimizing the overall performance of the robot.

The setup for our self-driving robot centers around two key components: the SPIKE™ Large Hub and the AISTEAM Controller, along with its accompanying battery. Below are the figures and details about the components in the power management section:

<img src = "https://github.com/user-attachments/assets/a76e94a5-78ec-4ae1-a66c-fcbb91f20ae8">

### 3.1.   SPIKE™ Large Hub
The SPIKE™ Large Hub serves as the primary controller of the robot, controlling most of the components of the robot including its motors and sensors. It is where the robot’s main program is downloaded; integrated with MicroPython as the operating system. The hub features six LPF2 input/output ports and a built-in six-axis gyro sensor, which includes a three-axis accelerometer and three-axis gyroscope. Additionally, it has a built-in speaker with a maximum sound quality of 12-bit 16 KHz and can connect to devices via Bluetooth or USB Cable. The team selected this hub as the primary controller for the robot due to its comprehensive capabilities, having six (6) ports for SPIKE™ excellent motors and sensors.

### 3.2.   SPIKE™ Large Hub Rechargeable Battery
The SPIKE™ Large Hub Rechargeable Battery is a lithium-ion polymer battery designed to power the Technic Large Hub, which in turn powers all Spike motors and sensors. It can be charged inside the Hub using a micro-USB cable and can be removed easily. With a capacity of 2100 mAh and an output of 7.3V, this battery has a lifetime of over 500 cycles, meaning it can handle more than 500 charge-discharge cycles throughout its lifespan.

***

## 4. Obstacle Management

In order to detect the position and negotiate with the color of the obstacles, a specific strategy must be well-planned to possibly finish three (3) laps in Obstacle Challenge Rounds. The team had spent a fair amount of time considering different thoughts and ideas to efficiently manage the obstacles on the game field; always giving space for new yet excellent ideas to be added in the team’s strategy.

The main strategy for the robot involves two (2) major ideas: first is giving the camera and the distance sensor the ability to rotate with the use of a SPIKE™ Large Motor, which wil be referenced as “vision motor” in this documentary. The vision motor can rotate both the camera and distance sensor for approximately 90° in both directions starting from the middle. The rotation of the vision motor depends on the position of the robot and the color of the detected obstacles.

The second major idea is programming the robot to follow three (3) possible routes based on the color of the obstacles, the position of the parking lot boundaries, and the defined driving direction of the round. Example: the driving direction is set to be clockwise; refer to the illustration below. If the detected obstacle is GREEN, the robot would follow the green arrow, near the outer wall. If the obstacle is RED, the robot would follow the red arrow, near the inner wall. However, if the robot detected a GREEN obstacle, and the parking lot boundaries were located on that same section, the robot would follow the gray arrow, somewhere between the outer and inner walls. If there are no detected obstacles, the robot would either follow the route for a GREEN or RED obstacle.

<img src = "https://github.com/user-attachments/assets/500eb94e-bbe9-4991-bf80-80a7fc3ddd98">

***

## 5. Recommendations

The robot has come a long way since its development, yet there are still areas where it can be refined and optimized. The team first assessed the limitations of the robot to identify possible recommendations that should address these current limitations and anticipate future challenges. These recommendations aim to enhance the overall performance, reliability, and functionality of the robot.

### 5.1.  Mobility Management

- Incorporate a differential gear into the robot's driving mechanism for smooth and stable turns by letting the wheels rotate at different speeds. This is important since for instance, during a right turn, the left wheel, being farther from the center of the turn, must cover a larger distance along the circular path than the right wheel within the same duration. 
- Try other types of steering geometry, particularly the Ackerman steering mechanism which allows a car to turn while avoiding tire slip. Though it is not that easy to implement, it should allow smoother and sharper turns if incorporated correctly, allowing the robot for a wider range of movements.
- Test the capability of all-wheel drive (AWD) transmission which may improve the speed, acceleration, and stability of the robot. This is due to the fact that it distributes power across all four wheels, reducing the chance of wheels losing traction at high acceleration. However, it should be taken into consideration that AWD systems typically consumes more weight than RWD, which can reduce the maximum speed of the robot. 
- Select or develop custom wheels with appropriate dimensions and proper tires for better traction on the game field. This would lessen tire slip, improving the precision of the motor encoders thus enhancing the consistency of the robot.
