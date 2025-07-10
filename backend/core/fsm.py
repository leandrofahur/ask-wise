class FSM:
    def __init__(self):
        # Quintuple (x_0, X, X_marked, E, f)
        # x_0 = initial state
        pass

    def set_initial_state(self):
        pass

    def set_states(self):
        pass

    def set_marked_states(self):
        pass

    def set_events(self):
        pass

    def set_transition_function(self):
        pass

    def run(self):
        pass


# x_0 = "OFF"
# X = ["OFF", "ON", "ERROR"]
# X_marked = ["OFF", "ERROR"]

# E = ["TURN_ON", "TURN_OFF", "ERROR"]

# f = {
#     ("OFF", "TURN_ON"): "ON",
#     ("ON", "TURN_OFF"): "OFF",
#     ("ON", "ERROR"): "ERROR",
#     ("OFF", "ERROR"): "ERROR",
#     ("ERROR", "TURN_ON"): "ERROR",
#     ("ERROR", "TURN_OFF"): "ERROR",
#     ("ERROR", "ERROR"): "ERROR",
# }

# print(f[("OFF", "TURN_ON")])

# current_state = x_0
# for event in E:
#     print(f"({current_state} x {event}) -> {f[(current_state, event)]}")
#     current_state = f[(current_state, event)]
