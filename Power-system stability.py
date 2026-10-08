# Power-system-stability
print("Power-System Stability Analysis")

E = float(input("Enter generator internal voltage E (pu): "))
V = float(input("Enter bus voltage V (pu): "))
X = float(input("Enter transfer reactance X (pu): "))
delta = float(input("Enter power angle δ (degrees): "))

if X <= 0:
    print("Reactance must be greater than zero.")
else:
    # Convert angle from degrees to radians
    delta_rad = math.radians(delta)

    # Electrical power transferred
    Pe = (E * V / X) * math.sin(delta_rad)

    # Maximum transferable power
    Pmax = E * V / X

    print("\n--- Stability Results ---")
    print("Electrical Power =", Pe, "pu")
    print("Maximum Power =", Pmax, "pu")
    print("Power Angle =", delta, "degrees")

    # Basic stability check
    if 0 <= delta < 90:
        print("System Status: STABLE")
    elif 90 <= delta < 180:
        print("System Status: Critical / Reduced Stability")
    else:
        print("System Status: UNSTABLE")
