# telling python to make a function by using def for define

# like scripts with argv
def print_two(*args): #print_two = name of function
	arg1, arg2 = args #indention of the lines is important - attaches lines to the function
	print "arg1: %r, arg2: %r" % (arg1, arg2) 
	
# without *args
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# prints no arguments
def print_none():
	print "I got nothin'."
	

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()