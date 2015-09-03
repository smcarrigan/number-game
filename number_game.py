import random

def check_value(guess, correct_value):
	if guess == correct_value:
		return True
	else:
		return False

def get_input():
	min_random_value = int(input("Minimum random value: "))
	max_random_value = int(input("Maximum random value: "))
	num_of_list_values = int(input("Number of values in list: "))
	num_of_tries = int(input("Number of tries: "))
	return {'min_random_value': min_random_value,
		'max_random_value': max_random_value,
		'num_of_list_values': num_of_list_values,
		'num_of_tries': num_of_tries
		}

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
		print(active_list)
		print("Number of tries left: %d" % num_of_tries)
		try:
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
					exit()
				if input_value < random_list[index]:
					print ("Guess higher")
				elif input_value > random_list[index]:
					print ("Guess lower")
		except ValueError:
			print("Invalid input.  Integer value must be between " + min_value + " and " + max_value + ".")
		except KeyboardInterrupt:
			print("Good Bye!")
			exit()
def main():
	input_dict = get_input()
	random_list = create_list(input_dict)
	game(random_list, input_dict)

if __name__ == "__main__":
	main()
