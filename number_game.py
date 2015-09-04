import random

# Constants
MIN_DIFFERENCE = 5
MIN_LIST = 3

class Bank(object):
	def __init__(self, inital_deposit):
		self.total_amount = inital_deposit
	def deposit(amount):
		self.total_amount += amount
	def withdrawal(amount):
		self.total_amount -= amount

def check_value(guess, correct_value):
	if guess == correct_value:
		return True
	else:
		return False

def get_input():
	min_random_value = 0
	max_random_value = 0
	num_of_list_values = 0
	num_of_tries = 0

	while((max_random_value - min_random_value) < MIN_DIFFERENCE):
		print("Range needs to be greater than " + str(MIN_DIFFERENCE))
		min_random_value = int(input("Minimum random value: "))
		max_random_value = int(input("Maximum random value: "))
	
	while(num_of_list_values < MIN_LIST):
		print("Number of list values needs to be greater than " + str(MIN_LIST))
		num_of_list_values = int(input("Number of values in list: "))

	while(num_of_tries < num_of_list_values):
		print("Number of tries needs to be greater or equal to number of list values.")
		num_of_tries = int(input("Number of tries: "))

	return {'min_random_value': min_random_value,
		'max_random_value': max_random_value,
		'num_of_list_values': num_of_list_values,
		'num_of_tries': num_of_tries
		}

def calculate_inputs(input_dict, bank):
	difference = input_dict['max_random_value'] - input_dict['min_random_value']

def create_list(input_dict):
	return [random.randint(input_dict['min_random_value'],input_dict['max_random_value'])
		       for x in range(1,input_dict['num_of_list_values']+1)]

def game(random_list, input_dict):
	index = 0
	num_of_tries = input_dict['num_of_tries']
	min_value = str(input_dict['min_random_value'])
	max_value = str(input_dict['max_random_value'])

	active_list = ['x' for x in range(0,len(random_list))]
	while(True):
		try:
			print(active_list)
			print("Number of tries left: %d" % num_of_tries)
			input_value = int(input("Enter guess between " + min_value + " and " + max_value + ": "))
			if input_value < int(min_value) or input_value > int(max_value):
				raise ValueError
			if check_value(input_value, random_list[index]):
				active_list[index] = input_value
				index += 1
				if index == len(random_list):
					print(active_list)
					print("You Win!")
					break
			else:
				num_of_tries -= 1
				if num_of_tries == 0:
					print("Game Over!")
					break
				if input_value < random_list[index]:
					print ("Guess higher")
				elif input_value > random_list[index]:
					print ("Guess lower")
		except ValueError:
			print("Invalid input.  Integer value must be between " + min_value + " and " + max_value + ".")

def menu():
	print("-------------------")
	print("1) New Game")
	print("2) Export Game")
	print("3) Exit")
	
	return input("Enter: ")

def main():
	print("Welcome to the number guessing game.  You start with $100 and the goal is to try to earn $100k.")
	while(True):
		menu_input = menu()
		if menu_input == '1':
			bank = Bank(100.00)
			print("$%.2f" % bank.total_amount)
			input_dict = get_input()
			calculate_inputs(input_dict,bank)
			random_list = create_list(input_dict)
			game(random_list, input_dict)
		elif menu_input == '2':
			print("Not yet implemented")
		elif menu_input == '3':
			print("Good bye!!!")
			exit()
		else:
			print("Invalid input...")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nGood Bye!")
		exit()
