import PyXConstants
import PyXinput


if __name__ == '__main__':
    PyXinput.load_DLL()
    state = PyXinput.STATE()
    state.dwPacketNumber = 10
    print(state.dwPacketNumber)


    # state = PyXinput.STATE()
    #
    # PyXinput.set_motor_speed(0, 0.1, 0.5)
    # PyXinput.set_deadzone(PyXConstants.GAMEPAD_LEFT_THUMB_DEADZONE, 50)
    #
    # while True:
    #     PyXinput.pyX_get_state(0, state)
    #     print(state.Gamepad.wButtons)