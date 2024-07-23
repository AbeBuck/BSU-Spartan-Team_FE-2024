NOVUS SPARTIAT
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2022.

## Content

* `Team Photos` contains 2 photos of the team (an official one and one funny photo with all team members)
* `Vehicle Photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `Video Performance` contains the video.md file with the link to a video where driving demonstration exists
* `schemes` contains one or several schematic diagrams in form of JPEG, PNG or PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition
* `models` is for the files for models used by 3D printers, laser cutting machines and CNC machines to produce the vehicle elements. If there is nothing to add to this location, the directory can be removed.
* `other` is for other files which can be used to understand how to prepare the vehicle for the competition. It may include documentation how to connect to a SBC/SBM and upload files there, datasets, hardware specifications, communication protocols descriptions etc. If there is nothing to add to this location, the directory can be removed.

## 1. Mobility Management

Motor selection is a crucial part of building the robot since its maneuverability highly depends on it. LEGO® Education SPIKE™ Prime Set has two (2) available motors: Medium Angluar Motor and Large Angular Motor, which can be referenced as Medium Motor and Large Motor respectively. These motors have a lot in common performance-wise and only differ in speed and torque. Based on tests performed with a provision of 7.2V power supply, here are the results: 

    Medium Motor                    Large Motor
     Speed: 135 RPM to 185 RPM       Speed: 135 RPM to 175 RPM
     Torque: 3.5 Ncm to 18 Ncm       Torque: 8 Ncm to 25 Ncm

    RPM – rotations per minute, Ncm – newton centimeter

The Medium Motor was shown to be negligibly faster than the Large Motor. However, the Large Motor was able to provide a substantial amount of power compared to its counterpart. With these pieces of  information, the team had chosen to use the Large Motor for both driving and steering management. The robot uses three (3) Large Motors, one each for driving and steering, while the other one will be discussed in the last part of Sense Management.

The robot is propelled by a rear-wheel drive transmission, where power from the rear motor drives the rear wheels, propelling the robot forward or backward. The large motors in the front are centralized on focusing for steering the entire robot, allowing for a range of motion from 90 degrees to -90 degrees. This transmission setup was chosen by the team because it is commonly used in the Future Engineers Category. Additionally, it is found that RWD (rear-wheel drive) systems offer better handling compared to the front-wheel drives, which were tested by the team.
