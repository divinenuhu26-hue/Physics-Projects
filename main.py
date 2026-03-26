import numpy as np
import matplotlib.pyplot as plt

# Physics functions
def calculate_position(x0, u, a, t):
    return x0 + u*t + 0.5*a*t**2

def calculate_velocity(u, a, t):
    return u + a*t


def run_simulation():
    print("=== 1D Motion Simulator with Graphs ===")

    # User inputs
    x0 = float(input("Enter initial position (m): "))
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    total_time = float(input("Enter total time (s): "))
    dt = float(input("Enter time step (e.g. 0.1): "))

    # Time array
    t_values = np.arange(0, total_time, dt)

    # Lists to store results
    positions = []
    velocities = []

    # Compute values
    for t in t_values:
        x = calculate_position(x0, u, a, t)
        v = calculate_velocity(u, a, t)

        positions.append(x)
        velocities.append(v)

    # ---- Plot Position vs Time ----
    plt.figure()
    plt.plot(t_values, positions)
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.title("Position vs Time")
    plt.grid()

    # ---- Plot Velocity vs Time ----
    plt.figure()
    plt.plot(t_values, velocities)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity vs Time")
    plt.grid()

    plt.show()


# Run program
if __name__ == "__main__":
    run_simulation()