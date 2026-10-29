
# Testing the Stateful Classroom Agent

from model import ClassroomAgent

agent = ClassroomAgent()

test_cases = [
    (True, 28),
    (True, 28),
    (True, 20),
    (True, 26),
    (True, 18),
    (False, 24),
    (False, 24)
]

print("Stateful Agent Test")
print("-------------------")

for occupied, temperature in test_cases:
    old_mode = agent.previous_mode

    target_mode, send_command = agent.choose_mode(
        occupied, temperature
    )

    if send_command:
        status = "SEND COMMAND"
    else:
        status = "NO COMMAND"

    print(
        "Previous Mode:", old_mode,
        "| Occupied:", occupied,
        "| Temperature:", temperature,
        "| Target:", target_mode,
        "| Status:", status
    )