# sets1.py

set1 = set(['a', 'b', 'c', 'c', 'd'])
set2 = set(['a', 'b', 'x', 'y', 'z'])

print "set1: " , set1
print "set2: " , set2
print "intersection: ", set1 & set2
print "union: ", set1 | set2
print "difference: ", set1 - set2
print "symmetric difference: ", set1 ^ set2

s1 = set([1, 2, 3, 4, 5, 6,1, 2, 3,4 ,5])

print s1
s2 = set([1, 3, 5])

print s2

print "Is s2 a subset of print s1 ?", s2.issubset(s1)

print "Is s1 a subset of print s2 ?", s1.issubset(s2)


s1.add(1)
s1.add(10)
s1.add(12)
s1.add(13)
s1.add(14)
s1.add(15)
s1.add(16)
s1.add(17)
s1.add(18)


print "s1 now ", s1


print "Is s2 a subset of print s1 ?", s2.issubset(s1)

print "Is s1 a subset of print s2 ?", s1.issubset(s2)

s1.clear()

print "s1 now ", s1

fs = frozenset(['a', 'b', 'c'])
print fs
