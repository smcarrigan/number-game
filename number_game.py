# Number Guessing Game
# Created by: Shaun Carrigan
# Created date: Sept 2, 2015
# Last modified date: Sept 6, 2015

import random
import json
import os

# Constants
MIN_DIFFERENCE = 3
MIN_LIST = 3
STARTING_NUM_OF_LIVES = 7
WINNINGS_NUM_OF_LIVES = 7
WINNING_TOTAL = 1000000
STARTING_MONEY = 100
COST_TO_PURCHASE_LIFE = 10

player = { 
	'total_lives' : STARTING_NUM_OF_LIVES,
	'total_money' : STARTING_MONEY
	}

def check_value(guess, correct_value):
	if guess == correct_value:
		return True
	else:
		return False

def get_input():
	min_random_value = 0
	max_random_value = 0
	num_of_list_values = 0

	while((max_random_value - min_random_value) < MIN_DIFFERENCE):
		print("Range needs to be greater than " + str(MIN_DIFFERENCE) + ".")
		min_random_value = int(input("Minimum random value: "))
		max_random_value = int(input("Maximum random value: "))
	
	while(num_of_list_values < MIN_LIST):
		print("Number of list values needs to be greater than or equal to " + str(MIN_LIST) + ".")
		num_of_list_values = int(input("Number of values in list: "))

	while(num_of_list_values > player['total_lives']):
		print("Number of list values needs to be less than total lives.")
		num_of_list_values = int(input("Number of values in list: "))
	#while(num_of_lives < num_of_list_values):
	#	print("Number of lives needs to be greater or equal to number of list values.")
	#	num_of_tries = int(input("Number of tries: "))

	return {'min_random_value': min_random_value,
		'max_random_value': max_random_value,
		'num_of_list_values': num_of_list_values
		}

def calculate_inputs(input_dict):
	difference = input_dict['max_random_value'] - input_dict['min_random_value']

def create_list(input_dict):
	return [random.randint(input_dict['min_random_value'],input_dict['max_random_value'])
		       for x in range(1,input_dict['num_of_list_values']+1)]

def game(random_list, input_dict):
	index = 0
	num_of_lives = player['total_lives']
	min_value = str(input_dict['min_random_value'])
	max_value = str(input_dict['max_random_value'])
	difference = int(max_value) - int(min_value)

	active_list = ['x' for x in range(0,len(random_list))]
	while(True):
		print(active_list)
		print("Number of lives left: %d" % num_of_lives)

		try:
			input_value = int(input("Enter guess between " + min_value + " and " + max_value + ": "))
			if input_value < int(min_value) or input_value > int(max_value):
				raise ValueError

		except ValueError:
			print("Invalid input.  Integer value must be between " + min_value + " and " + max_value + ".")
		else:
			if check_value(input_value, random_list[index]):
				active_list[index] = input_value
				index += 1
				if index == len(random_list):
					print(active_list)
					player['total_lives'] = num_of_lives
					player['total_lives'] += WINNINGS_NUM_OF_LIVES

					winnings = difference * len(active_list)
					player['total_money'] += winnings
					print("You won $" + str(winnings))
					if player['total_money'] >= WINNING_TOTAL:
						print("CONGRATULATIONS!  YOU MADE OVER " + str(WINNING_TOTAL))
					return True
			else:
				num_of_lives -= 1
				if num_of_lives == 0:
					print("You ran out of lives!")
					losses = difference * len(active_list)
					player['total_money'] -= losses
					player['total_lives'] = STARTING_NUM_OF_LIVES
					print("You lost $" + str(losses))
					if player['total_money'] <= 0:
						return False
					else:
						return True

				if input_value < random_list[index]:
					print ("Guess higher")
				elif input_value > random_list[index]:
					print ("Guess lower")

def print_stats():
	print("+++++++++++++++++++")
	print("Total amount of money: $%d" % player['total_money'])
	print("Total number of lives: %d" % player['total_lives'])
	print("You currently have $%d of $%d." % (player['total_money'],WINNING_TOTAL))
	print("Progress: %.1f%%" % ((player['total_money'] / WINNING_TOTAL)*100))

def main_menu():
	print("-------------------")
	print("1) Start Game")
	print("2) Save Game")
	print("3) Load Saved Game")
	print("4) Exit")
	
	return input("Enter: ")

def game_menu():
	print("-------------------")
	print("1) New Match")
	print("2) Purchase Lives")
	print("3) Main Menu")
	print("4) Exit")

	return input("Enter: ")

def game_loop():
	while(True):
		print_stats()
		game_input = game_menu()
		if game_input == '1':
			try:
				input_dict = get_input()
			except ValueError:
				print("Invalid input!")
			else:
				calculate_inputs(input_dict)
				random_list = create_list(input_dict)
				if(not game(random_list, input_dict)):
					print("GAME OVER")
					player['total_money'] = STARTING_MONEY
					break
		elif game_input == '2':
			print("Lives cost $10 per life.  How many would you like to purchase?")
			life_input_value = int(input("Enter: "))
			if (life_input_value * COST_TO_PURCHASE_LIFE) > player['total_money']:
				print("You do not have enought money.")
			else:
				player['total_lives'] += life_input_value
				player['total_money'] -= (life_input_value * COST_TO_PURCHASE_LIFE)
		elif game_input == '3':
			break
		elif game_input == '4':
			print("Good bye!!!")
			exit()
def main():
	print("Welcome to the number guessing game.")
	print("Rules:")
	print("- You start with $100 and the goal is to try to earn $" + str(WINNING_TOTAL) + ".")
	print("- If you run out of money, you lose the game.")
	print("- Every match, you input a range of random numbers and a list of numbers to guess.")
	print("- The longer the list and range the more money you can either win or lose.")
	print("- Every completed match, you earn " + str(WINNINGS_NUM_OF_LIVES) + " + extra lives not spent.")
	print("Good luck and have fun!")

	while(True):
		menu_input = main_menu()
		# New Game
		if menu_input == '1':
			game_loop()
		# Export lives and money to a text file
		elif menu_input == '2':
			print("Saving game...")
			if not os.path.exists('save'):
				os.makedirs('save')
			with open('save/saved_state.json', 'w') as fp:
				json.dump(player, fp)
		elif menu_input == '3':
			print("Loading saved game...")
			with open('save/saved_state.json') as json_data:
			    json_file = json.load(json_data)
			    json_data.close()
			    player['total_lives'] = int(json_file['total_lives'])
			    player['total_money'] = int(json_file['total_money'])
			    game_loop()
		# Import lives and money from a text file
		elif menu_input == '4':
			print("Good bye!!!")
			exit()
		else:
			print("Invalid input...")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nGood Bye!!!")
		exit()
