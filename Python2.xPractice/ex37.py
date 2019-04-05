ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "I have these many stuffs: \n", ten_things
print "Oops!! there's not 10 things in that list, let's fix that."

stuff1 = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print "I have more stuffs:\n ", more_stuff

while len(stuff1) != 10:
    next_one = more_stuff.pop()
    print ">Adding: ", next_one
    stuff1.append(next_one)
    print "There's %d items now." % len(stuff1)

print "There we go: ", stuff1
print "\nAdditional item are taken form the last tail of the more stufffs: "
len_of_more_stuff = len(more_stuff)
stuff2 = ten_things.split(' ')

while len(stuff2) != 10:
    
    for i in range(len_of_more_stuff):
        next_one = more_stuff[i]
        print ">>Adding: ", next_one
        stuff2.append(next_one)

    print "There's %d items now." % len(stuff2)

print "There we go: ", stuff2
print "\nAdditional item are taken form the last head of the more stufffs: "

print "stuff1: ", stuff1
print "stuff2: ", stuff2

allstuffs = stuff1 + stuff2 # what? cool!
print "All %d stuffs are as follows: " %len(allstuffs)
print allstuffs


print "\n\nLet's do some things with the all stuffs."

print allstuffs[1]
print allstuffs[-1] # whoa! fancy
#print allstuffs.pop()
print ', '.join(allstuffs) # what? cool!
print "\n\n"
print ' & '.join(allstuffs[3:10]) # super stellar!
print '  '.join(allstuffs[0]) # super stellar!
