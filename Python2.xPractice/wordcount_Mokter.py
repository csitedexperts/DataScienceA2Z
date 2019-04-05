
# CS 591 Assignment-3: Mokter Hossain 10-23-2013

import os
from collections import Counter
import time
import re

totallines, blanklines, totalsentences, totalwords, wordfreq = 0, 0, 0, 0, 0
initletter, word1, word2, word3 = '', "", "", "" 


#fname = "Myfile1.txt"

fname = "bible+shakes.nopunc.txt"

myfile = open(fname, "r")

# reads one line at a time

for line in myfile:
  #  print line,   # test
    totallines += 1
    if line.startswith('\n'):
        blanklines += 1
    else:
        # assume that each sentence ends with . or ! or ?
        totalsentences += line.count('.') + line.count('!') + line.count('?')

        # Double space counts as single space
        tempwords = line.split(None)

        totalwords += len(tempwords)   #  total words

print "\n\nWelcome to the WordCount Program"
print '-' * 50
print "The file: ",fname, " contains: "

print "Total Lines: ", totallines
print "Blank lines: ", blanklines
#print "Total Sentences  : ", totalsentences
print "Total Words: ", totalwords
print '-' * 50

loop = 1
# the following 'choice' variable holds the user's choice in the menu:
choice = 0

while loop == 1:
    #print what options you have
    print "Current time is : %s" % time.ctime()
    print "\nChoose one of the following options (1-4): "
    print " "
    print "1) Enter a word to count its occurrence in the file : "
    print "2) Enter a letter to count the number of words start with the letter : "
    print "3) Enter two words to count the number of times these two words occur together : "
    print "4) Quit the Program. "
    print " "

    choice = input("Choose one of the above options (1-4): ")

    if choice == 1:
        word1 = raw_input("Enter a word to count its occurrence in the file (Case Sensitive!) :")
               
        starttime = time.clock()

        wordfreq = 0
        i =0
        
        with open(fname, 'r') as searchfile:
            for line in searchfile:
                #print line
                newline = line.split()
                #print newline
                for word in newline:
                    #print word
                    if word == word1:
                        wordfreq = wordfreq +1
        if  wordfreq >=0:
           print "\nThe word: '", word1, "' exists", wordfreq, " times in the file"
        else:
           print "\nThe word: ", word1, ": does not exist in the file (The search was Case Sensitive)"

        endtime = time.clock()
        print "The search took %0.3f ms"  %((endtime-starttime)*1000.0)
        
        print "\n"

        
    elif choice == 2:
        wordfreq = 0  
        initletter = raw_input("Enter a letter to count the number of words start with the letter (Case Sensitive!):")

        
        starttime = time.clock()
        with open(fname, 'r') as searchfile:
            for line in searchfile:
                #print line
                newline = line.split()
                #print newline
                for word in newline:
                    #print word
                    if word.startswith(initletter):
                        wordfreq = wordfreq +1
        if  wordfreq >=0:
           print "\nThere are total", wordfreq, " words that start with the letter : ", initletter
        else:
           print "\nThe is no word that starts with the letter (The search was Case Sensitive):", initletter

        endtime = time.clock()
        print "The search took %0.3f ms"  %((endtime-starttime)*1000.0)
        
        print "\n"

        
    elif choice == 3:
        wordfreq = 0
        print "Enter two words to count the number of times these two words occur together : "
        word1 = raw_input("Enter the first word :")
        word2 = raw_input("Enter the second word :")
        
        starttime = time.clock()
        word3 = word1 + " " + word2
                
        with open(fname, 'r') as searchfile:
            for line in searchfile:
                #print line
                newline = line.split()
                #print newline
                for i in range(0, len(newline)-1):
                    if word1==newline[i]:
                        if(word2==newline[i+1]):
                            wordfreq = wordfreq +1
                
        if  wordfreq >=0:
           print "\nThe combined words:'",word3,"' exists", wordfreq, " times in the file"
        else:
           print "\nThe combined words:", word3,": does not exist in the file (The search was Case Sensitive)"

        endtime = time.clock()
        print "The search took %0.3f ms"  %((endtime-starttime)*1000.0)
        print "\n"
      
     
    elif choice == 4:
        loop = 0
	
print "\nThank you for using the WordCount program!"
print "Local time is : %s" % time.ctime()

myfile.close()  # Closes the open file

# End od the program

