from time import sleep
from ftplib import FTP
import requests

f = 1
crashes = []

for i in range(1005840,1750000):
	if f == 100:
		with open('crashes.txt', 'a+') as file:
			for txt in crashes:
				file.write(str(txt) + '\n')
			file.close()
		crashes = []
		f = 1
	try:
		json = requests.get(f'https://api.csgorun.pro/games/{i}').json()
		g_id = json['data']['id']
		crash = json['data']['crash']
		print(f'''
			Id = {g_id}
			Crash = {crash}
			---------------------------
		''')
		crashes.append([g_id,crash])
		f = f + 1
		sleep(0.3)
	except:
		print(f'''
			Id = {i}
			Crash = Error
			''')
		continue

with open('crashes1.txt', 'a+') as file:
	for txt in crashes:
		file.write(str(txt) + '\n')
	file.close()

sleep(30)

ftp = FTP('files.000webhost.com', 'herfiles', '2283320704')
with open('crashes.txt', 'rb') as f:
	ftp.storlines('STOR crashes.txt', f)
	f.close()
print('Upload succes')
