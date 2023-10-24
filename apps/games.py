"""Hotkeys for switching between games."""

try:
    from typing import Optional
except ImportError:
    pass

from apps.hots import HOTSApp
from apps.idlechampions import IdleChampionsApp
from apps.oni import ONIApp
from apps.msfs import MSFSApp
from apps.starfield import StarfieldApp
from apps.stinfinite import STInfiniteApp

from apps.func import FuncKeysApp
from apps.numpad import NumpadApp

from utils.app_pad import AppPad
from utils.apps.key import Key, KeyApp, KeyAppSettings, MacroKey
from utils.commands import (
    ConsumerControlCode,
    Keycode,
    MacroCommand,
    Media,
    Press,
    PreviousAppCommand,
    Release,
    Sequence,
    SwitchAppCommand,
    Wait,
)
from utils.constants import (
    COLOR_BACK,
    COLOR_FILES,
    COLOR_FUNC,
    COLOR_MEDIA,
    COLOR_NUMPAD,
    COLOR_WINDOWS,

    COLOR_HOTS,
    COLOR_IDLECHAMPIONS,
    COLOR_MSFS,
    COLOR_ONI,
    COLOR_STARFIELD,
    COLOR_STINFINITE,
)


class GamesApp(KeyApp):
    """
    App with commands for switching between games.
    """

    name = "Games"

    # Fourth row
    key_9 = Key("<<", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_PREVIOUS_TRACK))
    key_10 = Key(">||", COLOR_MEDIA, Media(ConsumerControlCode.PLAY_PAUSE))
    key_11 = Key(">>", COLOR_MEDIA, Media(ConsumerControlCode.SCAN_NEXT_TRACK))

    encoder_button = Media(ConsumerControlCode.MUTE)

    encoder_increase = Media(ConsumerControlCode.VOLUME_INCREMENT)
    encoder_decrease = Media(ConsumerControlCode.VOLUME_DECREMENT)

    def __init__(self, app_pad: AppPad, settings: Optional[KeyAppSettings] = None):
        self.initialize_settings_dependent_keys(app_pad, settings)
        super().__init__(app_pad, settings=settings)

    @classmethod
    def initialize_settings_dependent_keys(
        cls, app_pad: AppPad, settings: Optional[KeyAppSettings] = None
    ):
        hots_app = HOTSApp(app_pad, settings)
        idlechampions_app = IdleChampionsApp(app_pad, settings)
        msfs_app = MSFSApp(app_pad, settings)
        oni_app = ONIApp(app_pad, settings)
        starfield_app = StarfieldApp(app_pad, settings)
        stinfinite_app = STInfiniteApp(app_pad, settings)


        # First row
        cls.key_0 = Key(
            text ="Back",
            color=COLOR_BACK,
            command=PreviousAppCommand()
        )

        func_keys_app = FuncKeysApp(app_pad, settings)
        cls.key_1 = Key(
            text="Func", color=COLOR_FUNC, command=SwitchAppCommand(func_keys_app)
        )

        numpad_app = NumpadApp(app_pad, settings)
        cls.key_2 = Key(
            text="Num", color=COLOR_NUMPAD, command=SwitchAppCommand(numpad_app)
        )

        # Second row
        cls.key_3 = Key(
            text="HOTS",
            color=COLOR_HOTS,
            command=SwitchAppCommand(hots_app)
        )

        cls.key_4 = Key(
            text="IdleChamp",
            color=COLOR_IDLECHAMPIONS,
            command=SwitchAppCommand(idlechampions_app)
        )

        cls.key_5 = Key(
            text="Flight",
            color=COLOR_MSFS,
            command=SwitchAppCommand(msfs_app)
        )

        # Third row
        cls.key_6 = Key(
            text="ONI",
            color=COLOR_ONI,
            command=SwitchAppCommand(oni_app)
        )

        cls.key_7 = Key(
            text="Starfield",
            color=COLOR_STARFIELD,
            command=SwitchAppCommand(starfield_app)
        )

        cls.key_8 = Key(
            text="TrekInf",
            color=COLOR_STINFINITE,
            command=SwitchAppCommand(stinfinite_app)
        )
        # Fourth row
        # Media Keys ABOVE /\
