from transitions import Machine


class MainMenueController(Machine):
    main_menue_states = ["IDLE", "ACTIVE"]
    main_menue_transitions = [
        {"trigger": "t_on", "source": "IDLE", "dest": "ACTIVE"},
        {"trigger": "t_off", "source": "ACTIVE", "dest": "IDLE"},
    ]

    def __init__(self) -> None:
        Machine.__init__(
            self,
            states=MainMenueController.main_menue_states,
            transitions=MainMenueController.main_menue_transitions,
            initial=MainMenueController.main_menue_states[0],
            ignore_invalid_triggers=True,
            queued=True,
        )

    def on_enter_ACTIVE(self):
        print("now active")

    def on_enter_IDLE(self):
        print("now idle")
