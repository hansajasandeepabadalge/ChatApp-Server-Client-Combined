import socket
import sys
import threading

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(1)
    print("Server listening on port 9999...")

    client, address = server_socket.accept()
    print("Connection from", address)

    done = False
    while not done:
        msg = client.recv(1024).decode('utf-8')
        print("Client:", msg)
        if msg.lower() == "quit":
            done = True
        else:
            reply = input("Server Message: ")
            client.send(reply.encode('utf-8'))

    print("Server shutting down.")
    client.close()
    server_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))

    done = False
    while not done:
        message = input("Client Message: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == "quit":
            done = True
        else:
            reply = client_socket.recv(1024).decode('utf-8')
            print("Server:", reply)

    print("Client shutting down.")
    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py server|client")
    else:
        if sys.argv[1].lower() == "server":
            start_server()
        elif sys.argv[1].lower() == "client":
            start_client()
        else:
            print("Invalid argument. Use 'server' or 'client'.")
