import ctypes
from ctypes import Structure, POINTER,util
from PyXConstants import *
import PyXConstants
import numpy
import inspect

xinput_lib = None

def load_DLL(is_test=False):
    global xinput_lib
    # load DLL
    FAKE_XINPUT_DLL = "Test_FakeXinputDLL\\FakeXinput.dll"

    XINPUT_DLL = (
        "XInput1_4.dll",
        "XInput9_1_0.dll",
        "XInput1_3.dll",
        "XInput1_2.dll",
        "XInput1_1.dll"
    )
    if is_test:
        xinput_lib = ctypes.WinDLL(FAKE_XINPUT_DLL)
    else:
        for name in XINPUT_DLL:
            found = ctypes.util.find_library(name)
            if found:
                xinput_lib = ctypes.WinDLL(found)
                break

    if not xinput_lib:
        raise IOError("XInput library not found")

    xinput_lib.XInputGetState.argtypes = [DWORD, POINTER(STATE)]
    xinput_lib.XInputGetState.restype = DWORD

    xinput_lib.XInputSetState.argtypes = [DWORD, POINTER(VIBRATION)]
    xinput_lib.XInputSetState.restype = DWORD

    xinput_lib.XInputGetCapabilities.argtypes = [DWORD, DWORD, POINTER(CAPABILITIES)]
    xinput_lib.XInputGetCapabilities.restype = DWORD

    xinput_lib.XInputEnable.argtypes = [BOOL]

    # TODO: XInputGetAudioDeviceIds _Out_writes_opt_ test if work
    xinput_lib.XInputGetAudioDeviceIds.argtypes = [DWORD, LPWSTR, POINTER(UINT), LPWSTR,
                                                   POINTER(UINT)]
    xinput_lib.XInputGetAudioDeviceIds.restype = DWORD

    xinput_lib.XInputGetBatteryInformation.argtypes = [DWORD, BYTE, POINTER(BATTERY_INFORMATION)]
    xinput_lib.XInputGetBatteryInformation.restype = DWORD

    xinput_lib.XInputGetKeystroke.argtypes = [DWORD, DWORD, POINTER(KEYSTROKE)]
    xinput_lib.XInputGetKeystroke.restype = DWORD
    return xinput_lib


WORD = ctypes.c_ushort
BYTE = ctypes.c_ubyte
SHORT = ctypes.c_short
DWORD = ctypes.c_ulong
BOOL = ctypes.c_bool
LPWSTR = ctypes.c_wchar_p
UINT = ctypes.c_uint
WCHAR = ctypes.c_wchar


# region Classes
class GAMEPAD(Structure):

    def __init__(self,buttons=0,left_trigger=0,right_trigger=0,left_thumb_x=0,left_thumb_y=0,right_thumb_x=0,right_thumb_y=0):
        self.wButtons = buttons
        self.bLeftTrigger = left_trigger
        self.bRightTrigger = right_trigger
        self.sThumbLX = left_thumb_x
        self.sThumbLY = left_thumb_y
        self.sThumbRX = right_thumb_x
        self.sThumbRY = right_thumb_y
        super().__init__(wButtons=buttons,bLeftTrigger=left_trigger,bRightTrigger=right_trigger,sThumbLX=left_thumb_x,sThumbLY=left_thumb_y,sThumbRX=right_thumb_x,sThumbRY=right_thumb_y)
    _fields_ = [("wButtons", WORD),
                ("bLeftTrigger", BYTE),
                ("bRightTrigger", BYTE),
                ("sThumbLX", SHORT),
                ("sThumbLY", SHORT),
                ("sThumbRX", SHORT),
                ("sThumbRY", SHORT),
                ]



class STATE(Structure):
    def __init__(self,packet_number=0,gamepad=GAMEPAD()):
        self.dwPacketNumber = packet_number
        self.Gamepad = gamepad
        super().__init__(dwPacketNumber=packet_number,Gamepad=gamepad)

    _fields_ = [("dwPacketNumber", DWORD),
                ("Gamepad", GAMEPAD),
                ]


class VIBRATION(Structure):
    def __init__(self, left_motor=0, right_motor=0):
        self.wLeftMotorSpeed = left_motor
        self.wRightMotorSpeed = right_motor
        super().__init__(wLeftMotorSpeed=left_motor, wRightMotorSpeed=right_motor)

    _fields_ = [("wLeftMotorSpeed", WORD),
                ("wRightMotorSpeed", WORD),
                ]


class CAPABILITIES(Structure):
    def __init__(self,type=0,subtype=0,flags=0,gamepad=GAMEPAD(),vibration=VIBRATION()):
        self.Type = type
        self.SubType = subtype
        self.Flags = flags
        self.Gamepad = gamepad
        self.Vibration = vibration
        super().__init__(Type=type,SubType=subtype,Flags=flags,Gamepad=gamepad,Vibration=vibration)


    _fields_ = [("Type", BYTE),
                ("SubType", BYTE),
                ("Flags", WORD),
                ("Gamepad", GAMEPAD),
                ("Vibration", VIBRATION),
                ]


class BATTERY_INFORMATION(Structure):

    def __init__(self, battery_type=0, battery_level=0):
        self.BatteryType = battery_type
        self.BatteryLevel = battery_level
        super().__init__(BatteryType=battery_type,BatteryLevel=battery_level)


    _fields_ = [("BatteryType", BYTE),
                ("BatteryLevel", BYTE),
                ]

class KEYSTROKE(Structure):

    def __init__(self, virtual_key=0, unicode= "o", flags=0, user_id=0, hid_code=0):
        self.VirtualKey = virtual_key
        self.Unicode = unicode
        self.Flags = flags
        self.UserIndex = user_id
        self.HidCode = hid_code
        super().__init__(VirtualKey=virtual_key,Unicode=unicode,Flags=flags,UserIndex=user_id,HidCode=hid_code)


    _fields_ = [("VirtualKey", WORD),
                ("Unicode", WCHAR),
                ("Flags", WORD),
                ("UserIndex", BYTE),
                ("HidCode", BYTE),
                ]

# endregion



def pyX_get_state(dwUserIndex, pState:STATE):
    ret_val = xinput_lib.XInputGetState(dwUserIndex, ctypes.byref(pState))
    return ret_val



def pyX_set_state(dwUserIndex, vibration:VIBRATION):
    return xinput_lib.XInputSetState(dwUserIndex, ctypes.byref(vibration))



def pyX_get_capabilities(dwUserIndex, dwFlags, pCapabilities):
    return xinput_lib.XInputGetCapabilities(dwUserIndex,dwFlags,ctypes.byref(pCapabilities))


def pyX_input_enable(enable):
    return xinput_lib.XInputEnable(enable)




def pyX_get_Audio_Device_Ids(dwUserIndex,pRenderDeviceId = None,pRenderCount = None,pCaptureDeviceId = None,pCaptureCount = None):
    return xinput_lib.XInputGetAudioDeviceIds(dwUserIndex,ctypes.byref(pRenderDeviceId),ctypes.byref(pRenderCount),ctypes.byref(pCaptureDeviceId),ctypes.byref(pCaptureCount))



def pyX_get_battery_info(dwUserIndex, devType, batteryInformation):
    return xinput_lib.XInputGetBatteryInformation(dwUserIndex, devType, ctypes.byref(batteryInformation))



def pyX_get_keystroke(dwUserIndex, pKeystroke, dwReserved=1):
    return xinput_lib.XInputGetKeystroke(dwUserIndex,dwReserved, ctypes.byref(pKeystroke))

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

