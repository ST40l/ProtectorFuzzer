import socket

# Hedef IP adresi ve port numarası
target_ip = "127.0.0.1"
target_port = 12345

# Fuzzer'ın üreteceği rastgele girdi boyutu aralığı
min_input_size = 10
max_input_size = 100

# Fuzzer'ın çalışma sayısı
num_tests = 100

def generate_random_input(size):
    # Rastgele bir girdi üret
    return b"A" * size

def main():
    for _ in range(num_tests):
        # Rastgele bir girdi boyutu üret
        input_size = random.randint(min_input_size, max_input_size)
        
        # Rastgele bir girdi üret
        input_data = generate_random_input(input_size)
        
        # TCP bağlantısı oluştur
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        
        try:
            # Girdiyi hedefe gönder
            client_socket.send(input_data)
            
            # Hedeften gelen cevabı al
            response = client_socket.recv(1024)
            
            # Cevabı incele
            # Burada hedef sistemden gelen cevabı analiz edebilirsiniz
        except Exception as e:
            print("Hata:", e)
        finally:
            # Bağlantıyı kapat
            client_socket.close()

if __name__ == "__main__":
    main()
