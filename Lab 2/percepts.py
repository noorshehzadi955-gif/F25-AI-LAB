
# Lab 2 - Basic Classroom Agent

def choose_mode(occupied, temperature):
    if not occupied:
        return "ECO"
    elif temperature > 26:
        return "COOL"
    elif temperature < 20:
        return "WARM"
    else:
        return "IDLE"


# Classroom percepts: (occupied, temperature)
percepts = [
    (True, 28),
    (True, 28),
    (True, 18),
    (True, 20),
    (True, 26),
    (False, 24)
]

print("Basic Classroom Agent Trace")
print("---------------------------")

for occupied, temperature in percepts:
    mode = choose_mode(occupied, temperature)

    print(
        "Occupied:", occupied,
        "| Temperature:", temperature,
        "| Action:", mode
    )
