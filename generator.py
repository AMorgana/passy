import secrets
import string

word_list = []
passphrase = ""
words_n = 4
allowed_symbols = input("Enter valid special characters to use: ")
sep_choice = input("Use only one symbol as a separator? (y/N): ")

use_one_symbol = sep_choice.lower()
with open("eff_words.txt") as file:
	for line in file:
		word_list.append(line.split()[1])

selected_words = []

for word in range(words_n):
	new_word = secrets.choice(word_list)
	selected_words.append(new_word)


# pick a random index (0,1,2 or 3)
caps_index = secrets.randbelow(words_n)
selected_words[caps_index] = selected_words[caps_index].upper()

if use_one_symbol == "y":
	#pick the one symbol as a separator
	sep = secrets.choice(allowed_symbols)
	# Use join to put that symbol between each word
	passphrase = sep.join(selected_words)
else:
	for word in selected_words:
		symbol = secrets.choice(allowed_symbols)
		passphrase += word + symbol
	passphrase = passphrase[:-1]
print(passphrase)

