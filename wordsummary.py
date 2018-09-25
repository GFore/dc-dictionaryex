# Write a word histogram program that asks the user for a sentence as its input,and prints
# a dictionary containing the tally of how many times each word was used in the text

str = input("Please enter a sentence: ").lower()
newstr = ''

# remove any non-alpha, non-space characters
for i in str:
    if i in 'abcdefghijklmnopqrstuvwxyz ':
        newstr += i

wordlist = newstr.split(' ')       #wordlist is a lowercase list of all the words in str

dict = {}
for word in wordlist:               # iterate over words in wordlist
    if word in dict:                # if word is already in dict, then increment its value
        dict[word] += 1
    else:                           # if word is not in dict, add it with val of 1
        dict[word] = 1

print(dict)