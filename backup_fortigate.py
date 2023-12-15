#! /usr/local/Python_envs/Python3/bin/python3
from datetime import date, datetime
from netmiko import Netmiko

# Define o nome do arquivo de backup
filename = 'backup.bkp'
data_atual = date.today()

fw_01 = {'host': '192.168.0.1',
		 'username':'admin',
		 'password':'Password',
		 'device_type': 'fortinet'
	}
print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
print(f"{'#'*20} Connected {'#'*20}")

# print(net_connect.find_prompt())
# command = 'show full-configuration'
# full_config = net_connect.send_command(command)
# print(full_config)

# Comando para exibir as configurações completas do fortigate
config = ['show full-configuration']
send_config = net_connect.send_config_set(config)

# print(send_config)

# Abre o arquivo backup.txt e escreve o backup
log_file = open(filename, 'a')
log_file.write('### ARQUIVO BACKUP GERADO EM ' + str(data_atual) + '\n')
log_file.write(send_config)
log_file.write('\n')
