"""Hotkeys for Oxygen Not Included."""

from utils.apps.key import Key, KeyApp, MacroKey
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    MacroCommand,
    Media,
    Press,
    PreviousAppCommand,
    Sequence,
)
from utils.constants import (
    COLOR_1,
    COLOR_2,
    COLOR_3,
    COLOR_4,
    COLOR_5,
    COLOR_6,
    COLOR_7,
    COLOR_8,
    COLOR_9,
    COLOR_10,
    COLOR_BACK,
    COLOR_CLOSE,
    COLOR_MEDIA,
    COLOR_ONI,
)


class ONIApp(KeyApp):
    name = "Oxygen Not Inc"

    key_0 = Key(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )

    key_2 = MacroKey(
        "Exit",
        COLOR_CLOSE,
        Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )
    
    # second row
    key_3 = MacroKey(
        "Map",
        COLOR_3,
        Press(Keycode.M),
    )
    key_4 = MacroKey(
        "Chest",
        COLOR_4,
        Press(Keycode.O),
    )
    key_5 = MacroKey(
        "Patron",
        COLOR_5,
        Press(Keycode.P),
    )

    # third row
    key_6 = MacroKey(
        "Parties",
        COLOR_6,
        Press(Keycode.FORWARD_SLASH),
    )
    key_7 = MacroKey(
        "Shop",
        COLOR_7,
        Press(Keycode.S),
    )
    key_8 = MacroKey(
        "Pots",
        COLOR_8,
        Press(Keycode.TAB),
    )

    # Fourth row
    key_9 = MacroKey(
        "Auto",
        COLOR_9,
        Press(Keycode.G),
    )
    key_10 = MacroKey(
        "Core",
        COLOR_10,
        Press(Keycode.N),
    )
    key_11 = MacroKey(
        "Menu",
        COLOR_1,
        Press(Keycode.ESCAPE),
    )

    encoder_button = Media(ConsumerControlCode.MUTE)
    encoder_increase = MacroCommand(
        Press(Keycode.CONTROL, Keycode.UP_ARROW),
    )
    encoder_decrease = MacroCommand(
        Press(Keycode.CONTROL, Keycode.DOWN_ARROW),
    )
