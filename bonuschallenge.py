import sys 
if len(sys.argv) == 2:
    word_or_sentence = sys.argv[1]
else:
    word_or_sentence = input("Word (w) or Sentence (s)? ").lower()

dict = {}
if word_or_sentence == 'w':
    s = input("\nPlease enter a word: ")
    for ltr in s:
        dict[ltr] = dict.get(ltr, 0) + 1    # dict.get(a,b) returns dict[a] if present, b if not present 

else:
    s = input("\nPlease enter a sentence: ").lower()
    newstr = ''

    # remove any non-alpha, non-space characters
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz ':
            newstr += i

    wordlist = newstr.split(' ')       #wordlist is a lowercase list of all the words in str

    for word in wordlist:               # iterate over words in wordlist
        dict[word] = dict.get(word, 0) + 1

    
print("\nThe top three {0} are:".format('words' if word_or_sentence == 's' else 'letters'))

lst = []
for item in dict:                       # conver the dict to a list of lists
    lst.append([item, dict[item]])

#create a new list containing the 3 items with the highest counts
top_lst = []
while len(top_lst) < 3:
    hi_pos = 0
    hi = lst[hi_pos]
    for i in range(1, len(lst)):
        if lst[i][1] > hi[1]:
            hi = lst[i]
            hi_pos = i
    # after the for loop completes, hi contains the item with the highest count 
    # and hi_pos is its index in lst

    top_lst.append(lst.pop(hi_pos))     # remove hi from lst and append it to top_lst

for item in top_lst:
    print(item[0] + ': ' + str(item[1]))

print()