import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the my Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


max_letters = len(letters)
max_numbers = len(numbers)
max_symbols = len(symbols)

password = []

for each_letter in range(1, (nr_letters + 1)):
  random_letter_position = random.randint(0, (max_letters - 1))
  password.append(letters[random_letter_position - 1])

for each_symbol in range(1, (nr_symbols + 1)):
  random_symbol_position = random.randint(0, (max_symbols - 1))
  password.append(symbols[random_symbol_position])

for each_number in range(1, (nr_numbers + 1)):
  random_number_position = random.randint(0, (max_numbers - 1))
  password.append(numbers[random_number_position])

random.shuffle(password)

encrypted_password = ""

for each_character in password:
  encrypted_password += each_character

print(encrypted_password)