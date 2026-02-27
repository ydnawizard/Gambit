import ascii_art
from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textualeffects.effects import EffectType
from textualeffects.widgets import EffectLabel

#define gambit header animation
gambit_header_text = ascii_art.gambit_header
gambit_header_effect: EffectType = "Rain"
gambit_header_config = {}
Gambit_Header = EffectLabel(gambit_header_text, effect=gambit_header_effect)

#define play button animation
#play_button_text = "                     PLAY\n"
play_button_text = ascii_art.play_button
play_button_effect: EffectType = "Slide"
play_button_config = {
        "movement_speed": 0.9,
        }
Play_Button = EffectLabel(play_button_text, effect=play_button_effect, config=play_button_config)


#info_button_text = "                     INFO\n"
info_button_text = ascii_art.info_button
info_button_effect: EffectType = "Slide"
info_button_config = {
        "movement_speed": 0.6,
        }
Info_Button = EffectLabel(info_button_text, effect=info_button_effect, config=info_button_config)

#quit_button_text = "                     QUIT\n"
quit_button_text = ascii_art.quit_button
quit_button_effect: EffectType = "Slide"
quit_button_config = {
        "movement_speed": 0.3,
        }
Quit_Button = EffectLabel(quit_button_text, effect=quit_button_effect, config=quit_button_config)

class MyApp(App):
    CSS_PATH = "grid_layout.tcss"
    def compose(self) -> ComposeResult:
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle
        yield Static("", classes="box")
        yield Static("", classes="box")
        yield Static("", classes="box")
        #New Line
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle
        yield Static("", classes="box")
        yield Static("", classes="box")
        yield Static("", classes="box")
        #New Line
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle
        yield Gambit_Header
        yield Static("", classes="box")
        yield Static("", classes="box")
        #New Line
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle
        yield Static("", classes="box")
        yield Static("", classes="box")
        yield Static("", classes="box")
        #New Line
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle LIne
        yield Play_Button
        yield Static("", classes="box")
        yield Static("", classes="box")
        #Middle Line 4
        yield Static("", classes="box")
        yield Static("", classes="box")
        yield Info_Button
        yield Static("", classes="box")
        yield Static("", classes="box")
        #New Line
        yield Static("", classes="box")
        yield Static("", classes="box")
        yield Quit_Button
        yield Static("", classes="box")
        yield Static("", classes="box")

