import socket
import json
import time
import random

# Server setup
HOST = '127.0.0.1'
PORT = 5555

def generate_17x3_array():
    return [[random.uniform(0, 1) for _ in range(3)] for _ in range(17)]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = generate_17x3_array()
            
            # Send JSON data with a newline delimiter
            conn.sendall((str(data) + "\n").encode('utf-8'))
            print("Sent:", data)
            
            time.sleep(1)  # Adjust update rate as needed