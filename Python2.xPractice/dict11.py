# dict11.py

words = { 'name': 'Mahdi', 'house': '1105 14 st', 'apt': 'B' }

print words['house']

print words.keys()
print words.values()
print words.items()

words2list = list(words)
print "words2list : ", words2list

list3= sorted(words2list)
print "sorted words2list : ", sorted(words2list)

print " list3 vs sorted words2list : ", cmp(list3, sorted(words2list))

print words.pop('name')
print words
#words.clear()
print words
