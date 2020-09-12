def check_guess(guess, answer):
	global score
	still_guessing = True
	attempt = 0
	while still_guessing and attempt < 3:
		if guess.lower() == answer.lower():
			print("Correct answer")
			score = score + 1
			still_guessing = False
		else:
			if attempt < 2:
				guess = input('Sorry wrong answer, Try again ')
			attempt = attempt +1
	if attempt == 3:
			print('The corect answer is ' + answer)


score = 0
print(" Animal Quiz ")
# guess1 = input('which bear lives at the Norh pole? ')
# check_guess(guess1, 'polar bear')

# guess2 = input('which is the faster land animal? ')
# check_guess(guess2, 'cheetah')

# guess3 = input('which is the largest animal? ')
# check_guess(guess3, 'blue whale')

# guess4 = input('which is the highest animal? ')
# check_guess(guess4, 'Giraffe')

guess5 = input('which one is a fish?\n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n')
check_guess(guess5,'C')
print('Your score is '+ str(score))
