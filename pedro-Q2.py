import ipaddress

entrada = input('Digite um endereco ip ou numero inteiro: ')

if '.' in entrada:
    ip_inteiro = int(ipaddress.ip_address(entrada))
    print("Ip inteiro =",ip_inteiro)

else:
    ip_inteiro = int(entrada)
    ip_str = str(ipaddress.ip_address(int(entrada)))
    ip_str = str(ipaddress.ip_address(ip_inteiro))
    print("Ip =",ip_str)
