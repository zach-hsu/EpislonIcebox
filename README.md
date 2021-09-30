# EpislonIcebox
Simple two button interface that controls a motor that rotates the shelves of the fridge

The code is implemented on the raspberry pi using the 16 and 18 GPIO ports for the motors, as well as the 7 and 8 GPIO ports as inputs for the buttons, and the 1 GPIO pin as a power source.
Current would flow out of the first GPIO pin, through a resistor, and then through two buttons in parallel. These buttons would act as open switches until pressed, when they would allow energy to flow to the 7 and 8 GPIO pins. The FridgeScript.py would check for input on the 7 and 8 GPIO ports, and if it recieved a current on one and not the other it would turn on the 16 or 18 GPIO port to spin the motor.
This signal would then go to a L298 stepper motor driver, which would take the signal, as well as power from the raspberry pi, to rotate the motor.

This project contains FridgeScript.py, the code implemented in the physical system, as well as FridgeScript(LargeMotor).py, a theoretical code for a large stepper motor that could rotate heavier loads with a higher torque.
