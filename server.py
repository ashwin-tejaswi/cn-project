"""
---------
TCP Server program that:
- waits for a client connection
- receives a filename requested by the client
- reads the file (if it exists)
- sends the file content back to the client
"""

import socket
import os

HOST = "127.0.0.1"   # localhost
PORT = 5001          # any free port


def handle_client(conn, addr):
    print(f"[+] Connected to {addr}")

    # Step 1: Receive filename from client
    filename = conn.recv(1024).decode().strip()
    print(f"[SERVER] Client requested file: {filename}")

    if not filename:
        conn.sendall(b"Error: No filename received.")
        conn.close()
        return

    # Step 2: Check if file exists
    if not os.path.exists(filename):
        conn.sendall(b"Error: File not found on server.")
        conn.close()
        return

    # Step 3: Read file content
    try:
        with open(filename, "r") as f:
            data = f.read()
        conn.sendall(data.encode())
    except Exception as e:
        conn.sendall(f"Error reading file: {str(e)}".encode())

    conn.close()
    print(f"[+] Connection with {addr} closed.")


def main():
    print(f"[*] Starting Server on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print("[*] Server is waiting for client connection...")

        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)


if __name__ == "__main__":
    main()
