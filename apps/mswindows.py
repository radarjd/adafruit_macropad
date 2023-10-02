"""Hotkeys for Windows"""

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
)


class WindowsApp(KeyApp):
    name = "Windows"

    # First row
    key_0 = Key(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )
    key_1 = Key(
        "Switch",
        COLOR_1,
        Press(Keycode.ALT, Keycode.TAB),
    )
    key_2 = Key(
        "Quit",
        COLOR_CLOSE,
        Press(Keycode.ALT, Keycode.F4),
    )

    # Second row
    key_3 = Key(
        "Lock",
        COLOR_3,
        Press(Keycode.WINDOWS, Keycode.L),
    )
    key_4 = Key(
        "Explorer",
        COLOR_4,
        Press(Keycode.WINDOWS, Keycode.E),
    )
    key_5 = Key(
        "Task",
        COLOR_5,
        Press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE),
    )

    # Third row
    key_6 = Key(
        "Cut",
        COLOR_6,
        Press(Keycode.CONTROL, Keycode.X),
    )
    key_7 = Key(
        "Copy",
        COLOR_7,
        Press(Keycode.CONTROL, Keycode.C),
    )
    key_8 = Key(
        "Paste",
        COLOR_8,
        Press(Keycode.CONTROL, Keycode.V),
    )

    # Fourth row
    key_9 = Key(
        "Undo",
        COLOR_9,
        Press(Keycode.CONTROL, Keycode.Z),
    )
    key_10 = Key(
        "Redo",
        COLOR_10,
        Press(Keycode.CONTROL, Keycode.Y),
    )
    key_11 = Key(
        "Desktop",
        COLOR_2,
        Press(Keycode.WINDOWS, Keycode.D),
    )


    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
