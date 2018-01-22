#-*- coding: utf-8 -*-
class Scene(object):

	def __init__(self, title, urlname, description):
		self.title = title
		self.urlname = urlname
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		default_direction = None
		if '*' in self.paths.keys():
			default_direction = self.paths.get('*')
		return self.paths.get(direction, default_direction)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
		
# PART 1 - scenes of the game

start_point = Scene("Start", "north_pole",
"""
This is Buddy the Elf: Save X-Mas (again)
a game about a fictional - tho we all know it's true - story,
about an adopted Elf named Buddy, who was raised in the NorthPole,
went to NewYork, ate spaghetti, worked in a shiny mail-room
and eventually
saved X-Mas.

This year once more, New York City lost its' faith in the magic of X-Mas
and Santa asks for help to rescue the Holidays.
This time you get to slip into the role of Buddy the Elf
and convince the NewYorkers of the holiday spirit once again!

Are you ready to start this journey
and take on the burden of saving X-Mas?
Yes or No?
""")

np_ready = Scene("Northpole", "np_ready",
"""
Wonderful!
Then let's dive into the world of Buddy the Elf
and his friends.
Your journey starts at the Northpole - duh.
(say: 'continue')
""")

np_not_ready = Scene("Northpole", "np_not_ready",
"""
I won't take no for an answer.
Santa needs your help, so you have to do it anyway.
				
(say: 'continue')
""")

little_advice = Scene("Advice", "little_advice",
"""
A little piece of advice, before we start,
On your way, you'll encounter differnt quests.
The answers to the questions won't always be obvious,
which is why I now you the chance of a little assistance:
I have prepared a manual of possible answers that you are
now able to open up and have a quick look at.

Of course you are also free to do it the hard way and get to
the answers via trial and error.
Just keep in mind, that the manual is a possibility.

You also have the possibility to type in 'clue' at every scene,
to receive a tip on what the answer might be
or 'help', to get the right answer directly presented to you.

So, do you want me to open up the manual?
Yes / No ?
""")

helping_manual = Scene("Manual", "helping_manual", 
"""
This is the Manual
It's a list of every computed answer in this game.
Whenever you are stuck, you can scroll back up to this list and search for a solution.
(It's alphabeticallly sorted, so don't you think it's in the right
chronological order - after all I don#t want it to be too easy either.)

________________________________________________________________________________________

Dont you eat the yellow snow!
eat the gum
Floe No. 3
ignore gum
is singing loud for all to hear!
save for later
		

_________________________________________________________________________________________

If you are ready, type in 'start' and press enter:
""")

candy_cane_forest = Scene("CandyCaneForest", "candy_cane_forest",
"""
Let's get right to it!

-Candycane-Forest-

Your journey begins in the Candycane-Forest,
a magical place , where there grow Candycanes instead of trees.
In the middle of the Forest you encounter
Leon the Snowman

Hey Buddy!
How are you today, my favourite Elf?
I know you are on your way to save X-Mas,
but before I can let you pass,
you have to answer me one question.

BUT be careful, you only got one chance:

What was the advice I gave you on your last journey?
""")

ccf_end = Scene("End", "ccf_end",
"""
I am disappointed in you.
I said it two times in the movie Buddy,
TWO times!"
I thought you would've listened more closely to what I've said.

Wether you like it or not, you can't continue this journey here.
It's to dangerous for you to be out there,
if you can't even remember the simplest advice.

________________________________________________________________________________________

You lost.
Santa won't be able to deliver the gifts,
so we won't be able to celebrate X-Mas this year
and it's all your fault!
We trusted you, you impostor...
""")

ccf_help = Scene("Help", "ccf_help",
"""
The right answer is: 
Dont you eat the yellow snow!

('continue')
""")

ccf_clue = Scene("Help", "ccf_clue",
"""
It is an advice your parents give to you when you are little,
it has to do with dogs peeing in the snow in the winter
and what you shouldn't do afterwards...

('continue')
""")

gum_drop_sea = Scene("GumDropSea", "gum_drop_sea",
"""
Great Buddy!
I knew you listened to me.
Good luck on your journey and remember,
Don't you eat the yellow snow! HO HO HO!


-Gumdrop-Sea-


You say good bye to Leon and pass the Candycane-Forest.
As you walk through the forests huge Candycane-gate,
you come upon your next obstacle:
The Sea of twirly swirly Gumdrops!
On its' boarder, you find three ice floes
and Mr. Narwal right next to them.

Hey Bud! You see these 3 ice floes?
You need to decide which one you'll take.
Tell me, is it 1, 2 or 3?
""")

gds_end = Scene("End", "gds_end",
"""
You jump onto the floe and push away from the land.
You already consider youself safe,
when suddenly the ice begins to break.
You fall into the twirly, swirly Gumdrop-Sea
and Mr. Narwal has to get you out.
Lying in the ground you are so confused by all the swirling
and twirling, that you are not able to continue your journey.

________________________________________________________________________________________

You lost.
Santa won't be able to deliver the gifts,
so we won't be able to celebrate X-Mas this year
and it's all your fault!
We trusted you, you impostor...
""")

gds_help = Scene("Help", "gds_help",
"""
The right answer is:
3

('continue')
""")

gds_clue = Scene("Help", "gds_clue",
"""
What makes 2 + 5 - 2 x 2 + 6 - 7 + 1?

('continue')
""")

lincoln_tunnel = Scene("Lincoln Tunnel", "lincoln_tunnel",
"""
You jump onto floe number 3 and push away from the land.
After you float a few meters towards the horizon,
it's safe to say, that you chose the right floe.

Mr. Narwal waves goodbye in the distance
and you continue your journey.


-Lincoln Tunnel-


Back again on mainland, you walked for a few miles
and survived a fight with an evil black Squirrel,
you come across he Lincoln Tunnel.
The final stage before reaching New York!
You enter the tunnel and are already halway through,
when you see a chewing gum adhered to the ground, on the other side of the street.
What do you do now?
""")

lt_end = Scene("End", "lt_end",
"""
Buddy you are beyond remedy.
As you walk across the street
and bend down to pick up the gum,
a car hits you...
Just as a short reminder from the the movie:

USED GUM IS NOT TO BE EATEN!

Especially not from the street...

________________________________________________________________________________________

You lost.
Santa won't be able to deliver the gifts,
so we won't be able to celebrate X-Mas this year
and it's all your fault!
We trusted you, you impostor...
""")

lt_help = Scene("Help", "lt_help",
"""
The right answers are: 
ignore gum
OR
save gum

'eat gum' will kill you

('continue')
""")

lt_clue = Scene("Help", "lt_clue",
"""
You've got two possibilities to choose from and
neither one is eating the gum. That would kill you.

One includes seeing the gum again later...
The other one would be leaving the gum forever...
only differntly frased.

('continue')
""")

central_park_one = Scene("Central Park", "central_park_one",
"""
You keep on going
(although I can see that tempted look in your eyes)
and exit the tunnel on the other side.
Well done,
only one quest is left!


-Central Park-


As your last stage Buddy, you enter the Central Park.
A place full of wonder and joy,
particularly in the X-Mas time.

You might wonder why there are so many people,
standing there, as if they're waiting for something.
That was actually my doing. We need them after you complete
your part of the game.
I told them that there would be free food.
Works marvelous, every time!

Now Let's come to your last task to save X-Mas.
Those people don't believe in Santa anymore,
So you need to tell me how to convince them
and regain their trust!
You only got one try
but this should be an easy one for you anyway: 

Complete the following quote:
The best way to spread X-Mas chear...
""")

central_park_two = Scene("Central Park", "central_park:_two",
"""
You keep on going
and exit the tunnel on the other side.
You are good for now but PLEASE,
don't try to get that gum on your way back. 
It's dangerous and just simply gross!
(And yes, maybe I am starting to like you,
after all this time we spent together
and don't want you to get hit by a car...
But don't tell anyone, I dare you!)


-Central Park-


As your last stage Buddy, you enter the Central Park.
A place full of wonder and joy,
particularly in the X-Mas time.

You might wonder why there are so many people,
standing there, as if they're waiting for something.
That was actually my doing. We need them after you complete
your part of the game.
I told them that there would be free food.
Works marvelous, every time!

Now Let's come to your last task to save X-Mas.
Those people don't believe in Santa anymore,
So you need to tell me how to convince them
and regain their trust!
You only got one try
but this should be an easy one for you anyway: 

Complete the following quote:
The best way to spread X-Mas chear...
""")

cp_end = Scene("End","cp_end",
"""
If you don't even know the most important quote
of the whole movie, than I don't want you to play my game.
You have no idea of how sad I am right now...

________________________________________________________________________________________

You lost.
Santa won't be able to deliver the gifts,
so we won't be able to celebrate X-Mas this year
and it's all your fault!
We trusted you, you impostor...
""")

cpo_help = Scene("Help", "cpo_help",
"""
The right answer is:
is singing loud for all to hear!

('continue')
""")

cpo_clue = Scene("Help", "cpo_clue",
"""
first word: 'is'
second and third word: what you do under the shower
fourth word: 'for'
fifth word: synonym for everybody
6th, 7th word: What you don't want them to do, while you do what you do under the shower

('continue')
""")

cpt_help = Scene("Help", "cpt_help",
"""
The right answer is:
is singing loud for all to hear!

('continue')
""")

cpt_clue = Scene("Help", "cpt_clue",
"""
first word: 'is'
second and third word: what you do under the shower
fourth word: 'for'
fifth word: synonym for everybody
6th, 7th word: What you don't want them to do, while you do what you do under the shower

('continue')
""")

you_win = Scene("Victory", "you_win",
"""
Exactly Buddy, let's do this! Let's spread X-Mas chear!


-Epilog-


At first, everyone looked a little bewildered,
but more and more people started to join in
in our beautiful (only slightly atonal) choir.
Oh how I love X-Mas songs!
And the others seem to do so too - their faith is restored!

You did it, you saved X-mas!
We are so proud of you.
Hope you'll help us again next year!

""")


#PART 2 - the action commands 

cpt_help.add_paths({
    'continue': central_park_two
})
cpo_help.add_paths({
    'continue': central_park_one
})

lt_help.add_paths({
    'continue': lincoln_tunnel
})

gds_help.add_paths({
    'continue': gum_drop_sea
})

ccf_help.add_paths({
    'continue': candy_cane_forest
})
cpt_clue.add_paths({
    'continue': central_park_two
})
cpo_clue.add_paths({
    'continue': central_park_one
})

lt_clue.add_paths({
    'continue': lincoln_tunnel
})

gds_clue.add_paths({
    'continue': gum_drop_sea
})

ccf_clue.add_paths({
    'continue': candy_cane_forest
})

central_park_two.add_paths({
    'is singing loud for all to hear!': you_win,
    '*': cp_end,
    'help': cpo_help,
    'clue': cpo_clue
})

central_park_one.add_paths({
    'is singing loud for all to hear!': you_win,
    '*': cp_end,
	'help': cpt_help,
	'clue': cpt_clue
})

lincoln_tunnel.add_paths({
    'eat gum': lt_end,
    'ignore gum': central_park_one,
    'save gum': central_park_two,
    'help': lt_help,
    'clue': lt_clue
})

gum_drop_sea.add_paths({
    '3': lincoln_tunnel,
    '*': gds_end,
    'help': gds_help,
    'clue': gds_clue
})

candy_cane_forest.add_paths({
    'Dont you eat the yellow snow!': gum_drop_sea,
    '*': ccf_end,
    'help': ccf_help,
    'clue': ccf_clue
})

helping_manual.add_paths({
    'start': candy_cane_forest
})

little_advice.add_paths({
    'Yes': helping_manual,
    'No': candy_cane_forest
})

np_not_ready.add_paths({
    'continue': little_advice
})

np_ready.add_paths({
    'continue': little_advice
})

start_point.add_paths({
    'Yes': np_ready,
    'No': np_not_ready
})

#PART 3 - Variables
SCENES = {
    start_point.urlname : start_point,
    np_ready.urlname : np_ready,
    np_not_ready.urlname : np_not_ready,
    little_advice.urlname : little_advice,
    helping_manual.urlname : helping_manual,
	candy_cane_forest.urlname : candy_cane_forest,
    gum_drop_sea.urlname : gum_drop_sea,
    lincoln_tunnel.urlname : lincoln_tunnel,
    central_park_one.urlname : central_park_one,
    central_park_two.urlname : central_park_two,
    ccf_end.urlname : ccf_end,
    gds_end.urlname : gds_end,
    lt_end.urlname : lt_end,
    cp_end.urlname : cp_end,
    you_win.urlname : you_win,
    cpt_help.urlname : cpt_help,
    cpo_help.urlname : cpo_help,
    lt_help.urlname : lt_help,
    gds_help.urlname : gds_help,
    ccf_help.urlname : ccf_help,
    cpt_clue.urlname : cpt_clue,
    cpo_clue.urlname : cpo_clue,
    lt_clue.urlname : lt_clue,
    gds_clue.urlname : gds_clue,
    ccf_clue.urlname : ccf_clue
    
}
START = start_point
BACKGROUND = "northpole.jpg" 