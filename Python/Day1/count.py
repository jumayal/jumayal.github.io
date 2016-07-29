text = 'A man a plan a canal panama'
words = text.lower().split()

counts = {}

for word in words:
    if word in counts:
        #Add a count to the value
        counts[word] = counts[word] + 1
    else:
        #Add word to counts
        counts[word] = 1
print counts
