INPUT_DEVSUBTYPE_UNKNOWN = 0x00
INPUT_DEVSUBTYPE_WHEEL = 0x02
INPUT_DEVSUBTYPE_ARCADE_STICK = 0x03
INPUT_DEVSUBTYPE_FLIGHT_STICK = 0x04
INPUT_DEVSUBTYPE_DANCE_PAD = 0x05
INPUT_DEVSUBTYPE_GUITAR = 0x06
INPUT_DEVSUBTYPE_GUITAR_ALTERNATE = 0x07
INPUT_DEVSUBTYPE_DRUM_KIT = 0x08
INPUT_DEVSUBTYPE_GUITAR_BASS = 0x0B
INPUT_DEVSUBTYPE_ARCADE_PAD = 0x13

DEVSUBTYPE_GAMEPAD = 0x01
DEVTYPE_GAMEPAD = 0x01
CAPS_VOICE_SUPPORTED = 0x0004

CAPS_FFB_SUPPORTED = 0x0001
CAPS_WIRELESS = 0x0002
CAPS_PMD_SUPPORTED = 0x0008
CAPS_NO_NAVIGATION = 0x0010

# Gamepad Buttons

GAMEPAD_DPAD_UP = 0x0001
GAMEPAD_DPAD_DOWN = 0x0002
GAMEPAD_DPAD_LEFT = 0x0004
GAMEPAD_DPAD_RIGHT = 0x0008
GAMEPAD_START = 0x0010
GAMEPAD_BACK = 0x0020
GAMEPAD_LEFT_THUMB = 0x0040
GAMEPAD_RIGHT_THUMB = 0x0080
GAMEPAD_LEFT_SHOULDER = 0x0100
GAMEPAD_RIGHT_SHOULDER = 0x0200
GAMEPAD_A = 0x1000
GAMEPAD_B = 0x2000
GAMEPAD_X = 0x4000
GAMEPAD_Y = 0x8000

# Gamepad thresholds
GAMEPAD_LEFT_THUMB_DEADZONE = 7849
GAMEPAD_RIGHT_THUMB_DEADZONE = 8689
GAMEPAD_TRIGGER_THRESHOLD = 30


# Battery
BATTERY_DEVTYPE_GAMEPAD = 0x00
BATTERY_DEVTYPE_HEADSET = 0x01

BATTERY_TYPE_DISCONNECTED = 0x00  # This device is not connected
BATTERY_TYPE_WIRED = 0x01  # Wired device, no battery
BATTERY_TYPE_ALKALINE = 0x02  # Alkaline battery source
BATTERY_TYPE_NIMH = 0x03  # Nickel Metal Hydride battery source
BATTERY_TYPE_UNKNOWN = 0xFF  # Cannot determine the battery type

BATTERY_LEVEL_EMPTY = 0x00
BATTERY_LEVEL_LOW = 0x01
BATTERY_LEVEL_MEDIUM = 0x02
BATTERY_LEVEL_FULL = 0x03

# Codes returned for the gamepad keystroke
VK_PAD_A = 0x5800
VK_PAD_B = 0x5801
VK_PAD_X = 0x5802
VK_PAD_Y = 0x5803
VK_PAD_RSHOULDER = 0x5804
VK_PAD_LSHOULDER = 0x5805
VK_PAD_LTRIGGER = 0x5806
VK_PAD_RTRIGGER = 0x5807

VK_PAD_DPAD_UP = 0x5810
VK_PAD_DPAD_DOWN = 0x5811
VK_PAD_DPAD_LEFT = 0x5812
VK_PAD_DPAD_RIGHT = 0x5813
VK_PAD_START = 0x5814
VK_PAD_BACK = 0x5815
VK_PAD_LTHUMB_PRESS = 0x5816
VK_PAD_RTHUMB_PRESS = 0x5817

VK_PAD_LTHUMB_UP = 0x5820
VK_PAD_LTHUMB_DOWN = 0x5821
VK_PAD_LTHUMB_RIGHT = 0x5822
VK_PAD_LTHUMB_LEFT = 0x5823
VK_PAD_LTHUMB_UPLEFT = 0x5824
VK_PAD_LTHUMB_UPRIGHT = 0x5825
VK_PAD_LTHUMB_DOWNRIGHT = 0x5826
VK_PAD_LTHUMB_DOWNLEFT = 0x5827

VK_PAD_RTHUMB_UP = 0x5830
VK_PAD_RTHUMB_DOWN = 0x5831
VK_PAD_RTHUMB_RIGHT = 0x5832
VK_PAD_RTHUMB_LEFT = 0x5833
VK_PAD_RTHUMB_UPLEFT = 0x5834
VK_PAD_RTHUMB_UPRIGHT = 0x5835
VK_PAD_RTHUMB_DOWNRIGHT = 0x5836
VK_PAD_RTHUMB_DOWNLEFT = 0x5837

# Flags used in XINPUT_KEYSTROKE

KEYSTROKE_KEYDOWN = 0x0001
KEYSTROKE_KEYUP = 0x0002
KEYSTROKE_REPEAT = 0x0004
