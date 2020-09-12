import random
import string



adjectives = ['sleep', 'slow', 'smelly',
             'wet', 'fat', 'red',
			 'orange', 'yellow', 'green', 
			 'blue', 'purple', 'fluffy',
			 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball'
		 'toaster', 'goat', 'dragon'
		 'hammer', 'duck','panda',]
last_name = ['truong', 'le']
mid_name = ['huu']
frist_name =['phat', 'dat']
print('welcome to password picker')

while True:		
	adjective = random.choice(adjectives)
	noun = random.choice(nouns)
	number = random.randrange(0,100)
	special_char = random.choice(string.punctuation)
	password = adjective + noun + str(number) + special_char
	lastName = random.choice(last_name)
	firstName = random.choice(frist_name)
	password2 = adjective+ lastName + firstName + str(number) + special_char
	print('Your new password is: %s' % password)
	print('Your new password2 is: %s' % password2)
	respone = input('Would you like anther password? Type y or n: ')
	if respone == 'n':
		break