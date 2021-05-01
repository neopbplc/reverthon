import hashlib
from datetime import datetime
import threading

banner = """
 ____                    _____ _                 
|  _ \ _____   _____ _ _|_   _| |__   ___  _ __  
| |_) / _ \ \ / / _ \ '__|| | | '_ \ / _ \| '_ \ 
|  _ <  __/\ V /  __/ |   | | | | | | (_) | | | |
|_| \_\___| \_/ \___|_|   |_| |_| |_|\___/|_| |_|
                                                 
v1.0

Telegram: @neopbplc
"""

print(banner)

#Variables
count = 0
wordlist = open("dic.txt",encoding='utf8',errors='replace')
algorithms_available = ['md4', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
total_algorithms = len(algorithms_available)

print(f'Seleccione un algoritmo. Hay {total_algorithms} algoritmos disponibles. ')

for element in algorithms_available:
	print('> '+element)

while True:
	algorithm = input('[?] Escriba el nombre del algoritmo: ').lower()
	try: 
		algorithms_available.index(algorithm)
		break
	except:
		print('[!] El algoritmo no existe!')

hash_input = input('[?] Escriba el HASH a revertir: ').lower()

print('++DATOS INGRESADOS+++++++++++++++++++++++++')
print(f'Algoritmo: {algorithm}')
print(f'Hash: {hash_input}')
print('+++++++++++++++++++++++++++++++++++++++++++')

print('[...] Por favor espere, estamos buscando coincidencias.')

def dehash(password):
	password_hash = hashlib.new(algorithm)
	password_hash.update(password.encode())
	password_hash = password_hash.hexdigest()

	if password_hash == hash_input:
		print('******* ¡PASSWORD FOUND! *******')
		print('¡Encontramos coincidencias!')
		print(f'=> Password: {password}')
		print(f'=> Hash: {password_hash}')
		print(f'=> Algoritmo: {algorithm}')
		print(f'=> Intentos fallidos totales: {count}')
		print(f'=> Intentos totales: {count + 1}')
		print(f'=> Hora actual: {datetime.now()}')
		print('******* ******* ******* *******')
		exit()

for password in wordlist:
	count += 1

	password = password.replace("\n", "")
	dehash(password)
