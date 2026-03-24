
# 1D Motion Simulator
# Calculates displacement and final velocity using kinematic equations

def motion_simulator(u, a, t):
    """
    u : initial velocity (m/s)
    a : acceleration (m/s^2)
    t : time (s)
    
    Returns:
    displacement (s) in meters
    final velocity (v) in m/s
    """
    # Kinematic equations
    v = u + a * t
    s = u * t + 0.5 * a * t**2
    return s, v

# Main Program 
if __name__ == "__main__":
    print(" Welcome to the 1D Motion Simulator")
    
    # Get user input
    try:
        u = float(input("Enter initial velocity (m/s): "))
        a = float(input("Enter acceleration (m/s^2): "))
        t = float(input("Enter time (s): "))
    except ValueError:
        print("Error: Please enter numeric values only.")
        exit()
    
    # Calculate
    displacement, final_velocity = motion_simulator(u, a, t)
    
    # Output
    print(f"\nResults:")
    print(f"Displacement: {displacement:.2f} meters")
    print(f"Final Velocity: {final_velocity:.2f} m/s")
print("Hello, Physics World!")
