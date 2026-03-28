import numpy as np
import matplotlib.pyplot as plt

# Physics functions
def calculate_position(x0, u, a, t):
    return x0 + u*t + 0.5*a*t**2

def calculate_velocity(u, a, t):
    return u + a*t

def calculate_kinetic_energy(m, v):
    return 0.5 * m * v**2


def run_simulation():
    print("=== 1D Motion Simulator with Energy Analysis ===")

    # Inputs
    x0 = float(input("Enter initial position (m): "))
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    m = float(input("Enter mass (kg): "))
    total_time = float(input("Enter total time (s): "))
    dt = float(input("Enter time step (e.g. 0.1): "))

    # Time values
    t_values = np.arange(0, total_time, dt)

    positions = []
    velocities = []
    energies = []

    # Compute values
    for t in t_values:
        x = calculate_position(x0, u, a, t)
        v = calculate_velocity(u, a, t)
        ke = calculate_kinetic_energy(m, v)

        positions.append(x)
        velocities.append(v)
        energies.append(ke)

    # ---- Combined Plots ----
    plt.figure(figsize=(10, 8))

    # Position vs Time
    plt.subplot(3, 1, 1)
    plt.plot(t_values, positions)
    plt.ylabel("Position (m)")
    plt.title("1D Motion Analysis")
    plt.grid()

    # Velocity vs Time
    plt.subplot(3, 1, 2)
    plt.plot(t_values, velocities)
    plt.ylabel("Velocity (m/s)")
    plt.grid()

    # Kinetic Energy vs Time
    plt.subplot(3, 1, 3)
    plt.plot(t_values, energies)
    plt.xlabel("Time (s)")
    plt.ylabel("Kinetic Energy (J)")
    plt.grid()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_simulation()