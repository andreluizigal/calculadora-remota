
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Bem-vindo à Calculadora remota!\n")

while True:
    mensagem_envio = input("Digite a operação separada por espaço: ")
    cliente.sendto(mensagem_envio.encode(), ('localhost', 12000))
    mensagem_bytes, ip_servidor = cliente.recvfrom(2048)
    print("Resposta: ", mensagem_bytes.decode(), "\n")