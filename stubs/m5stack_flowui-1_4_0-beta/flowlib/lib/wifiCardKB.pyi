
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Btn:
    def attach() -> None: ...
    def deinit() -> None: ...
    def detach() -> None: ...
    def multiBtnCb() -> None: ...
    def restart() -> None: ...
    def timerCb() -> None: ...
class BtnChild:
    def deinit() -> None: ...
    def isPressed() -> None: ...
    def isReleased() -> None: ...
    def pressFor() -> None: ...
    def restart() -> None: ...
    def upDate() -> None: ...
    def wasDoublePress() -> None: ...
    def wasPressed() -> None: ...
    def wasReleased() -> None: ...
class IP5306:
    def getBatteryLevel() -> None: ...
    def init() -> None: ...
    def isChargeFull() -> None: ...
    def isCharging() -> None: ...
    def setCharge() -> None: ...
    def setChargeVolt() -> None: ...
    def setVinMaxCurrent() -> None: ...
class M5Button: ...
class M5Circle:
    def hide() -> None: ...
    def setBgColor() -> None: ...
    def setBorderColor() -> None: ...
    def setPosition() -> None: ...
    def setSize() -> None: ...
    def show() -> None: ...
class M5Img:
    def changeImg() -> None: ...
    def hide() -> None: ...
    def setPosition() -> None: ...
    def show() -> None: ...
class M5Rect:
    def hide() -> None: ...
    def setBgColor() -> None: ...
    def setBorderColor() -> None: ...
    def setPosition() -> None: ...
    def setSize() -> None: ...
    def show() -> None: ...
class M5TextBox:
    def hide() -> None: ...
    def setColor() -> None: ...
    def setFont() -> None: ...
    def setPosition() -> None: ...
    def setRotate() -> None: ...
    def setText() -> None: ...
    def show() -> None: ...
class M5Title:
    def hide() -> None: ...
    def setBgColor() -> None: ...
    def setFgColor() -> None: ...
    def setTitle() -> None: ...
    def show() -> None: ...
def M5UI_Deinit() -> None: ...
class Rgb_multi:
    def deinit() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorAll() -> None: ...
    def setColorFrom() -> None: ...
    def setShowLock() -> None: ...
    def show() -> None: ...
class Speaker:
    def _timeout_cb() -> None: ...
    def checkInit() -> None: ...
    def setBeat() -> None: ...
    def setVolume() -> None: ...
    def sing() -> None: ...
    def tone() -> None: ...
def btnText() -> None: ...
def const() -> None: ...
def get_sd_state() -> None: ...
def hwDeinit() -> None: ...
def sd_mount() -> None: ...
def sd_umount() -> None: ...
def setScreenColor() -> None: ...
