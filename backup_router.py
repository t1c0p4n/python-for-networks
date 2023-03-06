import netmiko, getpass

# Pergunta IP, usuário e senha do roteador
ip = input('Device IP: ')
user = input('Username: ')
pw = getpass.getpass()
secret = getpass.getpass(prompt='Secret: ')

# Abaixo é feita uma conexão telnet. Se for SSH, basta trocar o device_type para cisco_ios
cisco_ios = {
    'device_type': 'cisco_ios_telnet',
    'ip': ip,
    'username': user,
    'password': pw,
    'secret': secret,
}

# Conecta ao roteador usando o ConnectHandler do netmiko
net_connect = netmiko.ConnectHandler(**cisco_ios)
prompt = net_connect.find_prompt()

# Cria o arquivo backup.txt para salvar as configurações
filename = backup.txt

# Executa o comando 'enable' no terminal do roteador
net_connect.enable()

# Executa o comando 'show run' no roteador
showrun = net_connect.send_command('show run')

# Executa o comando 'show ver' no roteador
showver = net_connect.send_command('show ver')

# Abre o arquivo backup.txt e escreve o backup
log_file = open(filename, 'a')
log_file.write(showrun)
log_file.write('\n')
log_file.write(showver)
log_file.write('\n')

# Sai do enable do roteador
net_connect.exit_enable_mode()

# Desconecta do roteador
net_connect.disconnect()