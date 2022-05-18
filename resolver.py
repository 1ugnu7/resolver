#!/usr/bin/python

import socket

class colors:

	WARNING = '\033[91m'
	SUCCESS = '\033[92m'
	ENDC = '\033[0m'

with open(r'hosts.txt', 'r') as host_file:
	with open(r'ips.csv', 'w') as ip_file:
		with open(r'error.log', 'w') as error_file:
			for hostname in host_file.readlines():
				hostname = hostname.strip()
				try:
					print(colors.SUCCESS + '[+]'+''+'Resolving : ' + hostname + colors.ENDC)
					ip = socket.gethostbyname(hostname)
					ip_file.write(hostname + ',' + ip + '\n')
				except:
					print(colors.WARNING + '[!]'+''+'Can not resolve ' + hostname + colors.ENDC)
					error_file.write(hostname + '--' + 'Could Not Resolve' + '\n')
