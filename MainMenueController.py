from transitions import Machine, State


class MainMenueController(Machine):
    main_menue_states = ["IDLE", "ACTIVE"]
    my_states = [
        State(name="IDLE", on_enter=["_deactivate"], on_exit=[]),
        State(name="ACTIVE", on_enter=["_activate"], on_exit=["_shutdown"]),
    ]
    main_menue_transitions = [
        {"trigger": "t_on", "source": "IDLE", "dest": "ACTIVE"},
        {"trigger": "t_off", "source": "ACTIVE", "dest": "IDLE"},
    ]

    def __init__(self) -> None:
        Machine.__init__(
            self,
            states=MainMenueController.my_states,
            transitions=MainMenueController.main_menue_transitions,
            initial=MainMenueController.my_states[0],
            ignore_invalid_triggers=True,
            queued=True,
        )

    def _shutdown(self):
        print("callback: on_exit ACTIVE state")

    def _activate(self):
        print("callback: on_enter ACTIVE state")

    def _deactivate(self):
        print("callback: on_enter IDLE state")
