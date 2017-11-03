import random

print('--------------------------------------')
print('     Guess The Number App')
print('--------------------------------------')
print('')

target = random.randint(0,100)

guess_text = input('Guess a number between 0 and 100: ')
guess = int(guess_text)

while guess != target:
	if guess < target:
		print('Your guess is too low')
		guess_text = input('Please guess again: ')
		guess = int(guess_text)
	elif guess > target:
		print('Your guess is too high')
		guess_text = input('Please guess again: ')
		guess = int(guess_text)

print('You Win!!!')	