"""Hotkeys for No Man's Sky."""

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
    COLOR_NOMANSSKY,
)


class NoMansSkyApp(KeyApp):
    name = "NoMansSky"

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
        "Interact",
        COLOR_3,
        Press(Keycode.E),
    )
    key_4 = MacroKey(
        "Scan",
        COLOR_4,
        Press(Keycode.C),
    )
    key_5 = MacroKey(
        "Inv",
        COLOR_5,
        Press(Keycode.TAB),
    )

    # third row
    key_6 = MacroKey(
        "Quick",
        COLOR_6,
        Press(Keycode.X),
    )
    key_7 = MacroKey(
        "Build",
        COLOR_7,
        Press(Keycode.Z),
    )
    key_8 = MacroKey(
        "Mode",
        COLOR_8,
        Press(Keycode.G),
    )

    # Fourth row
    key_9 = MacroKey(
        "Dash",
        COLOR_9,
        Sequence(Keycode.Q, Keycode.SPACE),
    )
    key_10 = MacroKey(
        "HUD",
        COLOR_10,
        Press(Keycode.H),
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
