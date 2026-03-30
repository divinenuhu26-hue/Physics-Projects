import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
v0 = 20          # initial velocity (m/s)
theta_deg = 45   # launch angle (degrees)
g = 9.81         # gravity (m/s^2)
m = 1.0          # mass (kg)

theta = np.radians(theta_deg)

# INITIAL VELOCITY COMPONENTS
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# TIME OF FLIGHT
t_flight = (2 * v0y) / g
t = np.linspace(0, t_flight, 500)

# MOTION EQUATIONS
x = v0x * t
y = v0y * t - 0.5 * g * t**2

vx = np.full_like(t, v0x)
vy = v0y - g * t
 
# ENERGY CALCULATIONS
KE = 0.5 * m * (vx**2 + vy**2)
PE = m * g * y
E_total = KE + PE

# PLOTTING
plt.figure(figsize=(10, 8))

# Trajectory (x vs y)
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Projectile Trajectory")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid()

# Velocity vs Time
plt.subplot(2, 2, 2)
plt.plot(t, vx, label="vx")
plt.plot(t, vy, label="vy")
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid()

# Position vs Time
plt.subplot(2, 2, 3)
plt.plot(t, x, label="x")
plt.plot(t, y, label="y")
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.grid()

# Energy vs Time
plt.subplot(2, 2, 4)
plt.plot(t, KE, label="Kinetic Energy")
plt.plot(t, PE, label="Potential Energy")
plt.plot(t, E_total, label="Total Energy")
plt.title("Energy vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# ENERGY VALIDATION
energy_drift = np.max(E_total) - np.min(E_total)
print("Max Energy Drift:", energy_drift)