
import nes, lcd
from Maix import GPIO
from fpioa_manager import fm

# 音频使能IO
AUDIO_PA_EN_PIN = 32

#注册音频使能IO
if AUDIO_PA_EN_PIN:
    fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1, force=True)

#LCD初始化
lcd.init()

#初始化nes，配置为键盘控制
nes.init(nes.KEYBOARD)

#运行游戏
nes.run("/sd/Bomberman.nes")
