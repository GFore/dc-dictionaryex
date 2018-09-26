# Write a word histogram program that asks the user for a sentence as its input,and prints
# a dictionary containing the tally of how many times each word was used in the text

sentence = input("Please enter a sentence: ").lower()
newstr = ''

# remove any non-alpha, non-space characters
for i in sentence:
    if i in 'abcdefghijklmnopqrstuvwxyz ':
        newstr += i

wordlist = newstr.split(' ')       #wordlist is a lowercase list of all the words in sentence

word_dict = {}
for word in wordlist:               # iterate over words in wordlist
    if word in word_dict:                # if word is already in word_dict, then increment its value
        word_dict[word] += 1
    else:                           # if word is not in word_dict, add it with val of 1
        word_dict[word] = 1

print(word_dict)