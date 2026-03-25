 # 1D Motion Simulator
# Calculates displacement and final velocity using kinematic equations

def motion_simulator(u, a, t):
    v = u + a * t
    s = u * t + 0.5 * a * t**2
    return s, v

# Main Program
if __name__ == "__main__":
    print("Welcome to the 1D Motion Simulator")

    u = float(input("Enter initial velocity (m/s): "))
    a = float(input("Enter acceleration (m/s^2): "))
    t = float(input("Enter time (s): "))

    displacement, final_velocity = motion_simulator(u, a, t)

    print("\nResults:")
    print(f"Displacement: {displacement:.2f} meters")
    print(f"Final Velocity: {final_velocity:.2f} m/s")