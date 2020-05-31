import collections
s = 'a word and another word'
#c = collections.Counter(s)
#print(c)

# monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
#
# monty_words = monty_quote.split(" ")
# c = collections.Counter(monty_quote)
# print(c)
c = {}
for i in s:
    c[i] = c.get(i,0) + 1

print(c)

#https://stackoverflow.com/questions/23910595/counting-letters-in-a-string-python
