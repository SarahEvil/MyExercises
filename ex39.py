 # -*- coding: utf-8 -*- 
#mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
	}
	
#set of states with cities in them
cities ={
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

#add cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#using state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
#print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has city %s" % (abbrev, city)
	
#both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])
		
print '_' * 10
#get abbrev by state that's not there
state = states.get ('Texas')

if not state:
	print "Sorry, no Texas."
	
#get city with default value
city = cities.get('TX', 'Does Not Exist')	
print "The city for the state 'TX' is: %s" % city

