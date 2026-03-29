import numpy as np
import matplotlib.pyplot as plt

# Physics functions
def calculate_position(x0, u, a, t):
    return x0 + u*t + 0.5*a*t**2

def calculate_velocity(u, a, t):
    return u + a*t

def calculate_kinetic_energy(m, v):
    return 0.5 * m * v**2

def calculate_potential_energy(m, g, h):
    return m * g * h


def run_simulation():
    print("=== 1D Motion Simulator with Full Energy Analysis ===")

    # Inputs
    x0 = float(input("Enter initial position (m): "))
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    m = float(input("Enter mass (kg): "))
    g = float(input("Enter gravitational acceleration (e.g. 9.8): "))
    total_time = float(input("Enter total time (s): "))
    dt = float(input("Enter time step (e.g. 0.1): "))

    # Time values
    t_values = np.arange(0, total_time, dt)

    positions = []
    velocities = []
    kinetic_energies = []
    potential_energies = []
    total_energies = []

    # Compute values
    for t in t_values:
        x = calculate_position(x0, u, a, t)
        v = calculate_velocity(u, a, t)

        ke = calculate_kinetic_energy(m, v)
        pe = calculate_potential_energy(m, g, x)
        total_e = ke + pe

        positions.append(x)
        velocities.append(v)
        kinetic_energies.append(ke)
        potential_energies.append(pe)
        total_energies.append(total_e)

    # ---- Combined Plots ----
    plt.figure(figsize=(10, 10))

    # Position
    plt.subplot(4, 1, 1)
    plt.plot(t_values, positions)
    plt.ylabel("Position (m)")
    plt.title("1D Motion with Energy Analysis")
    plt.grid()

    # Velocity
    plt.subplot(4, 1, 2)
    plt.plot(t_values, velocities)
    plt.ylabel("Velocity (m/s)")
    plt.grid()

    # Energies
    plt.subplot(4, 1, 3)
    plt.plot(t_values, kinetic_energies, label="Kinetic Energy")
    plt.plot(t_values, potential_energies, label="Potential Energy")
    plt.ylabel("Energy (J)")
    plt.legend()
    plt.grid()

    # Total Energy
    plt.subplot(4, 1, 4)
    plt.plot(t_values, total_energies)
    plt.xlabel("Time (s)")
    plt.ylabel("Total Energy (J)")
    plt.grid()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_simulation()