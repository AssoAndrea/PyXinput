import ctypes
from ctypes import Structure, POINTER,util
from PyXConstants import *
import PyXConstants
import numpy

# load DLL
XINPUT_DLL = (
    "XInput1_4.dll",
    "XInput9_1_0.dll",
    "XInput1_3.dll",
    "XInput1_2.dll",
    "XInput1_1.dll"
)

xinput_lib = None

for name in XINPUT_DLL:
    found = ctypes.util.find_library(name)
    if found:
        xinput_lib = ctypes.WinDLL(found)
        break

if not xinput_lib:
    raise IOError("XInput library not found")

WORD = ctypes.c_ushort
BYTE = ctypes.c_ubyte
SHORT = ctypes.c_short
DWORD = ctypes.c_ulong
BOOL = ctypes.c_bool
LPWSTR = ctypes.c_wchar_p
UINT = ctypes.c_uint
WCHAR = ctypes.c_wchar


# region C-Classes
class GAMEPAD(Structure):
    _fields_ = [("wButtons", WORD),
                ("bLeftTrigger", BYTE),
                ("bRightTrigger", BYTE),
                ("sThumbLX", SHORT),
                ("sThumbLY", SHORT),
                ("sThumbRX", SHORT),
                ("sThumbRY", SHORT),
                ]


class STATE(Structure):
    _fields_ = [("dwPacketNumber", DWORD),
                ("Gamepad", GAMEPAD),
                ]


class VIBRATION(Structure):
    _fields_ = [("wLeftMotorSpeed", WORD),
                ("wRightMotorSpeed", WORD),
                ]


class CAPABILITIES(Structure):
    _fields_ = [("Type", BYTE),
                ("SubType", BYTE),
                ("Flags", WORD),
                ("Gamepad", GAMEPAD),
                ("Vibration", VIBRATION),
                ]


class BATTERY_INFORMATION(Structure):
    _fields_ = [("BatteryType", BYTE),
                ("BatteryLevel", BYTE),
                ]

class KEYSTROKE(Structure):
    _fields_ = [("VirtualKey", WORD),
                ("Unicode", WCHAR),
                ("Flags", WORD),
                ("UserIndex", BYTE),
                ("HidCode", BYTE),
                ]

# endregion

xinput_lib.XInputGetState.argtypes = [DWORD, POINTER(STATE)]
xinput_lib.XInputGetState.restype = DWORD

def pyX_get_state(dwUserIndex, pState):
    return xinput_lib.XInputGetState(dwUserIndex, ctypes.byref(pState))

xinput_lib.XInputSetState.argtypes = [DWORD, POINTER(VIBRATION)]
xinput_lib.XInputSetState.restype = DWORD

def pyX_set_state(dwUserIndex, vibration):
    return xinput_lib.XInputSetState(dwUserIndex, ctypes.byref(vibration))

xinput_lib.XInputGetCapabilities.argtypes = [DWORD, DWORD, POINTER(CAPABILITIES)]
xinput_lib.XInputGetCapabilities.restype = DWORD

def pyX_get_capabilities(dwUserIndex, dwFlags, pCapabilities):
    return xinput_lib.XInputGetCapabilities(dwUserIndex,dwFlags,ctypes.byref(pCapabilities))

xinput_lib.XInputEnable.argtypes = [BOOL]

def pyX_input_enable(enable):
    xinput_lib.XInputEnable(enable)
    return

# TODO: XInputGetAudioDeviceIds _Out_writes_opt_ test if work
xinput_lib.XInputGetAudioDeviceIds.argtypes = [DWORD, POINTER(LPWSTR),POINTER(UINT),POINTER(LPWSTR),POINTER(UINT)]
xinput_lib.XInputGetAudioDeviceIds.restype = DWORD

def pyX_get_Audio_Device_Ids(dwUserIndex,pRenderDeviceId = None,pRenderCount = None,pCaptureDeviceId = None,pCaptureCount = None):
    return xinput_lib.XInputGetAudioDeviceIds(dwUserIndex,ctypes.byref(pRenderDeviceId),ctypes.byref(pRenderCount),ctypes.byref(pCaptureDeviceId),ctypes.byref(pCaptureCount))

xinput_lib.XInputGetBatteryInformation.argtypes = [DWORD, BYTE, POINTER(BATTERY_INFORMATION)]
xinput_lib.XInputGetBatteryInformation.restype = DWORD

def pyX_get_battery_info(dwUserIndex, devType, batteryInformation):
    return xinput_lib.XInputGetBatteryInformation(dwUserIndex, devType, ctypes.byref(batteryInformation))

xinput_lib.XInputGetKeystroke.argtypes = [DWORD, DWORD, POINTER(KEYSTROKE)]
xinput_lib.XInputGetKeystroke.restype = DWORD

def pyX_get_keystroke(dwUserIndex, dwReserved, pKeystroke):
    return xinput_lib.XInputGetBatteryInformation(dwUserIndex,dwReserved, ctypes.byref(pKeystroke))

def set_deadzone(deadzone,value):
    if deadzone == GAMEPAD_TRIGGER_THRESHOLD:
        if value <= 0 or value > 255:
            raise ValueError("invalid value for trigger, must be greather than 0 and lower of 255")
    else:
        if value <=0 or value > 32767:
            raise ValueError("invalid value for trigger, must be greather than 0 and lower of 255")

    if deadzone == GAMEPAD_RIGHT_THUMB_DEADZONE:
        PyXConstants.GAMEPAD_RIGHT_THUMB_DEADZONE = value
    if deadzone == GAMEPAD_LEFT_THUMB_DEADZONE:
        PyXConstants.GAMEPAD_LEFT_THUMB_DEADZONE = value
    if deadzone == GAMEPAD_TRIGGER_THRESHOLD:
        PyXConstants.GAMEPAD_TRIGGER_THRESHOLD = value

def set_motor_speed(user,right_speed,left_speed):
    right_speed = numpy.clip(right_speed,0,1)
    left_speed = numpy.clip(left_speed,0,1)
    right_speed = 65535 * right_speed
    left_speed = 65535 * left_speed
    vibration = VIBRATION()
    vibration.wLeftMotorSpeed = int(left_speed)
    vibration.wRightMotorSpeed = int(right_speed)
    return pyX_set_state(user,vibration) == 0

