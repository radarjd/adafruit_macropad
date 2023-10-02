# Nav cluster

from utils.apps.key import Key, KeyApp, MacroKey
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    Media,
    Press,
    PreviousAppCommand,
)
from utils.constants import COLOR_2, COLOR_4, COLOR_8, COLOR_ALERT, COLOR_CLOSE, COLOR_NAV


class NavApp(KeyApp):
    name = "Navigation"


    key_0 = Key(
        text ="Back",
        color=COLOR_CLOSE,
        command=PreviousAppCommand()
    )

    key_1 = Key("PrtScrn", COLOR_8, Press(Keycode.PRINT_SCREEN))
    key_2 = Key(
        "Home",
        COLOR_2,
        Press(Keycode.HOME),
    )
    key_3 = Key(
        "PgUp", COLOR_4, Press(Keycode.PAGE_UP)
    )

    key_4 = Key("Del", COLOR_ALERT, Press(Keycode.DELETE))
    key_5 = Key(
        "End",
        COLOR_2,
        Press(Keycode.END),
    )
    key_6 = Key("PgDn", COLOR_4, Press(Keycode.PAGE_DOWN))

    key_7 = Key("/\\", COLOR_NAV, Press(Keycode.UP_ARROW))

    key_9 = Key("<-", COLOR_NAV, Press(Keycode.LEFT_ARROW))
    key_10 = Key("\\/", COLOR_NAV, Press(Keycode.DOWN_ARROW))
    key_11 = Key("->", COLOR_NAV, Press(Keycode.RIGHT_ARROW))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)
