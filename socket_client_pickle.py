import socket
from io import BytesIO
import pickle


def client_pic(ip, port, obj):
    try:
        msg = pickle.dumps(obj)  # 编码
        send_message = BytesIO(msg)
        send_message_from = send_message.read(1024)
    except:
        send_message = obj
        send_message_from = send_message.read(1024)

    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.connect((ip, port))
    while send_message_from:
        socket_obj.send(send_message_from)
        send_message_from = send_message.read(1024)

    socket_obj.close()


if __name__ == "__main__":
    dict_data = {
        'key_1': 'welcome!',
        'key_2': [
            1, 2, 3, 4, 5
        ]
    }
    client_pic('192.168.0.110', 6666, dict_data)
