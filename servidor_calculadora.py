
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('', 12000))
print("Servidor ligado")

while True:
    
    mensagem_bytes, mensagem_ip = servidor.recvfrom(2048)
    mensagem_decode = mensagem_bytes.decode()

    equacao = mensagem_decode.split(" ")

    if equacao[1] == "+":
        resultado = float(equacao[0]) + float(equacao[2])
    elif equacao[1] == "-":
        resultado = float(equacao[0]) - float(equacao[2])
    elif equacao[1] == "/":
        resultado = float(equacao[0]) / float(equacao[2])
    elif equacao[1] == "*" or equacao[1] == "x":
        resultado = float(equacao[0]) * float(equacao[2])
    else:
        resultado = "Operador não conhecido"
    
    servidor.sendto(str(resultado).encode(), mensagem_ip)

    print("resposta calculada:", equacao[0], equacao[1], equacao[2], "=", resultado)

