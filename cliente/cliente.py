import socket

def start_client():
    # Configuração do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Digite a mensagem (ou 'sair' para encerrar): ")
        client_socket.send(message.encode())
        
        if message.lower() == 'sair':
            break

        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()