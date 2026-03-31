 Physics Motion Simulator (1D → 2D → Non-Ideal Systems)
Overview

This project is a progressively developed physics simulation built to model motion using principles of classical mechanics and computational methods.

It began as a simple 1D kinematics model and has evolved into a 2D projectile motion simulator that incorporates energy analysis and non-ideal effects such as air resistance.

The focus of this project is not just visualization, but the translation of physical theory into computational models, along with validation using fundamental laws such as energy conservation.

Project Evolution
Phase 1: 1D Motion (Kinematics)

Initial implementation modeled motion along a single axis using analytical equations.

Features:

Position vs Time
Velocity vs Time
Acceleration vs Time
Analytical kinematic equations

Key Insight:

Established the relationship between motion variables as time-dependent functions
Phase 2: Energy Analysis (1D)

The simulator was extended to include energy-based modeling.

Features:

Kinetic Energy: KE = 1/2 mv²
Potential Energy: PE = mgh
Total Mechanical Energy: E = KE + PE
Energy conservation validation

Key Insight:

Verified conservation of mechanical energy in an ideal system
Introduced numerical validation through energy drift measurement
Phase 3: 2D Projectile Motion

The system was extended from 1D to 2D motion.

Features:

Projectile trajectory (x vs y)
Velocity components (vx, vy)
Position vs time in both axes
Time of flight calculation

Key Insight:

Separation of motion into independent horizontal and vertical components
Constant horizontal velocity vs accelerated vertical motion
Phase 4: Energy Analysis in 2D

Energy modeling was extended to multi-dimensional motion.

Features:

Total kinetic energy using both velocity components
Gravitational potential energy based on vertical position
Total energy visualization

Key Insight:

Demonstrated conservation of energy in 2D systems
Validated simulation accuracy through near-constant total energy
Phase 5: Projectile Motion with Air Resistance (Non-Ideal System)

The simulator was extended to include air resistance, transitioning from idealized physics to realistic modeling.

Features:

Quadratic drag force proportional to velocity squared
Drag direction opposing motion
Numerical integration using Euler method
Simulation of non-conservative systems

Mathematical Model:

Drag force: F_d = (1/2) C_d ρ A v²
Acceleration:
a_x = -k v v_x
a_y = -g - k v v_y
where k = (1/2)(C_d ρ A)/m

Key Insight:

Total mechanical energy is no longer conserved
Energy decreases over time due to dissipation
Analytical solutions are insufficient → numerical methods required
Technical Approach

Language:

Python

Libraries:

NumPy (numerical computation)
Matplotlib (visualization)

Design Principles:

Vectorized computations (efficient and scalable)
Clear separation between physics logic and visualization
Incremental system development
Validation through physical laws
Current Capabilities
Simulates 1D and 2D motion
Models ideal projectile motion
Implements air resistance (quadratic drag)
Uses numerical integration (Euler method)
Tracks full motion state (position, velocity)
Computes kinetic, potential, and total energy
Demonstrates both energy conservation and energy dissipation
Results & Validation
In ideal simulations, total energy remains nearly constant
In drag simulations, total energy decreases over time as expected
Trajectories change significantly under air resistance, reflecting real-world behavior

This confirms both:

Correct implementation of physical laws
Proper transition from ideal to non-ideal modeling
Limitations
Euler method has limited accuracy compared to higher-order methods
Assumes constant drag coefficient
No wind or environmental variability
Fixed time step (no adaptive stepping)
Future Improvements
Implement Runge-Kutta (RK4) for higher accuracy
Compare numerical methods (Euler vs RK4)
Add real-time animation
Introduce user-defined parameters
Model wind and variable atmospheric conditions
Extend simulation to 3D motion
Why This Project Matters

This project demonstrates:

Ability to translate physics theory into computational systems
Understanding of both ideal and non-ideal physical models
Use of numerical methods when analytical solutions fail
Structured, incremental development of complex systems

It reflects a shift from solving equations to building simulations that test and validate those equations.

Author

Developed as part of a self-driven exploration into computational physics, scientific programming, and mathematical modeling.