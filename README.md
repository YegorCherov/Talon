# Talon

Talon is a single motor ducted drone that uses thrust vectoring for flight control.

### How It Works

A single brushless motor and three blade propeller sit at the top of the duct. 

Because a single prop creates rotational torque, eight curved stator vanes sit inside the duct to straighten the airflow and cancel out motor torque passively. 

Directly below the stators, four control vanes are connected to micro servos positioned at ninety degree intervals. Deflecting opposing pairs controls pitch and roll. Deflecting all four vanes together controls yaw and trims out any remaining motor torque.

The lower cylinder holds the battery to keep the heaviest component low and centered directly under the thrust axis.

### Measured Data and Specs

* Total flying weight: 550 grams
* Battery weight: 217 grams (4S pack)
* Airframe and electronics: 330 grams
* Expected thrust: 850 grams to 1190 grams
* Thrust to weight ratio: 1.55 to 2.17

### Mechanical and Control Notes

Control authority depends directly on prop wash speed. When throttle is low, the vanes have less air passing over them and react slower. 

The curved stator vanes handle the bulk of the motor torque during hover, leaving the four servo vanes to focus on attitude control and fine yaw adjustments. 

Linkages between the servos and control vanes need to be stiff to avoid flutter at full throttle.
