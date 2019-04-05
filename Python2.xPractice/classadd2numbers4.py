
class Add2Numbers():
    num1 = 0
    num2 = 0
    sum = 0
    
    def __init__(self):
        pass
                    # this __init__ coould not be used
                    
    def Add2FixedNumbers(self, num1, num2):
        print "Inside the Add2FixedNumbers()"
        print ">>num1 = %r" %self.num1
        print "num2 = %r" %self.num2
        print "sum = %r" %(self.num1 + self.num2)

    def AddAny2Numbers(self):
        print "Inside the AddAny2Numbers()"
        num1 = float(raw_input("Enter num1: "))
        num2 = float(raw_input("Enter num2: "))
        print "num1 = %r" %num1
        print "num2 = %r" %num2
        sum = float(num1) + float(num2)        
        print "sum = %r" %sum
        
        
    def EnterAndAddAny2Numbers(self, num1, num2):
        print "Inside the EnterAndAddAny2Numbers()"
        self.num1 = float(raw_input("Enter num1: "))
        self.num2 = float(raw_input("Enter num2: "))
        print "num1 = %r" %self.num1
        print "num2 = %r" %self.num2
        sum = float(self.num1) + float(self.num2)
        print "sum = %r" %sum
                    #sum = num1 + num2)


n = Add2Numbers()
n.num1 = 100
n.num2 = 200
sum = n.num1 + n.num2

print "\nWithout calling Add2FixedNumbers().. "
print "num1 = %s" %n.num1
print "num2 = %s" %n.num2
print "sum = %s" %sum


print "\nBut this is more convenient, just calling the methods ... "
n.Add2FixedNumbers(n.num1, n.num2)
n.AddAny2Numbers()
n.EnterAndAddAny2Numbers(0, 0)

#Also could be as follows
#n1 = Add2Numbers()
#n1.AddAny2Numbers()

