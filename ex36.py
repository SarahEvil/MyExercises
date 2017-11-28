from sys import exit

#a possibility to get extra presents...or loose 'em all
def extra_points():
	print "As we all know, Santa loves Cookies. How many Cookies do you give him?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		"I need a number - try again."
		exit(0)
		
	if how_much < 20:
		print "That's Santas fovourite amount! You get an exra special present - Merry Christmas!"
		exit (0)
	else:
		print "That's too many..the next morning you find Santa sleeping in the living room due to food coma."
		print "He wakes up in shock and runs away, forgetting to leave your presents with you :("
		exit(0)



#yes or no to cookies - When you haven't pepared cookies
def no_cookies():
	print "Oh no, Santa will be so sad!"
	print "You DONT CARE?"
	print "Or are you quickly going to DOITNOW?"
	bake_cookies = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "DONT CARE":
			insomnia("That won't be good for your present count this year. You will get nothing.")
		elif choice == "DOITNOW" and not bake_cookies:
			print "You put pre baked cookies on a plate. Santa will be proud of you."
			bake_cookies = True
		elif choice =="DOITNOW" and bake_cookies:
			insomnia("You spend the whole night baking and therefore oversleep Christmas.")
		elif choice == "COUNTING COOKIES" and bake_cookies:
			extra_points()
		else:
			print "You see mummy kissing Santa Clause - quickly do something else!"



#yes or no to cookies - yes you prepared cookies
def yes_cookies():
	print "Good kid!"
	print "Are they BOUGHT or SELFMADE?"
	
	choice = raw_input("> ")
	
	if "BOUGHT" in choice:
		print "Not the best but oh well. Lucky for you, he isn't that picky."
	elif "SELFMADE" in choice:
		print "Awesome! You will for sure be his favourite this Christmas."
	else:
		insomnia()
		



#else functionblock
def insomnia(why):
	print why, "Try again next year!!"
	exit(0)



#start
def start():
	print "It is the 24th of December, Christmas evening."
	print "The tree is decorated. "
	print "You enjoyed a Christmas feast with your family."
	print "Finally, you lay in bed...but you can't sleep because you can't stop thinking about one thing... "
	print "Have you put out the Cookies for Santa Clause? Answer in capital letters:"
	
	choice = raw_input("> ")
	
	if choice == "YES":
		yes_cookies()
	elif choice == "NO":
		no_cookies()
	else:
		insomnia("You finally get to sleep at 6 o'clock in the morning and oversleep X-Mas.")
		

start()