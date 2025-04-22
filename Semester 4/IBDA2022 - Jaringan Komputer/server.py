import socket
import threading

# Inisialisasi socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5050))  # Dengarkan di semua IP pada port 5050
server_socket.listen(5)

# Simpan daftar klien yang terhubung
clients = {}  # Format: {username: socket}

def handle_client(client_socket, username):
    """Fungsi untuk menangani komunikasi dari setiap klien."""
    while True:
        try:
            pesan = client_socket.recv(1024).decode()
            if not pesan:
                break

            # Format pesan: target_username:isi_pesan
            if ":" in pesan:
                # split pesan untuk mencari tau nama penerima pesan
                target_username, message = pesan.split(":", 1) # 1 = pemisahan hanya satu kali, menjadi 2 bagian saja (untuk mengatasi pesan yang ada :)

                if target_username in clients: # jika penerima pesan tersedia
                    clients[target_username].sendall(f"{username}: {message}".encode()) # maka pesan dikirimkan
                else: # jika penerima pesan tidak tersedia, maka pesan ini akan dikirimkan
                    client_socket.sendall("User tidak ditemukan!".encode())

        except (ConnectionResetError, BrokenPipeError) # untuk mengatasi error tertentu
            break

    print(f"{username} terputus.")
    del clients[username]
    client_socket.close()

print("Server berjalan dan menunggu koneksi...")

while True:
    client_socket, client_address = server_socket.accept() # menerima info client yang terhubung ke server
    print(f"Koneksi baru dari {client_address}")

    # Terima username dari client
    username = client_socket.recv(1024).decode() # untuk mendapatkan username dari akun yang login
    if username in clients: # kalau username sudah dipakai
        client_socket.sendall("Username sudah digunakan!".encode())
        client_socket.close()
    else: # kalau tidak ada username yang login
        clients[username] = client_socket
        client_socket.sendall("Terhubung ke chatroom!".encode()) # mengirimkan pesan ke client

        # Buat thread baru untuk menangani klien
        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()
