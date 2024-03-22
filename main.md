# PID Controller Implementation in Software

- Overview
- Converting from continous to discrete time
- Practical considerations
- PID code in C
- Example applications

## Overview
- Want to make system output track desired setpoint via feedback
- PID controller takes two inputs and produces a **control signal**
- System usually in continuous time, PID controller usually implemented digitally.

## PID in continous domain
$$G(s) = {{u(s)} \over e(s)} = K_P + K_I \cdot {1 \over s} + K_D \cdot  {{s} \over s\tau+1}$$

## Convert to discrete time domain

- s-Domain to z-Domain can be obtained using the Tustin transform -> best frequency domain match

Tustin:
1. Substitute s with $2{{2}\over T} {{z-1} \over z+1}$

2. Recall: $Y(z) = X(z) \cdot Z^{-1} \therefore y[n] = x[n-1]$

T = sampling time of disrete controller in seconds

$$p[n] = K_p \cdot e[n]$$ 
$$i[n] = {{K_IT}\over 2}(e[n] + e[n-1]) + i[n-1]$$
$$d[n] = {{2K_D} \over 2\tau + T}(e[n]-e[n-1]) + {{2\tau - T} \over t\tau + T} d[u-1]$$

## Practical considerations
- Derivative amplifies high frequency noise
- Derivative "kick" during setpoint change
- Integrator can saturate output
- Limits on system input alternative
- Choosing a sample time T

## Code structure
- Header-file "library"
- PID controller struct
- Initialisation function
- Update function
