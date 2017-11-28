the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#the first for-loop goes through a list
for number in the_count:
	 print "This is count %d" % number
	 
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# going through mixed lists
# using %r because we don't know what's in it
for i in change:
	print "I got %r" % i
	
#buidling lists, starting with empty one
elements = []

#using range function to do 0 o 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
 	# append is a function that lists understand
 	elements.append(i)
 	
#printing them out
for i in elements:
	print "Element was: %d" % i