import socket
import os
import hashlib
import sys

host = socket.gethostbyname('ipc_server_dns_name')
port = int(os.environ.get('PORT', 9000))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
filePath="/clientdata/file.txt"

def main():
    s.connect((host, port))
    print("Connected to server")
    app()

def app():
    print("Receiving...")
    with open(filePath, "wb") as f:
        data = s.recv(1024)    
        f.write(data)
        f.close()
    print("Received")

    print("Receiving checksum...")
    checksum = s.recv(1024)
    print("Received")

    print("Verifying checksum...")
    with open(filePath, "rb") as f:
        checksum2 = 0
        for byte in f.read():
            checksum2 += byte


        checksum2 = str(checksum2).encode()
        print("Checksum: " + str(checksum))
        print("Checksum2: " + str(checksum2))
        if checksum == checksum2:
            print("Verified")
        else:
            print("Checksum mismatch")
    
    s.close()
    print("Connection closed")

if __name__ == "__main__":
    main()

