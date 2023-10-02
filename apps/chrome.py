# MACROPAD Hotkeys example: Firefox web browser for Linux

from utils.apps.key import KeyApp, MacroKey
from utils.commands import (
    Keycode,
    MacroCommand,
    Press,
    PreviousAppCommand,
    Release,
    Sequence,
    Text,
    Wait,
)
from utils.constants import (
    COLOR_1,
    COLOR_3,
    COLOR_5,
    COLOR_6,
    COLOR_7,
    COLOR_8,
    COLOR_9,
    COLOR_BACK,
    COLOR_CHROME,
    COLOR_CLOSE,
    OS_MAC,
)


class ChromeApp(KeyApp):
    name = "Chrome"

    # First row
    key_0 = MacroKey(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )
    key_1 = MacroKey(
        "+Bkmk",
        COLOR_1,
        Press(Keycode.CONTROL, Keycode.D),
        mac_command=Press(Keycode.COMMAND, Keycode.D),
    )
    key_2 = MacroKey(
        "Exit",
        COLOR_CLOSE,
        Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        ),
        mac_command=Sequence(Press(Keycode.COMMAND, Keycode.Q), PreviousAppCommand()),
    )

    # Second row
    key_3 = MacroKey(
        "<-Tab",
        COLOR_3,
        Sequence(
            Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB),
        ),
    )
    key_4 = MacroKey(
        "CloseTab",
        COLOR_CLOSE,
        Press(Keycode.CONTROL, Keycode.W),
        mac_command=Press(Keycode.COMMAND, Keycode.W),
    )
    key_5 = MacroKey(
        "Tab->",
        COLOR_5,
        Sequence(
            Press(Keycode.CONTROL, Keycode.TAB),
        ),
    )

    # Third row
    key_6 = MacroKey(
        "<-",
        COLOR_6,
        Press(Keycode.ALT, Keycode.LEFT_ARROW),
        mac_command=Press(Keycode.COMMAND, Keycode.LEFT_ARROW),
    )
    key_7 = MacroKey(
        "Reload",
        COLOR_7,
        Press(Keycode.CONTROL, Keycode.R),
        mac_command=Press(Keycode.COMMAND, Keycode.R),
    )
    key_8 = MacroKey(
        "->",
        COLOR_8,
        Press(Keycode.ALT, Keycode.RIGHT_ARROW),
        mac_command=Press(Keycode.COMMAND, Keycode.RIGHT_ARROW),
    )

    # Fourth row
    key_9 = MacroKey(
        "Menu",
        COLOR_CHROME,
        Press(Keycode.ALT, Keycode.E),
        mac_command=None,
    )
    key_10 = MacroKey(
        "Book",
        COLOR_1,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.O),
        mac_command=Press(Keycode.COMMAND, Keycode.OPTION, Keycode.B),
    )
    key_11 = MacroKey(
        "Hist",
        COLOR_CHROME,
        Press(Keycode.CONTROL, Keycode.H),
        mac_command=Press(Keycode.COMMAND, Keycode.Y),
    )

    encoder_button = MacroCommand(
        Sequence(
            Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.A),
            Wait(0.1),
            Release(Keycode.A, Keycode.SHIFT, Keycode.CONTROL),
        ),
        **{
            OS_MAC: Sequence(
                Press(Keycode.COMMAND, Keycode.SHIFT, Keycode.A),
                Wait(0.1),
                Release(Keycode.A, Keycode.SHIFT, Keycode.COMMAND),
            )
        },
    )

    encoder_decrease = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_UP),
        **{OS_MAC: Press(Keycode.COMMAND, Keycode.OPTION, Keycode.LEFT_ARROW)},
    )
    encoder_increase = MacroCommand(
        Press(Keycode.CONTROL, Keycode.PAGE_DOWN),
        **{OS_MAC: Press(Keycode.COMMAND, Keycode.OPTION, Keycode.RIGHT_ARROW)},
    )
