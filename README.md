 1D Motion Simulator (Kinematics)
This project models motion in one dimension using fundamental kinematic equations. It began as a simple displacement calculator and has been expanded to simulate motion under constant acceleration.

Physics Background

The simulator is based on standard kinematics:

Velocity: v = u + at
Position: x = x₀ + ut + ½at²

These equations describe how velocity and position change over time under constant acceleration.

Features
Computes position and velocity over time
Supports constant acceleration (including gravity)
Time-step simulation for observing motion dynamically
Handles different motion scenarios:
Constant velocity (a = 0)
Accelerated motion (a > 0)
Decelerated motion / gravity (a < 0)
Example Use Case

Simulating vertical motion under gravity:

Initial velocity = 10 m/s
Acceleration = -9.8 m/s²

The simulator demonstrates how velocity decreases linearly over time while position follows a curved trajectory.

How to Run
Run the Python file
Input:
Initial position
Initial velocity
Acceleration
Total time
Time step
Observe computed position and velocity values
Project Evolution
Started as a displacement calculator
Extended to include velocity and acceleration
Developed into a time-based motion simulator
Future Improvements
Graphical visualization (position-time and velocity-time graphs)
2D projectile motion
Air resistance modeling
Purpose

This project is part of my effort to combine physics and programming by building simulations that reflect real-world motion and deepen my understanding of mechanics.