f = open("alice_in_wonderland.txt")
special_character = ["\'","\"","!","?",".",",",";",":","-","(",")"]
book = f.read()
lowercaps_book = book.lower()
better_book = lowercaps_book
counts = {}

for character in special_character:
    better_book = better_book.replace(character,"")

better_book = better_book.split()

for word in better_book:
    if word in counts:
        #Add a count to the value
        counts[word] = counts[word] + 1
    else:
        #Add word to counts
        counts[word] = 1

#print counts

for words in counts:
    if counts[words] > 100:
        print words
