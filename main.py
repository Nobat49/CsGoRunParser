from time import sleep
import requests

f = 1
crashes = []

for i in range(300000,2212514):
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
		bets = json['data']['bets']
		total_bet = 0.0

		for i in bets:
			bet = i['deposit']['amount']
			total_bet = total_bet + bet

		print(f'''
			Id = {g_id}
			Crash = {crash}
			Total bet = {total_bet}
			---------------------------
		''')

		crashes.append([g_id,crash,total_bet])

		f = f + 1
		sleep(0.3)
	except:
		print(f'''
			Id = {i}
			Crash = Error
			''')
		continue

with open('crashes.txt', 'a+') as file:
	for txt in crashes:
		file.write(str(txt) + '\n')
	file.close()

