from terminaltexteffects.effects.effect_rain import Rain

text = """
  ______ _______ _______ ______  _____ _______
 |  ____ |_____| |  |  | |_____]   |      |   
 |_____| |     | |  |  | |_____] __|__    |   
                                                      """

def rain_effect(text):
    effect = Rain(text)
    effect.effect_config.merge = True # 
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

