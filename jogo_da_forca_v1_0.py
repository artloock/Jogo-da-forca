# Jogo da Forca Versão 1.0python jogo_da_forca_v1_0.py

# Import
import random
from os import system, name

#function to clean the screen after restart
def clean_screen():

	# Windows
	if name == 'nt':
		_ = system('cls')

	# Mac / Linux
	else:
		_ = system('clear')

# Function
def game():

	clean_screen()
	print("\nWelcome to the hangman game!")
	print("Guess the word below.")

	# Game words lists
	Words = ['banana', 'apple', 'orange', 'strawberry', 'grape', 'watermelon', 'pineapple', 'kiwi', 'peach', 'pear', 'cherry', 'mango', 'blueberry', 'raspberry', 'plum', 'apricot', 'fig', 'pomegranate', 'lychee', 'cantaloupe']

	# Chose words randomly
	Word = random.choice(Words)

	# List comprehension
	discovered_letters = ['_' for letter in Word]

	# Number of chances
	chances = 6

	# Wrong letters list
	wrong_lettes = []

	#Loop while the number of chances is not zero.
	while chances > 0:

		# Print
		print(" ".join(discovered_letters))
		print("\nRemaning chances:", chances)
		print( "Wrong letters:"," ".join(wrong_lettes))

		# Attempt
		attempt = input("\nTipe one letter: ").lower()
		while not attempt.isalpha() or len(attempt) != 1:
			print("Please tipe only letters and do not repeat letters.")
			attempt = input("\nTipe one letter: ").lower()

		# Conditional
		if attempt in Word:
			index = 0

			for letter in Word:
				if attempt == letter:
					discovered_letters[index] = letter
				index += 1
		else:
			chances -= 1
			wrong_lettes.append(attempt)

		# Conditional
		if "_" not in discovered_letters:
			print("\nCongratulations, you won! The word was:", Word)
			break
	# Verify chances
	if chances == 0:
		print("\nYou lose! The word was:", Word)

	# Ask for restart
	restart = input("\nWant to try again? (y/n): ").lower()
	if restart == 'y':
		game() 
	else:
		print("Thanks for playing!")