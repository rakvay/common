#Write a list comprehension that results in a list of every letter in the word smogtether capitalized.

word = 'smogtether'

result = [x.capitalize() for x in word ]

print(result)