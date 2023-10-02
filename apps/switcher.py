"""Hotkeys for switching between desktop apps."""

try:
    from typing import Optional
except ImportError:
    pass

from apps.chrome import ChromeApp
from apps.spotify import SpotifyApp
from apps.mswindows import WindowsApp
from apps.word import WordApp
from apps.zoom import ZoomApp
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
    COLOR_CHROME,
    COLOR_CODE,
    COLOR_FILES,
    COLOR_MEDIA,
    COLOR_NOTION,
    COLOR_PYCHARM,
    COLOR_SLACK,
    COLOR_SPOTIFY,
    COLOR_SUBLIME_MERGE,
    COLOR_TERMINAL,
    COLOR_WINDOWS,
    COLOR_WORD,
    COLOR_ZOOM,
    OS_MAC,
)


class AppSwitcherApp(KeyApp):
    """
    App with commands for switching between desktop apps. Some desktop apps
    also have a context-specific app for that desktop app. These will display
    when you switch to the app with the hotkey.
    """

    name = "App Switcher"

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
        chrome_app = ChromeApp(app_pad, settings)
        spotify_app = SpotifyApp(app_pad, settings)
        word_app = WordApp(app_pad, settings)
        zoom_app = ZoomApp(app_pad, settings)
        windows_app = WindowsApp(app_pad, settings)


        # First row
        cls.key_0 = Key(
            text ="Back",
            color=COLOR_BACK,
            command=PreviousAppCommand()
        )
        cls.key_1 = Key(
            text="Windows",
            color=COLOR_WINDOWS,
            command=SwitchAppCommand(windows_app)
        )

        cls.key_2 = Key(
            text="Word",
            color=COLOR_WORD,
            command=SwitchAppCommand(word_app)
        )

        # Second row
        cls.key_3 = Key(
            text="Chrome",
            color=COLOR_CHROME,
            command=SwitchAppCommand(chrome_app)
        )
        #4
        cls.key_5 = Key(
            text="Zoom",
            color=COLOR_ZOOM,
            command=SwitchAppCommand(zoom_app)
        )

        # Third row
        #6
        cls.key_7 = Key(
            text="Spotify",
            color=COLOR_SPOTIFY,
            command=SwitchAppCommand(spotify_app)
        )
        #8

        # Fourth row
        # Media Keys ABOVE /\
