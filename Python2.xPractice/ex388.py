from random import randint

mydict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print mydict

print mydict[1]

mydict[1] = "Mahdi"
print mydict


for i in range(9):
    print mydict[i]
    print mydict

print "\n\n Let us now play with ", mydict

searchitem = sorted(mydict)
for i in range(0, randint(0, 10)):
    searchitem[i] = mydict[i]
    #print ">> %r " %searchitem[i]
    if searchitem[i] == mydict[i]:
        
        print "%r is in mydict " %searchitem[i]
    else:
        print "%r is not in mydict" %searchitem[i]
        continue


