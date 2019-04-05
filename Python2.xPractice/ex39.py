# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Nevada': 'NV',
    'Georgia': 'GA'
}

print "Inital states: ", states
print ">> sorted initial states: ", sorted(states)
# add some more states
states['New Mexico'] = 'NM'
states['Pencilvenia'] = 'PA'
states['Alabama'] = "AL"

print ">> with new states: ", states
print ">> sorted new states: ", sorted(states)

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'NV': 'Las Vegas',
    'NV': 'Carson City',
    'GA': 'Atlanta',
    'AL': 'Birmigham'
}


# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# add a few more cities
cities['Al'] = 'Alabama'
cities['GA'] = 'Georgia'
cities['NV'] = 'Reno'
cities['PA'] = 'Pheladelphia'
cities["NM"] = "NM City"

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']
print "Alabama's abbreviation is: ", states['Alabama']
print "Nevada's abbreviation is: ", states['Nevada']

# do it by using the state then cities dict
print '--' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
print "Nevada has: ", cities[states['Nevada']]
print "Alabama has: ", cities[states['Alabama']]


# print every state abbreviation
print '--' * 10
for s, a in states.items():
    print "%s is abbreviated %s" % (s, a)

# print every city in state
print '--' * 10
for a, c in cities.items():
    print "%s has the city %s" % (a, c)

# now do both at the same time
print '---' * 10
for s, a in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        s, a, cities[a])

print '----' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
