from characters import characters
from urllib.request import Request, urlopen

startsA = 0
startsZ = 0
numDead = 0
maxTitles = 1
mostTitles = ''
numVal = 0
hotpieActor = ''
notOnTV = 0
targaryens = 0
houses = {}
house_dict = {}

for i in characters:
    if i['name'].startswith('A'): startsA += 1
    if i['name'].startswith('Z'): startsZ += 1
    if i['died'] != '': numDead += 1
    if len(i['titles']) > maxTitles:
        maxTitles = len(i['titles'])
        mostTitles = i['name']
    if i['culture'] == 'Valyrian': numVal += 1
    if i['name'] == 'Hot Pie': hotpieActor = i['playedBy'][0]
    if i['tvSeries'] == [""]: notOnTV += 1
    if 'Targaryen' in i['name']:
        targaryens += 1
        print(i['name'])

    allegs = i['allegiances']
    
    for house in allegs:                                       # house is a URL
        housename = house_dict.get(house, '')                  # if housename already found, then use it, don't get url again
        if housename == '':
            print('new')
            req = Request(house, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read().decode('utf-8')
            housename = webpage[webpage.find("name")+7: webpage.find("region")-3]
            house_dict[house] = housename
        print(housename)
        houses[housename] = houses.get(housename, 0) + 1

print('Num characters: ', len(characters))
print('\nHow many characters names start with "A"? Ans:', startsA)
print('How many characters names start with "Z"? Ans:', startsZ)
print('How many characters are dead? Ans:', numDead)
print('Who has the most titles? Ans: {0} ({1})'.format(mostTitles, maxTitles))
print('How many characters are Valyrian? Ans:', numVal)
print('What actor plays "Hot Pie"? Ans:', hotpieActor)
print('How many characters are *not* in the tv show? Ans:', notOnTV)
print('How many characters have last name "Targaryen"? Ans:', targaryens)
print('Histogram of the Houses:')
print(houses)
print()
print(house_dict)

## dict_keys(['url', 'name', 'gender', 'culture', 'born', 'died', 'titles', 'aliases', 'father', 'mother', 'spouse', 'allegiances', 'books', 'povBooks', 'tvSeries', 'playedBy'])

### How many characters names start with "A"?
### How many characters names start with "Z"?
### How many characters are dead?
### Who has the most titles?
### How many are Valyrian?
### What actor plays "Hot Pie" (and don't use IMDB)?
### How many characters are *not* in the tv show?
## Produce a list characters with the last name "Targaryen"
# Create a histogram of the houses (it's the "allegiances" key)
