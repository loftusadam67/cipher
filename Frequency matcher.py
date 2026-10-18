# ENTER THE TEXT INTO THIS STRING
TEXT = ""


letters = {}
#as per https://en.wikipedia.org/wiki/Letter_frequency
most_common = ["E","T","A","O","I","N","S","H","R","D","L","C","U","M","W","F","G","Y","P","B","V","K","J","X","Q","Z"]
most_common_dictionary = ["E","S","I","A","R","N","T","O","L","C","D","U","G","P","M","H","B","Y","F","V","K","W","Z","X","J","Q"]


#most_common = most_common_dictionary.copy()


most_common.reverse()

alphabetical = most_common.copy()
alphabetical.sort()
values = []

for i in alphabetical:
    letters[i] = 0

for letter in TEXT:
    if letter == " ":
        continue
    try:
        letters[letter] += 1
    except KeyError: # Filters out punctuation
        pass

for value in letters.keys():
    values.append(letters[value])

values.sort()
key = {}

for i in range(len(values)):
    value = values.pop()
    for x in letters.keys():
        if letters[x] == value:
            key[most_common.pop()] = x
            letters[x] = -1

string = ""
for i in alphabetical:
    string += key[i]

print(string)