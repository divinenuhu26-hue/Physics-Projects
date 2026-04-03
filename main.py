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

def derivatives(vx, vy):
    v = np.sqrt(vx**2 + vy**2)
    ax = -k * v * vx
    ay = -g - k * v * vy
    return ax, ay

# SIMULATION LOOP (RK4 Method)
while True:
    # Save current state
    t_vals.append(t)
    x_vals.append(x)
    y_vals.append(y)
    vx_vals.append(vx)
    vy_vals.append(vy)

    # RK4 for velocity
    ax1, ay1 = derivatives(vx, vy)
    ax2, ay2 = derivatives(vx + 0.5*dt*ax1, vy + 0.5*dt*ay1)
    ax3, ay3 = derivatives(vx + 0.5*dt*ax2, vy + 0.5*dt*ay2)
    ax4, ay4 = derivatives(vx + dt*ax3, vy + dt*ay3)

    vx_new = vx + (dt/6) * (ax1 + 2*ax2 + 2*ax3 + ax4)
    vy_new = vy + (dt/6) * (ay1 + 2*ay2 + 2*ay3 + ay4)

    x_new = x + vx_new * dt
    y_new = y + vy_new * dt
    t_new = t + dt

    # Check if projectile crosses ground
    if y_new < 0:
        # Linear interpolation to find exact landing point
        frac = y / (y - y_new)   # fraction between last y and new y
        x_land = x + frac * (x_new - x)
        t_land = t + frac * (t_new - t)

        # Append landing point at y=0
        t_vals.append(t_land)
        x_vals.append(x_land)
        y_vals.append(0.0)
        vx_vals.append(vx_new)
        vy_vals.append(vy_new)
        break

    # Update state
    vx, vy, x, y, t = vx_new, vy_new, x_new, y_new, t_new

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
plt.title("Trajectory with Air Resistance (RK4 + Interpolation)")
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
