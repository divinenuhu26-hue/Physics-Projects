import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
v0 = 20
theta_deg = 45
g = 9.81
m = 1.0

# Drag parameters
Cd = 0.47        # drag coefficient (sphere)
rho = 1.225      # air density (kg/m^3)
A = 0.01         # cross-sectional area (m^2)

k = 0.5 * Cd * rho * A / m

theta = np.radians(theta_deg)

# INITIAL CONDITIONS
vx = v0 * np.cos(theta)
vy = v0 * np.sin(theta)

x, y = 0, 0

dt = 0.01
t = 0

# Storage lists
t_vals = []
x_vals = []
y_vals = []
vx_vals = []
vy_vals = []

# SIMULATION LOOP (Euler Method)
while y >= 0:
    v = np.sqrt(vx**2 + vy**2)

    ax = -k * v * vx
    ay = -g - k * v * vy

    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    t += dt

    t_vals.append(t)
    x_vals.append(x)
    y_vals.append(y)
    vx_vals.append(vx)
    vy_vals.append(vy)

# Convert to arrays
t_vals = np.array(t_vals)
x_vals = np.array(x_vals)
y_vals = np.array(y_vals)
vx_vals = np.array(vx_vals)
vy_vals = np.array(vy_vals)

# ENERGY (NOTE: NOT CONSERVED)
KE = 0.5 * m * (vx_vals**2 + vy_vals**2)
PE = m * g * y_vals
E_total = KE + PE

# PLOTTING
plt.figure(figsize=(10, 8))

# Trajectory
plt.subplot(2, 2, 1)
plt.plot(x_vals, y_vals)
plt.title("Trajectory with Air Resistance")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid()

# Velocity
plt.subplot(2, 2, 2)
plt.plot(t_vals, vx_vals, label="vx")
plt.plot(t_vals, vy_vals, label="vy")
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid()

# Position
plt.subplot(2, 2, 3)
plt.plot(t_vals, x_vals, label="x")
plt.plot(t_vals, y_vals, label="y")
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.grid()

# Energy
plt.subplot(2, 2, 4)
plt.plot(t_vals, KE, label="KE")
plt.plot(t_vals, PE, label="PE")
plt.plot(t_vals, E_total, label="Total Energy")
plt.title("Energy vs Time (Non-Conservative)")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()