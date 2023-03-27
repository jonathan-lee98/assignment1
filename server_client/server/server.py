import socket
import os
import hashlib
import sys
import string
import random

host = socket.gethostbyname('ipc_server_dns_name')
port = int(os.environ.get('PORT', 9000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
filePath = "/serverdata/file.txt"

def text_generator(size=1024, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)).encode()

def main():
    print("Creating file...")
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    with open(filePath, "wb") as f:
        random_data = text_generator()
        f.write(random_data)
        f.close()
    print("Server started")
    app()

def app():
    print("Starting server...")
    s.bind((host, port))
    s.listen()
    print("Waiting for connection...")
    sc, address = s.accept()
    print("Connection from: " + str(address))

    print("Sending...")
    with open(filePath, "rb") as f:
        data = f.read(1024)
        sc.send(data)
        f.close()
    print("Sent")

    print("Sending checksum...")
    with open(filePath, "rb") as f:
        checksum = 0
        for byte in f.read():
            checksum += byte

        checksum = str(checksum).encode()
        sc.send(checksum)

    print("Sent")

    sc.close()
    print("Connection closed")


if __name__ == "__main__":
    main()