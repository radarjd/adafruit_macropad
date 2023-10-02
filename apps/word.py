"""Hotkeys for Word"""

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
    COLOR_WORD,
    OS_MAC,
)


class WordApp(KeyApp):
    name = "Word"

    # First row
    key_0 = Key(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )
    key_1 = MacroKey(
        "New",
        COLOR_1,
        Press(Keycode.CONTROL, Keycode.N),
    )
    key_2 = MacroKey(
        "Exit",
        COLOR_CLOSE,
        Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )

    # Second row
    key_3 = MacroKey(
        "Open",
        COLOR_3,
        Press(Keycode.CONTROL, Keycode.O),
    )
    key_4 = MacroKey(
        "Save",
        COLOR_4,
        Press(Keycode.CONTROL, Keycode.S),
    )
    key_5 = MacroKey(
        "Print",
        COLOR_5,
        Press(Keycode.CONTROL, Keycode.P),
    )

    # Third row
    key_6 = MacroKey(
        "Cut",
        COLOR_6,
        Press(Keycode.CONTROL, Keycode.X),
    )
    key_7 = MacroKey(
        "Copy",
        COLOR_7,
        Press(Keycode.CONTROL, Keycode.C),
    )
    key_8 = MacroKey(
        "Paste",
        COLOR_8,
        Press(Keycode.CONTROL, Keycode.V),
    )

    # Fourth row
    key_9 = MacroKey(
        "Undo",
        COLOR_9,
        Press(Keycode.CONTROL, Keycode.Z),
    )
    key_10 = MacroKey(
        "Redo",
        COLOR_10,
        Press(Keycode.CONTROL, Keycode.Y),
    )
    key_11 = MacroKey(
        "Replace",
        COLOR_2,
        Press(Keycode.CONTROL, Keycode.H),
    )


    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
