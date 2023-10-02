"""Hotkeys for Zoom"""

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
    COLOR_3,
    COLOR_4,
    COLOR_5,
    COLOR_6,
    COLOR_7,
    COLOR_8,
    COLOR_BACK,
    COLOR_CLOSE,
    COLOR_MEDIA,
    COLOR_ZOOM,
    OS_MAC,
)


class ZoomApp(KeyApp):
    name = "Zoom"

    key_0 = Key(
        "Back",
        COLOR_BACK,
        PreviousAppCommand(),
        double_tap_command=PreviousAppCommand(),
    )

    key_2 = Key(
        "Exit",
        COLOR_CLOSE,
        Sequence(
            Press(Keycode.ALT, Keycode.F4),
            PreviousAppCommand(),
        )
    )
    
    key_3 = Key(
        "TogVid",
        COLOR_3,
        Press(Keycode.ALT, Keycode.V),
    )
    key_4 = Key(
        "TogMic",
        COLOR_4,
        Press(Keycode.ALT, Keycode.A),
    )
    key_5 = Key(
        "Chat",
        COLOR_5,
        Press(Keycode.ALT, Keycode.H),
    )
    key_6 = Key(
        "Part",
        COLOR_6,
        Press(Keycode.ALT, Keycode.U),
    )
    key_7 = Key(
        "Gallery",
        COLOR_7,
        Press(Keycode.ALT, Keycode.F2),
    )
    key_8 = Key(
        "Active",
        COLOR_8,
        Press(Keycode.ALT, Keycode.F1),
    )

    # Fourth row
    key_9 = Key("<<", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_PREVIOUS_TRACK))
    key_10 = Key(">||", COLOR_MEDIA, Media(ConsumerControlCode.PLAY_PAUSE))
    key_11 = Key(">>", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_NEXT_TRACK))


    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
