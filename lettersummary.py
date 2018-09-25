# Write a letter_histogram program that asks the user for input, and prints
# a dictionary containing the tally of how many times each letter in the
# alphabet was used in the word. 

str = input("Please enter a word: ")

dict = {}
for ltr in str:
    if ltr in dict:
        dict[ltr] += 1
    else:
        dict[ltr] = 1

print(dict)