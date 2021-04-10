"""
-------------------------------------------------------------------------------
Name:   dreamadventuregame.py
Purpose:  A game where you can choose your own path and find your dream
 
Author: Chan.E
 
Created:  25/03/2021
------------------------------------------------------------------------------
"""
#Background
print ("...Background information...")

print ("\nYou are a person who lucid dreams every night, one day you seemingly cannot control you dream. Instead of a bright blue sky that you've invisioned, you see a storm clouds and thunder. When you realize that nothing is going your way you suddenly get sucked into a black hole that appeared right behind you and you pass out....")

#instructions
print ("\n...Instructions...")
print ("\n1. You will be able to make your own choices throughout this game which will either kill you, survive to win")
print ("2. You will be able to interact with a certain character and ask them guided questions")
print ("3. *** means an action you are doing, --- is what your subconcious is telling you, <> is when you're speaking, <<>> is inner dialougue, and [] is author's P.O.V")
print ("4. Do not type in anything other than what is instructed (it will be in parenthesis), it will crash the game")
print ("6. When you die, you can choose to either quit the game or move onto the section. You will not be brought back to where you die")
print ("6. Do your best to survive and have fun!")

#Character introduction
print ("\n...Design your character...")
name = input("\nEnter name (no numbers): ")
gender = input("Enter Gender (she/he): ")
age = int(input("Enter Age: "))

#introduction
print ("\n...Game Starting...")

print ("\n***You have gone to bed****")

print ("\n---You have entered into your lucid dream---")

print ("\n<Finally, after such a long day I can go back to fruitsville, wait, why are there clouds? I hate rain!>")

print ("\n---Error, there has been a breach in the system, trying to access dream 1907... Error, there has been a breach in the system, trying to access dream 1907...---")

print ("\n<What? What's going on? What error? This is a dream not a video game>")

print ("\n---Black hole generating...Black hole generating...---")

print ("\n<What in the world is going on right now?>")

print ("\n***You have been sucked in the black hole***")

print ("\n---You have arrived in the waiting room---")

print ("\n???: <Welcome " + name + " to Hellsbane system, I am your guide Finona Brinswurth... a8dskajsbdoichajbcsa, buy supersocks for only $603.99 aksjda89984ajkbcak10jsb...How may I help you today?>")

#Question options
print ("\n1.")
print ("Who are you?")
print ("2.")
print ("Where am I?")
print ("3.")
print ("Why am I here?")
print ("4.")
print ("I'm sorry, what did you say about the supersocks?")
print ("5.")
print ("How do I get out of here?")
print ("6.")
print ("I don't need your help")

#Question responses
while True: 
  question = input("\nChoose an option above: ")
  if question == "6":
    print ("\nFinona: If there are no questions then please follow me to the first course.")
    break
  if question == "1":
   print ("\nFinona: My name is Finona Brinswurth, I am your guide for this course. Would you like to ask anything else?")
  if question == "2":
   print ("\nFinona: You are in Hellsbane system where you will go through courses and earn points. Would you like to ask anything else?")
  if question == "3":
   print ("\nFinona: You are here because of 1 or more of these 3 reasons, 1. You have signed up to be here, 2. Because your dream was interupted by an unknown force, 3. A person you know has chosen you to come here in replacement of them. Would you like to ask anything else?")
  if question == "4":
   print ("\nFinona: Error...question uncomprehendable... variable: 'supersocks' unidentified")
   print ("<Ok, no supersocks it is>")
  if question == "5":
   print ("\nFinona: You must go through 3 random courses , each one giving you certain amounts of points. survive and you will wake up and you won't have to come back to Hellsbane system ever again, fail any courses, and you die. Would you like to ask anything else?")

#First voyage prologue
print ("\n<<This is insane. Why would this happen in a dream? That lady was speaking like a robot for goodness sake!>>")

print ("\nFinona: The first course is quite difficult, you got quite unlucky pass rate is about 27.8%. It's based on luck and stamina. I wish you luck and I will be waiting for you on the other side.")

print ("\n<Wait, why can't I just come with you?>")

print ("\nFinona: Because you must complete the course, if you fail to do so or cheat in anyway, you, " + name + ", will disappear from this world forever.")

print ("\n<First, how do you know my name? And second, does that mean the 70% of people who didn't pass died?")

print ("\nFinona: Your name, age, and gender are all stored in our database. " + name + " is " + str(age) + " and identifies themselves as a " + gender + ". is there anything that needs to be corrected?")

print ("\n<Uh...no, I don't think so.>")

print ("\nFinona: Perfect, now, if you could step onto this platform, it should take you right into section 1. May the odds be ever in your favour.")

print ("<<Luck...stamina...I hope I have enough of those. Wait, she didn't even answer my second question, and was that a quote from the Hunger Games?>>")

#First voyage
print ("\n[Once you got on the platform it started rising slowly. Right before it reached the top you saw a giant maze with dead ends everywhere]")

print ("\n???: Welcome to the Maze of luck, here you will go through the maze while constantly running. There is only one path that is correct and there will be a total of 5 different path roads you can choose from. Just a small heads up, there will be a boulder chasing after you going at 7km/hour so make your decisions quick and wisely! Gate will be opening in 3...2...1...")

print ("\n[You heard a loud blearing and decided to run, thinking that it would be a waste of time trying to question the person on the speaker]")

print ("\n<<5 paths and only 1 right answer? There's no way, I can't even turn back because of that stupid boulder!>>")

print ("\n[You stopped your running when you saw your first crossway]")

print ("\nOk " + name + " think. Left, or right.")

#Magnificent Maze
live_die = input("\n(left or right): ")

if live_die == "left":
 print ("[You have chosen correctly and you are now on your way to your second path]")
else:
  print ("[You ran faster and faster hoping to get to the next path when you suddenly see a giant wall. It's a dead end. Right as you turn around, you see a giant boulder just about to crush you...")
  print ("\nYou have died")
  print ("\nGame Finished") 
 
live_die = input("\n(left or right): ")

if live_die == "left":
 print ("[You have chosen correctly and you are now on your way to your third path]")
else:
 print ("[You ran faster and faster hoping to get to the next path when you suddenly see a giant wall. It's a dead end. Right as you turn around, you see a giant boulder just about to crush you...")
 print ("\nYou have died")
 print ("\nGame Finished")

live_die = input("\n(left or right): ")

if live_die == "right":
 print ("[You have chosen correctly and you are now on your way to your fourth path]")
else:
 print ("[You ran faster and faster hoping to get to the next path when you suddenly see a giant wall. It's a dead end. Right as you turn around, you see a giant boulder just about to crush you...")
 print ("\nYou have died")
 print ("\nGame Finished")
 
print ("\n<Hold on...>")

print ("\n[You stop running for a moment to look at the crossway in front of you, you make out of what seems to be a poster, but something about it looked off to you. The corners of the poster kept glitching out as if it wasn't meant to be there and the person in the advertisment poster seemed to be staring right into you]")

print ("\nPoster: Get your free order of supersocks now at only $503.99")

print ("\n<What am I doing right now? The boulder's right behind me!>")

print ("\n[Just as you ran away, you could've sworn the poster's eyes were following you]")

live_die = input("\n(left or right): ")

if live_die == "left":
 print ("[You have chosen correctly and you are now on your way to your fifth path]")
else:
 print ("[You ran faster and faster hoping to get to the next path when you suddenly see a giant wall. It's a dead end. Right as you turn around, you see a giant boulder just about to crush you...")
 print ("\nYou have died")
 print ("\nGame Finished")

live_die = input("\n(left or right): ")

if live_die == "right":
 print ("[You have chosen correctly and you are headed to the exit]")
else:
 print ("[You ran faster and faster hoping to get to the next path when you suddenly see a giant wall. It's a dead end. Right as you turn around, you see a giant boulder just about to crush you...")
 print ("\nYou have died")
 print ("\nGame Finished")

#Second voyage prolouge
print ("\nFinona: Good job in completing your first course. You only have 2 left. The one you're about to take is quite easy with a pass rate of 87.2%. Both courses are going to based on knowledge rather than luck or physical abilities.")

print ("\n<<Haha... I'm so tired I can't even think striaght anymore and you want me to do a knowledge based obstacle? I might as well die at this point>>")

print ("\nFinona: Please step onto this platform. You will get to see the other courses that you missed as well as arriving at your current course in 5 minutes. Best of luck.")

print ("\n<<I wonder how bad other courses must be>>")

print ("\n[While going up you see a total of 20 different courses, one including the maze you just ran through. There was a lava lake with a bunch of objects floating on it, which you guessed to be a recreation of the popular game, the floor is lava. An actual obstacle course with ladders, crocodiles, monkey bars, and lots more. Underneath just seemed to be a void of nothingness. You shivered at the thought of that. You looked at each and every one of the courses and one particular one caught your eye. It was just a metal box. The bottom of the box constantly kept opening and closing and every time it opened you could make out a tiny speck falling out of it. At the bottom is what looked to be quicksand but the people were sinking way too fast for that too just be normal quicksand. Just as you were about to lean closer and get a better view, you arrived at your floor.]")

#Second voyage
print ("\n???: Greetings to the new challanger of our course, 'COMPLETE THAT FAMOUS PHRASE!' The rules are simple, you will be given half of the famous phrase and you must finish it! There is no time limit, however if you don't know it immediately, your probably don't know it at all.")

print ("\n<<Famous phrases, well that should be quite easy after all everyone should know these phrases if they're famous right?>>")

#Famous phrases
print ("\n???: Let's start easy! The first rule of Fight Club is...?")
quote_finisher = input("\nfinish the quote (no capitals or punctuation, I used the EXACT quotes from the source so make sure you don't miss anything): ")

if quote_finisher == "you do not talk about fight club":
  print ("\n???: DING DING DING, you are correct!")

else: 
  print ("\n???: Oops! Turns out you don't know it! Although you didn't talk about fight club, which is the first rule, that's not how the game works.")
  print ("\n[Just then, two giant arms grabbed you and injected something in your neck. You slowly started finding yourself fading away into darkness...")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: The next quote iiiisssss... Life is like a box of chocolates...")

quote_finisher = input("\nfinish the quote (no capitals or punctuation): ")

if quote_finisher == "you never know what you're going to get":
  print ("\n???: Two for two! You're on a roll " + name + "!")

else: 
  print ("\n???: Oops! Turns out you don't know it! Too bad, instead of chocolates you're just going to get poison. Maybe the afterlife will be more predictable for you.")
  print ("\n[Just then, two giant arms grabbed you and injected something in your neck. You slowly started finding yourself fading away into darkness...")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Ready for the next quote? Well it doesn't matter, I'm giving it to you anyway... The early bird...")

quote_finisher = input("\nfinish the quote (no capitals or punctuation): ")

if quote_finisher == "catches the worm":
  print ("\n???: Correct! You're getting closer to the end.")

else: 
  print ("\n???: Err, err. Guess you don't catch the worm.")
  print ("\n[Just then, two giant arms grabbed you and injected something in your neck. You slowly started finding yourself fading away into darkness...")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: To infinity...")

quote_finisher = input("\nfinish the quote (no capitals or punctuation): ")

if quote_finisher == "and beyond":
  print ("\n???: You definitely went BEYOND my expectations!")

else: 
  print ("\n???: Unfortunetly you didn't go beyond the expectations.")
  print ("\n[Just then, two giant arms grabbed you and injected something in your neck. You slowly started finding yourself fading away into darkness...")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: The last and final quote is...Ignorance is...?")

quote_finisher = input("\nfinish the quote (no capitals or punctuation): ")

if quote_finisher == "bliss":
  print ("\n???: Well you're not ignorant, although living a little longer is great!")

else: 
  print ("\n???: Too bad! Instead of bliss, you just got death!")
  print ("\n[Just then, two giant arms grabbed you and injected something in your neck. You slowly started finding yourself fading away into darkness...")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Woohoo! You just completed course #2. Please step on the platform to bring you down to your guide.")

print ("\n[You sigh in relief as you made your way down to Finona]")

print ("\n<Just one more, one more " + name + ". You can get out of here>")

print ("\n[Just as you look up, you see Finona's face, she's looks at you and starts heading in your direction]")

#Third voyage prolougue 
print ("\n<That was easy, nice change of pace from the first obstacle>")

print ("\nFinona: Glad you think so. Unfortunetly the third stage is extremely difficult so you might want to say your prayers now.")

print ("\n<What do you mean?>")

print ("\nFinona: You might've missed it on your way to the second stage but that metal box?")

print ("\n[She pointed to the large metal box that you took notice of before]")

print ("\nFinona: That is where you'll be heading. With a average pass rate of 5%, you'll likely die, that is, only if you don't know random facts.")

print ("\n<What do you mean?>")

print ("\nFinona: The box contain a game like trivia. Random facts that not many people know. Many people struggle to know the facts that the box asks. If you fail, you will be dropped 100m into quicksand  and then proceed to be grinded by a grinder. Your flesh will be fed to the crocodiles that reside in the obstacle course.")

print ("\n<<Oh god...I'm not surviving am I? This place is practically forcing me to die>>")

print ("\nFinona: Here we are. As always, the platform will bring you to your destination. I hope for your safe arrival on the other side.")

#Third voyage
print ("\n???: OH HERE " + gender + " COMES! Our 40th contestant today! Everyone round of applause for " + name + " Let's hope they pass!")

print ("\n<<What's going on? There are other people here too now?>>")

print ("\n[Just as you were about have a mental breakdown a girl around your age came up to you]")

print ("\n???: Did you get forced to come here too?")

print ("\n<I'm not sure...I was about to go into my lucid dream and suddenly there was a black hole behind me>")

print ("\n???: A black hole? Never heard of that one before. Well I'm Kriston, my parents wanted me to come in place of them since they were too scared.")

print ("\n<Oh, that's horrible, sorry you have to deal with this>")

print ("\nKriston: Oh yeah for sure! You know that I've been here for over 2 hours and out of the 33 people that have gone, no one passed?The farthest one person has gone is to the fourth question, and there's 5 of them!")

print ("\n[Kriston continued to giggle as if the fact that 33 people becoming crocodile feed is funny. You have concluded that it would be best to stay away from her]")

print ("\nKriston: Oh make sure you pay attention to the questions they ask. Although it's rare, they might re-ask some questions!")

print ("\n<Ok that's kinda useful, but I think I ran out of luck for today. The stupid maze used it all up>")

print ("\n???: Contestant 40! Please make your way up to the podium!")

print ("\nKriston: Before you go, would you like to buy this wonderful pair of supersocks? They're only $403.99")

print ("\n<<Wait, supersocks? Why does everyone keep mentioning that...>>")

print ("[Before you got to ask her more, you saw that the box started turning into multiple colours, almost like a glitch. Something didn't feel right with you and you knew you had to get of this dream quickly. You ran up to where the person first called you and before you entered the room, you turned back to look at Kriston. She was looking right back at you with a sinister smile]")

#Trivia Time
print ("\n???: Let's not waste any time and give out the questions. The crocs are getting hungerier by the second.")

print ("<Well that's reassuring>")

print ("\n???: First question, what animal was arrested by the Nigerian Police due to the suspicion of attempted robbery in 2009? ")

print ("a. a dog")
print ("b. a cat")
print ("c. a goat")
print ("d. a bird")

answer = input("\nChoose an option above (just the letter): ")
if answer == "c":
  print ("\n???: Correct.")

else: 
  print ("???: What a fruitless struggle, release the lever.")
  print ("[Just then the ground below you gave way and you feel yourself suffocating in the sand]")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Second question, on average, how many turkeys are killed each year for thanksgiving?")

print ("a. 100 thousand")
print ("b. 10 million")
print ("c. 34 million")
print ("d. 46 million")

answer = input("\nChoose an option above (just the letter): ")
if answer == "d":
  print ("\n???: Correct yet again.")

else: 
  print ("???: As expected, not worth any more than just croc fodder, release the lever.")
  print ("[Just then the ground below you gave way and you feel yourself suffocating in the sand]")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Third question, what can you NOT buy from ikea?")

print ("a. food")
print ("b. a house")
print ("c. furniture")
print ("d. vaseline")

answer = input("\nChoose an option above (just the letter): ")
if answer == "d":
  print ("\n???: I'm surprised.")

else: 
  print ("???: What a waste of time, release the lever.")
  print ("[Just then the ground below you gave way and you feel yourself suffocating in the sand]")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Fourth question, on average, how many deaths are prevented due to vaccines?")

print ("a. 2.5 million")
print ("b. 2 million")
print ("c. 3 million")
print ("d. 1.5 million")

answer = input("\nChoose an option above (just the letter): ")
if answer == "a":
  print ("\n???: So you do know quite a bit information...")

else: 
  print ("???: Bring in the next person, release the lever.")
  print ("[Just then the ground below you gave way and you feel yourself suffocating in the sand]")
  print ("\nYou have died")
  print ("\nGame finished")

print ("\n???: Last question, how much of the Sahara Desert is sand?")

print ("a. 25%")
print ("b. 50%")
print ("c. 80%")
print ("d. 70%")

answer = input("\nChoose an option above (just the letter): ")
if answer == "a":
  print ("\n???: Colour me surprised. Guess you're pretty knowledgable.")

else: 
  print ("???: So much time was wasted because of you, in fact, just jump in yourself for being a nuisance.")
  print ("[You see a part of the floor collapsed and everyone was looking at you. You take a deep breath and jump in, hoping that you die before you suffocate]")
  print ("\nYou have died")
  print ("\nGame finished")

#Finally the end... or is it?
print ("\n???: Please head back to your guide...Contestant 41 please make your way to the podium.")

print ("\n <<I thought I was going to die, I had to guess for one of them, thank god I'm not dead>>")

print ("\n [Just as you were about to rejoice you see the world around the box start shaking, something doesn't feel right to you. You grab Finona's hand and start running]")

print ("\n Finona: Where and why are you running?")

print ("\n <I don't know, just lead me to where I can exit this cursed dream, fast>")

print ("\n Finona: You're heading the right direction, just keep going straight and go into the blackhole. You should be able to wake up right after.")

print ("\n [Right as you reached the blackhole you gulped. It looked sketchy but right now, everything is too colourful and it's just getting worse. Closing your eyes, you jump into the hole]")

print ("\n [You woke up with a start, your head hitting something hard]")

print ("\n ???: Oh my god " + name + " I thought you were as good as dead in there!")

print ("\n [You look at your surroundings and notice that you're in a capsule wearing a helmet that was way too tight for your head. Outside you see a male around your age wearing a lab coat]")

print ("\n <What's going on? Where am I? Who are you?>")

print ("\n ???: I'm Harrison, I was in charge of the testing for the new V.R. coming out and you volunteered to be the tester. DO you remember anything? Feel any side affects?")

print ("\n <My memory is a bit fuzzy and I have a massive headache. Other than that, nothing>")

print ("\n Harrison: That's good, you can come out now, I'll explain the situation over food.")

print ("\n...Time skip...")

print ("\n <So basically, there's a new V.R., I tested it, someone hacked it, and I barely made it out alive before someone tried to infect my mind>")

print ("\n Harrison: That basically summed it up")

print ("\n <Did you find who did it?>")

print ("\n <They're still investigating it but it won't be long until the police find them>")

print ("\n <That's a relief>")

print ("\n [You finished your sandwich and made your way over to the garbage can. Before you could throw it out a sign caught your eye. It said, 'Come buy these super cheap supersocks for only $100.99!' You gasped as you tried to warn Harrison but as you turned around you came face to face with Kriston]")

print ("\n Kriston: You know...it's rude to ignore someone and go running off.")

print ("[The last thing you heard was cackling and the world went dark...]")

print ("\n GAME END")

print ("\n.")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print (".")
print ("...or is it?")