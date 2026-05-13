import secrets
import math

def calculate_entropy(word_count, list_length, use_caps, include_number, separator_string, use_single_symbol):
    """Calculates the theoretical entropy of the generated passphrase."""

    # 1. Base word entropy
    # If list_length is 7776, math.log2(7776) is ~12.92 bits per word
    entropy = word_count * math.log2(list_length)

    # 2. Capitalization Bonus
    if use_caps:
        # Assuming you randomly capitalize one character/word.
        # It adds roughly 4 to 5 bits of entropy.
        entropy += math.log2(word_count)

        # 3. Number Bonus
    if include_number:
        # Choosing 1 random digit (0-9) adds exactly log2(10) bits
        entropy += math.log2(10)

        # 4. Symbol Bonus
    if separator_string:
        # Removing duplicates from the string to get the true pool of unique symbols
        unique_symbols = len(set(separator_string))
        if unique_symbols > 0:
            if use_single_symbol:
                entropy += math.log2(unique_symbols)
            else:
                num_gaps = word_count - 1
                if num_gaps > 0:
                    entropy += num_gaps * math.log2(unique_symbols)
    return round(entropy, 1)

def load_words(filename):
    # open the file and create the list
    words = []
    with open(filename) as file:
        for line in file: words.append(line.split()[1])
    return words

def select_random_words(word_pool, count):
    # ask user for number of words
    selected_words = []

    for _ in range(count):
        new_word = secrets.choice(word_pool)
        selected_words.append(new_word)
    return selected_words

def add_word_complexity(words_list,use_digit, use_caps):
    count = len(words_list)
    # Capitalize a random word if 'use_caps' is True
    if use_caps:
        caps_index = secrets.randbelow(count)
        words_list[caps_index] = words_list[caps_index].upper()
    # add a 0-9 digit if 'use_digit' is True
    if use_digit:
        num_index = secrets.randbelow(count)
        words_list[num_index] += str(secrets.randbelow(10))
    return words_list

def assemble_passphrase(words_list, symbols_used, use_single_symbol):
    # Join word pool to generate a single passphrase
    passphrase = ''
    count = len(words_list)
    # If the user just wants to use a single symbol, we'll randomly select 1 index from the length of symbols
    if use_single_symbol and symbols_used:
        sing_sym = symbols_used[secrets.randbelow(len(symbols_used))]
    for i, word in enumerate(words_list):
        passphrase += word
        if i < (count - 1) and symbols_used:
            if use_single_symbol:
                passphrase += sing_sym
            else:
                passphrase += secrets.choice(symbols_used)
    return passphrase

filepath = "eff_words.txt"
if __name__ == "__main__":
    words_num = int(input("Number of words to use: "))
    allowed_symbols = input("Symbols: ")
    word_list = load_words(filepath)
    wordpool = select_random_words(word_list, words_num)
    wordpool = add_word_complexity(wordpool,True)
    passphrase = assemble_passphrase(wordpool,allowed_symbols,True)
    print(wordpool)
    print(passphrase)

