from characters import characters

startsA = 0
startsZ = 0
numDead = 0
numTitles = 0
mostTitles = ''
numVal = 0
hotpieActor = ''
notOnTV = 0
targaryens = 0

for i in characters:
    if i['name'].startswith('A'): startsA += 1
    if i['name'].startswith('Z'): startsZ += 1
    if i['died'] != '': numDead += 1
    if i['culture'] == 'Valyrian': numVal += 1
    if i['name'] == 'Hot Pie': hotpieActor = i['playedBy']
    if i['tvSeries'] == [""]: notOnTV += 1
    if 'Targaryen' in i['name']: targaryens += 1

print('Num characters: ', len(characters))
print('\nHow many characters names start with "A"? Ans:', startsA)
print('How many characters names start with "Z"? Ans:', startsZ)
print('How many characters are dead? Ans:', numDead)
print('How many characters are Valyrian? Ans:', numVal)
print('What actor plays "Hot Pie"? Ans:', hotpieActor)
print('How many characters are *not* in the tv show? Ans:', notOnTV)
print('How many characters have last name "Targaryen"? Ans:', targaryens)
print()

## dict_keys(['url', 'name', 'gender', 'culture', 'born', 'died', 'titles', 'aliases', 'father', 'mother', 'spouse', 'allegiances', 'books', 'povBooks', 'tvSeries', 'playedBy'])

### How many characters names start with "A"?
### How many characters names start with "Z"?
### How many characters are dead?
# Who has the most titles?
### How many are Valyrian?
### What actor plays "Hot Pie" (and don't use IMDB)?
### How many characters are *not* in the tv show?
# Produce a list characters with the last name "Targaryen"
# Create a histogram of the houses (it's the "allegiances" key)
