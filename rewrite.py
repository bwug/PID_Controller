from machine import pin
from time import *
# Import the ADC class from the machine module
# This is for MicroPython

def ADC(): pass
def PIN(): pass

class PIDController:
    def __init__(self):
        # Variables
        self.integrator = 0
        self.previous_error = 0

        self.differentiator = 0
        self.previous_measure = 0

        self.output = 0

        # Constants
        self.Kp = None
        self.Ki = None
        self.Kd = None
        self.tau = None
        self.limMin = None
        self.limMax = None
        self.T = None

    def update(self, setpoint, measurement):
        error = setpoint - measurement

        proportional = self.Kp * error

        self.integrator = self.integrator + 0.5 * self.Ki * self.T * (error + self.previous_error)

        limMinInt, limMaxInt = None, None

        if self.limMax > proportional:
            limMaxInt = self.limMax - proportional
        else:
            limMaxInt = 0
        if self.limMin < proportional:
            limMinInt = self.limMin - proportional
        else:
            limMinInt = 0

        if self.integrator > limMaxInt:
            self.integrator = limMaxInt
        elif self.integrator < limMinInt:
            self.integrator = limMinInt

        self.differentiator = (2 * self.Kd * (measurement - self.previous_measure) +
                               (2 * self.tau - self.T) / (2 * self.tau + self.T))

        self.output = proportional + self.integrator + self.differentiator

        if self.output > self.limMax:
            self.output = self.limMax
        elif self.output > self.limMin:
            self.output = self.limMin

        self.previous_error = error
        self.previous_measure = measurement


# Create instance of a PID controller:
pid = PIDController()

# Set the PID controller parameters:
pid.Kp = 1
pid.Ki = 1
pid.Kd = 1

pid.limMax = 100
pid.limMin = 1
pid.T = 1
pid.tau = 1


# Creates an ADC input pin at GPIO 23
# Will throw errors when not using micropython
# Ignore them, the code will not run anyway
pid_pin = ADC(PIN("GP23")) # Remove quotation marks before compiing and uploading

# Assuming setpoint is like a fixed midpoint or a point of reference
setpoint = 1

# Main loop

def update():
    # Read 12 bit analog input from the pi pico analog pins
    measurement = pid_pin.read_u16()
    # Assuming pid_pin's measurement is the measurement?
    pid.update(setpoint, measurement)

    sleep(0.1) # Update on a 0.1s cycle
