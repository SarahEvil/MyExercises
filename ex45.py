 # -*- coding: utf-8 -*- 

#Buddy he Elf - saves X-Mas again

from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()
			
			
			
			
class Loss(Scene):
	def enter(self):
		print "________________________________________________"
		print "You lost."
		print "Santa won't be able to deliver the gifts,"
		print "so we won't be able to celebrate X-Mas this year"
		print "and it's all your fault!"
		print "We trusted you, you impostor..."
		return 'NorthPole'
		
		
		

class NorthPole(Scene):

	def enter(self):
		print "\n"
		print "This is Buddy the Elf: Save X-Mas (again)"
		print "a game about a fictional - tho we all know it's true - story,"
		print "about an adopted Elf named Buddy, who was raised in the NorthPole,"
		print "went to NewYork, ate spaghetti, worked in a shiny mail-room"
		print "and eventually"
		print "saved X-Mas."
		print "\n"
		print "This year once more, NewYorkCity lost its' faith in the magic of X-Mas"
		print "and Santa asks for help to rescue the Holidays."
		print "This time you get to slip into the role of Buddy the Elf"
		print "and convince the NewYorkers of the holiday spirit once again!"
		print "\n"
		print"Are you ready to start this journey"
		print"and take on the burden to save X-Mas?"
		print"I am ready! / I am so not ready for this."
		
		action = raw_input("> ")
		
		if action == "I am ready!":
			print "\n"
			print "Wonderful!"
			print "Then let's dive into the world of Buddy the Elf"
			print "and his friends."
			print "Your journey starts at the Northpole - duh."
			return 'Advice'
			
		elif action == "I am so not ready for this.":
			print "\n"
			print "I won't take no for an answer."
			print "Santa needs your help, so you have to do it anyway."	
			print " ¯\_('-')_/¯ "		
			return 'Advice'			

		else:
			print "Does not compute."
			return 'NorthPole'

class Advice(Scene):

	def enter(self):
		print "\n"
		print "A little piece of advice, before we start,"
		print "On your way, you'll encounter differnt"
		print "different quests."
		print "The answers to the questions won't always be obvious,"
		print "which is why I now you the chance of a little assistance:"
		print "I have prepared a manual of possible answers that you are"
		print "now able to open up and use for the game."
		print "Of course you are also free to do it the hard way and get to"
		print "the answers via trial and error."
		print "Just keep in mind, that the manual is a possibility."
		print "\n"
		print "So, do you want me to open up the manual?"
		print "YES / NO ?"
		
		action = raw_input("> ")
		
		if action == "YES":
			return 'Manual'
		else:
			return 'CandyCaneForest'
		
	
class Manual(Scene):

	def enter(self):
		print "\n"
		print "This is the Manual"
		print "It's a list of every computed answer in this game."
		print "Whenever you are stuck, you can scroll back up to this list and search for a solution."
		print "(It's alphabeticallly sorted, so don't you think it's in the right"
		print "chronological order - after all I don#t want it to be too easy either.)"
		print "\n"
		print "______________________________"
		print "\n"
		print "Don't you eat the yellow snow!"
		print "eat the gum"
		print "ignore gum"
		print "is singing loud for all to hear!"
		print "save for later"
		print "\n"
		print "______________________________"
		print "\n"
		print "If you are ready, type in 'start' and press enter:"
		action = raw_input("> ")
		
		if action == "start":
			return 'CandyCaneForest'
		else:
			print "Doesn't compute."
			return 'Manual'




class CandyCaneForest(Scene):

	def enter(self):
		print "\n"
		print "-Candycane-Forest-"
		print "Your journey begins in the Candycane-Forest,"
		print "a magical place , where there grow Candycanes instead of trees."
		print "In the middle of the Forest you encounter"
		print "Leon the Snowman"
		print "\n"
		print "Hey Buddy!"
		print "How are you today, my favourite Elf?"
		print "I know you are on your way to save X-Mas,"
		print "but before I can let you pass,"
		print "you have to answer me one question:"
		print "\n"
		print "What was the advice I gave you on your last journey?"
		print "\n"
		print "As I am generous today, you have got 3 guesses:"
		
		answer = "Don't you eat the yellow snow!"
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != answer and guesses < 2: 
			print "\n"
			print "Nope, try again."
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == answer:
			print "\n"
			print "Great Buddy!"
			print "I knew you listened to me."
			print "Good luck on your journey and remember,"
			print "Don't you eat the yellow snow! HO HO HO!"
			return 'GumDropSea'
		else:
			print "\n"
			print "I am disappointed in you."
			print "I said it two times in the movie Buddy,"
			print "TWO times!"
			print "I thought you would've listened more closely to what I've said."
			print "\n"
			print "Wether you like it or not, you can't continue this journey here."
			print "It's to dangerous for you to be out there,"
			print "if you can't even remember the simplest advice."
			return 'Loss'
		
		
		
		
class GumDropSea(Scene):

	def enter(self):
		print "\n"
		print "-Gumdrop-Sea-"
		print "You say good bye to Leon and pass the Candycane-Forest."
		print "As you walk through the forests huge Candycane-gate,"
		print "you come upon your next obstacle:"
		print "The Sea of twirly swirly Gumdrops!"
		print "On its' boarder, you find three ice floes"
		print "and Mr. Narwal right next to them."
		print "\n"
		print "Hey Bud! You see these 3 ice floes?"
		print "You need to decide which one you'll take."
		print "Tell me, is it 1, 2 or 3?"
		right_floe = randint(1,3)
		guess = raw_input("[floe #]>")
		
		if int(guess) != right_floe:
			print "\n"
			print "You jump onto floe number %s and push away from the land." % guess
			print "You already consider youself safe,"
			print "when suddenly the ice begins to break."
			print "You fall into the twirly, swirly Gumdrop-Sea"
			print "and Mr. Narwal has to get you out."
			print "Lying in the ground you are so confused by all the swirling"
			print "and twirling, that you are not able to continue your journey."
			return 'Loss'
		else:
			print "\n"
			print "You jump onto floe number %s and push away from the land." % guess
			print "After you float a few meters towards the horizon,"
			print "it's safe to say, that you chose the right floe."
			print "\n"
			print "Mr. Narwal waves goodbye in the distance"
			print "and you continue your journey."
			return 'LincolnTunnel'
			

		
		
class LincolnTunnel(Scene):

	def enter(self):
		print "\n"
		print "-Lincoln Tunnel-"
		print "Back again on mainland, you walked for a few miles"
		print "and survived a fight with an evil black Squirrel,"
		print "you come across he Lincoln Tunnel."
		print "The final stage before reaching New York!"
		print "You enter the tunnel and are already halway through,"
		print "when you see a chewing gum adhered to the ground, on the other side of the street."
		print "\n"
		print "What do you choose to do?"
		
		action = raw_input("> ")
		
		if action == "eat the gum":
			print "\n"
			print "Buddy you are beyond remedy."
			print "As you walk across the street"
			print "and bend down to pick up the gum,"
			print "a car hits you..."
			print "Just as a short reminder from the the movie:"
			print "USED GUM IS NOT TO BE EATEN!"
			print "Especially not from the street."
			return 'Loss'
		
		elif action == "ignore gum":
			print "\n"
			print "You keep on going"
			print "(although I can see that tempted look in your eyes)"
			print "and exit the tunnel on the other side."
			print "Well done,"
			print "only one quest is left!"
			return 'CentralPark'
		
		elif action == "save for later":
			print "\n"
			print "You keep on going"
			print "and exit the tunnel on the other side."
			print "You are good for now but PLEASE,"
			print "don't try to get that gum on your way back. "
			print "It's dangerous and just simply gross!"
			print "(And yes, maybe I am starting to like you,"
			print "after all this time we spent together"
			print "and don't want you to get hit by a car..."
			print "But don't tell anyone, I dare you!)"
			return 'CentralPark'
		
		else:
			print "\n"
			print "Wrong answer."
			print "Doesn't compute."
			print "(remember that there's still the option of jusing the manual)"
			print "(unless you already did use it and are even dumber than I thought."
			print "(In that case you're not worthy playing my precious game!)"
			return 'LincolnTunnel'
		
		
		
		
class CentralPark(Scene):

	def enter(self):
		print "\n"
		print "-Central Park-"
		print "As your last stage Buddy, you enter the Central Park."
		print "A place full of wonder and joy,"
		print "particularly in the X-Mas time."
		print "\n"
		print "You might wonder why there are so many people,"
		print "standing there, as if they're waiting for something."
		print "That was actually my doing. We need them after you complete"
		print "your part of the game." 
		print "I told them that there would be free food."
		print "Works marvelous, every time!"
		print "\n"
		print "Now Let's come to your last task to save X-Mas."
		print "Those people don't believe in Santa anymore,"
		print "So you need to tell me how to convince them"
		print "and regain their trust!"
		print "You only got one try"
		print "but this should be an easy one for you anyway: "
		print "\n"
		print "Complete the following quote:"
		print "The best way to spread X-Mas chear,..."
		
		action = raw_input("> ")

		if action == "is singing loud for all to hear!":
			print "\n"
			print "Exactly Buddy, let's do this!"
			print "\n"
			print "-Epilog-"
			print "At first, everyone looked a little bewildered,"
			print "but more and more people started to join in"
			print "in our beautiful (only slightly atonal) choir."
			print "Oh how I love X-Mas songs!"
			print "And the others seem to do so too - their faith is restored!"
			return 'Victory'
		
		else:
			print "\n"
			print "If you don't even know the most important quote"
			print "of the whole movie, than I don't want you to play my game."
			print "You have no idea of how sad I am right now..."
			return 'Loss'

class Victory(Scene):

	def enter(self):
		print "\n"
		print "You did it, you saved X-mas!"
		print "We are so proud of you."
		print "Hope you'll help us again next year!"
		print "Bye."
		print "\n"
		return 'NorthPole'		




class Map(object):

	scenes = {
		'NorthPole': NorthPole(),
		'CandyCaneForest': CandyCaneForest(),
		'GumDropSea': GumDropSea(),
		'LincolnTunnel': LincolnTunnel(),
		'CentralPark': CentralPark(),
		'Loss': Loss(),
		'Victory': Victory(),
		'Advice': Advice(),
		'Manual': Manual(),
		
	}
	
	
	

	def __init__(self, start_scene): 
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
		
		
a_map = Map('NorthPole')
a_game = Engine(a_map)
a_game.play()