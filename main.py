 # 1D Motion Simulator with Acceleration

def calculate_velocity(u, a, t):
    return u + a * t

def calculate_position(x0, u, a, t):
    return x0 + u * t + 0.5 * a * t**2


def run_simulation():
    print("=== 1D Motion Simulator ===")

    # Input for values
    x0 = float(input("Enter initial position (m): "))
    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    total_time = float(input("Enter total simulation time (s): "))
    dt = float(input("Enter time step (e.g. 0.1): "))

    print("\nTime | Position (m) | Velocity (m/s)")
    print("-" * 40)

    t = 0.0
    while t <= total_time:
        x = calculate_position(x0, u, a, t)
        v = calculate_velocity(u, a, t)

        print(f"{t:5.2f} | {x:12.4f} | {v:14.4f}")

        t += dt


# Run the simulation
run_simulation()