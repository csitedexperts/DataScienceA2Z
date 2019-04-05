class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

print "\n aaaaaaaaaaaaaaaaaaaab \n"
dad.implicit()
son.implicit()
print "\n bbbbbbbbbbbbbbbbbbbbb \n"
dad.override()
son.override()
print "\n ccccccccccccccccccccc \n"
dad.altered()
son.altered()
