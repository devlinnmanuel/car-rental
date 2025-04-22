import socket
import threading

# input ip dan username
server_ip = input("Masukkan IP server: ")
username = input("Masukkan nama pengguna: ")

# memulai koneksi client ke server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, 5050))
client_socket.sendall(username.encode())

# Terima pesan pertama dari server (konfirmasi koneksi)
response = client_socket.recv(1024).decode()
if response == "Username sudah digunakan!":
    print("Gagal terhubung: Username sudah dipakai.")
    client_socket.close()
    exit()
else:
    print(response)

def receive_messages():
    """Fungsi untuk menerima pesan dari server."""
    while True:
        try:
            pesan = client_socket.recv(1024).decode()
            if not pesan:
                break
            print(f"\n{pesan}")

        except (ConnectionResetError, BrokenPipeError):
            break

# Jalankan thread untuk menerima pesan
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

while True:
    target = input("Kirim ke: ")
    message = input("Pesan: ")

    if message.lower() == "exit":
        break

    full_message = f"{target}:{message}"
    client_socket.sendall(full_message.encode()) # sendall = mengirim data melalui socket

client_socket.close()
