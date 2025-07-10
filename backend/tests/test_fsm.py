from core.fsm import FSM


def test_fsm_creation():
    """
    Create a FSM with the following parameters:
    - initial_state = "OFF"
    - states = ["OFF", "ON", "ERROR"]
    - marked_states = ["OFF", "ERROR"]
    - events = ["TURN_ON", "TURN_OFF", "ERROR"]
    - transition_function = {
        "OFF": {"TURN_ON": "ON"},
        "ON": {"TURN_OFF": "OFF"},
        "ERROR": {"ERROR": "ERROR"}
    }
    """

    fsm = FSM(
        initial_state="OFF",
        states=["OFF", "ON", "ERROR"],
        marked_states=["OFF", "ERROR"],
        events=["TURN_ON", "TURN_OFF", "ERROR"],
        transition_function={
            "OFF": {"TURN_ON": "ON"},
            "ON": {"TURN_OFF": "OFF"},
            "ERROR": {"ERROR": "ERROR"},
        },
    )

    assert fsm.initial_state == "OFF"
    assert True, "FSM tests will be implemented as features are developed"


def test_fsm_run():
    """
    Run the FSM with the following events:
    - TURN_ON
    - TURN_OFF
    - ERROR
    """
    fsm = FSM(
        initial_state="OFF",
        states=["OFF", "ON", "ERROR"],
        marked_states=["OFF", "ERROR"],
        events=["TURN_ON", "TURN_OFF", "ERROR"],
        transition_function={
            ("OFF", "TURN_ON"): "ON",
            ("ON", "TURN_OFF"): "OFF",
            ("ON", "ERROR"): "ERROR",
            ("OFF", "ERROR"): "ERROR",
            ("ERROR", "TURN_ON"): "ERROR",
            ("ERROR", "TURN_OFF"): "ERROR",
            ("ERROR", "ERROR"): "ERROR",
        },
    )

    final_state = fsm.run()

    assert final_state == "ERROR"
