

#include "pch.h"
#include "TestX.h"
#include <stdio.h>
#include <stdlib.h>

DWORD XInputGetState(_In_ DWORD dwUserIndex, _Out_ XINPUT_STATE* pState)
{
	pState->dwPacketNumber = 10;
	pState->Gamepad.wButtons = 10;
	pState->Gamepad.bLeftTrigger = 10;
	pState->Gamepad.bRightTrigger = 10;
	pState->Gamepad.sThumbLX = 10;
	pState->Gamepad.sThumbLY = 10;
	pState->Gamepad.sThumbRX = 10;
	pState->Gamepad.sThumbRY = 10;
	return dwUserIndex;
}

DWORD XInputSetState(_In_ DWORD dwUserIndex, _In_ XINPUT_VIBRATION* pVibration)
{
	pVibration->wLeftMotorSpeed = 10;
	pVibration->wRightMotorSpeed = 10;
	return 1;
}

DWORD XInputGetCapabilities(_In_ DWORD dwUserIndex, _In_ DWORD dwFlags, _Out_ XINPUT_CAPABILITIES* pCapabilities)
{
	pCapabilities->Type = 10;
	pCapabilities->SubType = 10;
	pCapabilities->Flags = 10;
	pCapabilities->Gamepad.wButtons = 10;
	pCapabilities->Gamepad.bLeftTrigger = 10;
	pCapabilities->Gamepad.bRightTrigger = 10;
	pCapabilities->Gamepad.sThumbLX = 10;
	pCapabilities->Gamepad.sThumbLY = 10;
	pCapabilities->Gamepad.sThumbRX = 10;
	pCapabilities->Gamepad.sThumbRY = 10;
	pCapabilities->Vibration.wLeftMotorSpeed = 10;
	pCapabilities->Vibration.wRightMotorSpeed = 10;
	return dwUserIndex + dwFlags;
}
BOOL XInputEnable(_In_ BOOL enable)
{
	return enable;
}

DWORD XInputGetAudioDeviceIds(_In_ DWORD dwUserIndex, _Out_writes_opt_(*pRenderCount) LPWSTR pRenderDeviceId, _Inout_opt_ UINT* pRenderCount, _Out_writes_opt_(*pCaptureCount) LPWSTR pCaptureDeviceId, _Inout_opt_ UINT* pCaptureCount)
{
	//LPWSTR* str = (LPWSTR*)L"Test";
	if (pRenderDeviceId)
	{
		*pRenderDeviceId = (WCHAR)'F';
	}

	if (pRenderCount)
	{
		*pRenderCount = 10;
	}
	if (pCaptureDeviceId)
	{
		*pCaptureDeviceId = (WCHAR)'F';
	}

	if (pCaptureCount)
	{
		*pCaptureCount = 10;
	}
	
	return dwUserIndex;
}

DWORD XInputGetBatteryInformation(_In_ DWORD dwUserIndex, _In_ BYTE devType, _Out_ XINPUT_BATTERY_INFORMATION* pBatteryInformation)
{
	pBatteryInformation->BatteryLevel = 10;
	pBatteryInformation->BatteryType = 10;
	return dwUserIndex + devType;
}

DWORD XInputGetKeystroke(_In_ DWORD dwUserIndex, _Reserved_ DWORD dwReserved, _Out_ PXINPUT_KEYSTROKE pKeystroke)
{
	pKeystroke->VirtualKey = 10;
	pKeystroke->Unicode = (WCHAR)'F';
	pKeystroke->Flags = 10;
	pKeystroke->UserIndex = 10;
	pKeystroke->HidCode = 10;
	return dwUserIndex;
}

DWORD XInputGetDSoundAudioDeviceGuids(_In_ DWORD dwUserIndex, _Out_ GUID* pDSoundRenderGuid, _Out_ GUID* pDSoundCaptureGuid)
{
	pDSoundRenderGuid->Data1 = 10;
	pDSoundCaptureGuid->Data1 = 50;
	printf("end %lu \n", dwUserIndex);
	return dwUserIndex;
}
