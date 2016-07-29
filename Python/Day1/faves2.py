fave = raw_input('What\'s your favorite food? ')
caps_fave = fave.upper()
vowels = ['A', 'E', 'I', 'O', 'U']
for c in vowels:
    caps_fave = caps_fave.replace(c, c * 5)
    print caps_fave
