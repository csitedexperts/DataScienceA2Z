
class Add2Numbers():
    num1 = 0
    num2 = 0
    sum = 0
    
    def __init__(self, num):
        self.num = num
        
    def Add2FixedNumbers(self, num1, num2):
        print "This is inside the Add2FixedNumbers()"
        print "num1 = %r" %self.num1
        print "num2 = %r" %self.num2
        print "sum = %r" %(self.num1 + self.num2)

    def AddAny2Numbers(self):
        print "This is inside the AddAny2Numbers()"
        num1 = float(raw_input("Enter num1: "))
        num2 = float(raw_input("Enter num2: "))
        print "num1 = %r" %num1
        print "num2 = %r" %num2
        sum = float(num1) + float(num2)        
        print "sum = %r" %sum
                    #sum = num1 + num2)


n = Add2Numbers(0)
n.num1 = 100
n.num2 = 200
sum = n.num1 + n.num2

print "\nWithout calling Add2FixedNumbers().. "
print "num1 = %s" %n.num1
print "num2 = %s" %n.num2
print "sum = %s" %sum

print "\nAfter calling Add2FixedNumbers().. "
n.Add2FixedNumbers(n.num1, n.num2)


print "\n"
    
n1 = Add2Numbers(0)
print "\nAfter calling AddAny2Numbers().. "
n.AddAny2Numbers()




    
