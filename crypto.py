import requests
import inquirer

print('''
	----------------------------
	Latest cryptocurrency prices
	----------------------------
''')

crypto_prompt = [
	inquirer.List(
		'crypto',
		message = 'Choose a cryptocurrency',
		choices = ['Bitcoin', 'Ethereum', 'XRP', 'Tether', 'Litecoin', 'Monero', 'Stellar']
	)
]

crypto_choice = inquirer.prompt(crypto_prompt)['crypto']

crypto_api = f'https://api.coinmarketcap.com/v1/ticker/{crypto_choice}'
response = requests.get(crypto_api)
response_list = response.json()

current_price = float(response_list[0]['price_usd'])

def crypto_price_change():
	percent_change = float(response_list[0]['percent_change_24h'])
	previous_price = current_price/(percent_change/100 + 1)
	return previous_price
previous_price = crypto_price_change()

def find_price_direction():
	if current_price > previous_price:
		return 'up'
	elif current_price < previous_price:
		return'down'
	else:
		return 'same'

print(f'{crypto_choice} is currently ${round(current_price, 2)} USD, {find_price_direction()} from ${round(previous_price, 2)} yesterday')