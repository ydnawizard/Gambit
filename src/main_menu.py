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
gambit_header = EffectLabel(gambit_header_text, effect=gambit_header_effect)


#define play button animation
#play_button_text = "                     PLAY\n"
play_button_text = ascii_art.play_button
play_button_effect: EffectType = "Slide"
play_button_config = {
        "movement_speed": 0.9,
        }
play_button = EffectLabel(play_button_text, effect=play_button_effect, config=play_button_config)


#info_button_text = "                     INFO\n"
info_button_text = ascii_art.info_button
info_button_effect: EffectType = "Slide"
info_button_config = {
        "movement_speed": 0.6,
        }
info_button = EffectLabel(info_button_text, effect=info_button_effect, config=info_button_config)

#quit_button_text = "                     QUIT\n"
quit_button_text = ascii_art.quit_button
quit_button_effect: EffectType = "Slide"
quit_button_config = {
        "movement_speed": 0.3,
        }
quit_button = EffectLabel(quit_button_text, effect=quit_button_effect, config=quit_button_config)

class MyApp(App):
    async def on_mount(self) -> None:
        if self.screen.size.width > 150:
            header_width = round(self.screen.size.width/3)+ self.screen.size.width//15
            button_width = round(self.screen.size.width/3)+ self.screen.size.width//14
        else:
            header_width = round(self.screen.size.width/3)
            button_width = round(self.screen.size.width/3)
        header_height = self.screen.size.height//5
        gambit_header.styles.margin = header_height, header_width, 0, header_width
        play_button.styles.margin = 0, button_width, 0, button_width
        info_button.styles.margin = 0, button_width, 0, button_width
        quit_button.styles.margin = 0, button_width, 0, button_width
    def compose(self) -> ComposeResult:
        yield gambit_header
        yield play_button
        yield info_button
        yield quit_button
