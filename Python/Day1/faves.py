response= raw_input("What is your favorite food")
newWord = ""
for i in range (0, len(response)):
    newLetter = response[i]
    if "a" in newLetter:
        newLetter= newLetter.replace('a','aaaaa')
    if "e" in newLetter:
        newLetter=newLetter.replace('e','eeeee')
    if "i" in newLetter:
        newLetter= newLetter.replace('i','iiiii')
    if "o" in newLetter:
        newLetter= newLetter.replace('o','ooooo')
    if "u" in newLetter:
        newLetter= newLetter.replace('u','uuuuu')
    newWord = newWord + newLetter
print newWord
