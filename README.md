  # 1D Motion Simulator (Kinematics)

This project models motion in one dimension using fundamental kinematic equations. It began as a simple displacement calculator and has been progressively developed into a simulation tool that analyzes motion, velocity, and energy over time.

---

## Physics Background

The simulator is based on standard kinematics:

- Velocity: v = u + at  
- Position: x = x₀ + ut + ½at²  

These equations describe how velocity and position evolve over time under constant acceleration.

---

## Features

- Computes position and velocity over time
- Supports constant acceleration (including gravity)
- Time-step simulation for dynamic motion analysis

### Graphical Analysis
- Position vs Time graph
- Velocity vs Time graph

### Energy Analysis
- Computes kinetic energy using:  
  KE = ½mv²  
- Kinetic Energy vs Time graph

### Motion Scenarios
- Constant velocity (a = 0)
- Accelerated motion (a > 0)
- Decelerated motion / gravity (a < 0)

---

## Example Use Case

Simulating vertical motion under gravity:

- Initial velocity = 10 m/s  
- Acceleration = -9.8 m/s²  

The simulator demonstrates:
- Linear change in velocity over time
- Curved position-time graph
- Increasing or decreasing kinetic energy depending on motion

---

## How to Run

1. Run the Python file
2. Input:
   - Initial position
   - Initial velocity
   - Acceleration
   - Mass
   - Total time
   - Time step
3. Observe:
   - Numerical results
   - Graphical plots (position, velocity, and energy)

---

## Project Evolution

- Started as a displacement calculator  
- Extended to include velocity and acceleration  
- Developed into a time-based motion simulator  
- Added graphical visualization of motion  
- Integrated kinetic energy computation and analysis  

---

## Future Improvements

- Combine multiple graphs into a single figure
- Add potential energy and total energy analysis
- Extend to 2D motion (projectile motion)
- Include air resistance and drag forces

---

# Purpose

This project is part of my effort to combine physics and programming by building simulations that reflect real-world motion and deepen my understanding of mechanics.