

import socket

class SocketManager:

    def __init__(self, addres):
        self.addres = addres

    def __enter__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.addres)
        self.sock.listen(1)
        return self.sock

    def __exit__(self, *ignore):
        self.sock.close()


with SocketManager(('0.0.0.0', 2222)) as sock:
    # sock.listen(1)
    while True:
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            print(data)
            if not data or 'close' in data.encode('utf-8'):
                break

            conn.sendall(data)


