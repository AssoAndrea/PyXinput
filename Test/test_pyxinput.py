import ctypes
import sys
sys.path.insert(0,"../PyXinput_Source")
from PyXinputCode.PyXinput_Source import PyXinput as pyX
import pytest


def setup_module():
    pytest.lib = pyX.load_DLL(is_test=True)
    pytest.num = 10
    if not pytest.lib:
        raise IOError("lib not found")



def test_GetState():

    state = pyX.STATE()
    ret_val = pyX.pyX_get_state(1,state)
    assert ret_val == 1
    assert state.dwPacketNumber == 10
    assert state.Gamepad.wButtons == 10
    assert state.Gamepad.bLeftTrigger == 10
    assert state.Gamepad.bRightTrigger == 10
    assert state.Gamepad.sThumbLX == 10
    assert state.Gamepad.sThumbLY == 10
    assert state.Gamepad.sThumbRX == 10
    assert state.Gamepad.sThumbRY == 10

def test_SetState():
    vibration = pyX.VIBRATION(left_motor=2,right_motor=2)
    ret_val = pyX.pyX_set_state(1,vibration)
    assert ret_val == 1
    assert vibration.wLeftMotorSpeed == 10
    assert vibration.wRightMotorSpeed == 10

def test_get_capabilities():
    capabilities = pyX.CAPABILITIES()
    ret_val = pyX.pyX_get_capabilities(1,10,capabilities)
    assert ret_val == 1 + 10
    assert capabilities.Type == 10
    assert capabilities.SubType == 10
    assert capabilities.Flags == 10
    assert capabilities.Gamepad.wButtons == 10
    assert capabilities.Gamepad.bLeftTrigger == 10
    assert capabilities.Gamepad.bRightTrigger == 10
    assert capabilities.Gamepad.sThumbLX == 10
    assert capabilities.Gamepad.sThumbLY == 10
    assert capabilities.Gamepad.sThumbRX == 10
    assert capabilities.Gamepad.sThumbRY == 10
    assert capabilities.Vibration.wLeftMotorSpeed == 10
    assert capabilities.Vibration.wRightMotorSpeed == 10
    assert ret_val == 1 + 10

def test_input_enable():
    ret_val = pyX.pyX_input_enable(True)
    assert ret_val == True
    ret_val = pyX.pyX_input_enable(False)
    assert ret_val == False

def test_get_audio_devide_ids():
    render_device_id = ctypes.c_wchar('v')
    render_count = pyX.UINT(0)
    capture_device_id =  ctypes.c_wchar('v')
    capture_count = pyX.UINT(0)
    ret_val = pyX.pyX_get_Audio_Device_Ids(5,render_device_id,render_count,capture_device_id,capture_count)
    assert ret_val == 5
    assert render_count.value == 10
    assert capture_count.value == 10
    assert render_device_id.value == 'F'
    assert capture_device_id.value == 'F'

def test_get_battery_info():
    battery_info = pyX.BATTERY_INFORMATION()
    ret_val = pyX.pyX_get_battery_info(1,2,battery_info)
    assert ret_val == 3 # 1 + 2
    assert battery_info.BatteryLevel == 10
    assert battery_info.BatteryType == 10

def test_get_keystroke():
    keystroke = pyX.KEYSTROKE()
    ret_val = pyX.pyX_get_keystroke(1,keystroke)
    assert ret_val == 1
    assert keystroke.VirtualKey == 10
    assert keystroke.Flags == 10
    assert keystroke.HidCode == 10
    assert keystroke.UserIndex == 10
    assert keystroke.Unicode == 'F'


