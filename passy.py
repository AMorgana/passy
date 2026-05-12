import secrets

word_list = []
passphrase = ""
words_n = 4

allowed_symbols = input("Enter valid special characters (default: !@#$%^&*-, type 'n' for none): ").lower()
if allowed_symbols == "":
    allowed_symbols = "!@#$%^&*-"
elif allowed_symbols == "n" or allowed_symbols == "none":
    allowed_symbols = ""

if allowed_symbols != "":
    sep_choice = input("Use only one symbol as a separator? (y/N): ")
else:
    sep_choice = ""

use_one_symbol = sep_choice.lower()

use_randome_number = input("Use randome number? (y/N): ").lower()

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

# pick a random index to append a 0-9 to it

if use_randome_number == "y":
    num_index = secrets.randbelow(words_n)
    num_random = secrets.randbelow(10)
    selected_words[num_index] = selected_words[num_index] + str(num_random)

if allowed_symbols:
    if use_one_symbol == "y":
        sep = secrets.choice(allowed_symbols)
        for i, word in enumerate(selected_words):
            passphrase += word
            # Add the separator ONLY if this isn't the digit word
            # AND it's not the very last word
            if i != num_index and i < words_n - 1:
                passphrase += sep
    else:
        for i, word in enumerate(selected_words):
            passphrase += word
            if i != num_index and i < words_n - 1:
                passphrase += secrets.choice(allowed_symbols)
else:
    # If the user chose 'none', just squish them together
    passphrase = "".join(selected_words)
print(passphrase)

