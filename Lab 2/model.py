

# Stateful Classroom Agent

class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def choose_mode(self, occupied, temperature):
        if not occupied:
            target_mode = "ECO"
        elif temperature > 26:
            target_mode = "COOL"
        elif temperature < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if target_mode != self.previous_mode:
            send_command = True
        else:
            send_command = False

        self.previous_mode = target_mode

        return target_mode, send_command
