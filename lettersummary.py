# Write a letter_histogram program that asks the user for input, and prints
# a dictionary containing the tally of how many times each letter in the
# alphabet was used in the word. 

word = input("\nPlease enter a word: ")     # append .lower() here for case insensitive

histogram_dict = {}

for letter in word:
    if letter in histogram_dict:
        histogram_dict[letter] += 1
    else:
        histogram_dict[letter] = 1

    #histogram_dict[letter] = histogram_dict.get(letter, 0) + 1

print(histogram_dict)
print()