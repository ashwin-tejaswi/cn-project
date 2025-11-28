"""
-------
TCP Client program that:
- connects to the server
- sends a filename
- receives file content or error message
"""

import socket

HOST = "127.0.0.1"
PORT = 5001


def main():
    print("TCP File Request Client")

    # Ask user for filename
    filename = input("Enter filename to request from server: ").strip()

    if filename == "":
        print("Filename cannot be empty.")
        return

    # Connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
        except Exception as e:
            print("Error connecting to server:", e)
            return

        # Step 1: Send filename
        client.sendall(filename.encode())

        # Step 2: Receive response
        data = client.recv(4096)
        print("\n----- Server Response -----")
        print(data.decode())
        print("---------------------------")


if __name__ == "__main__":
    main()
