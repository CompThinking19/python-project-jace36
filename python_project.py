# -*- coding: utf-8 -*-
#I added this cause I kept getting errors for line 59 about non-ascii characters

#Intro screen
print("Welcome to Survive the Night");
#I'm not exactly sure if this is how you create a choose your own adventure game, but a model I saw online had a similiar looking code, so hopefully they did it right?? And I didn't type out all of this for nothing

#Starter Screen
while True:
    starting_question_1= raw_input('Ready to play?: ')
    if starting_question_1=='yes':
        print('Let us begin')
        break
#After saying yes, players get to create their character and has to choose between male or female
#Yet, if the player tries to pick male, it won't work, so they have no choice but to pick female
#I have no idea how to do that yet though, I think I just use a typeError, but not a hundred percent sure yet
#But I'll ignore it for now since this is fine
name= raw_input('Enter a female name for your character: ')
#after naming their character, the game starts

#Level 1
print("It was just your average Thursday night. You got out of work an hour ago and you were able to pick up some groceries for the weekend. After putting your groceries away, you settle on the couch and turn on the TV. However, you don't know what you want to watch.")
while True:
    question_1= raw_input('Should you watch a Comedy or a Thriller?')
    if question_1=='Comedy':
        print('You put on Brooklyn Nine Nine')
        break
    elif question_1=='Thriller':
        print('You put on Stranger Things')
        break
#This section just gives players an idea of what the game is going to be like from here on out.
#Although this won't show that every choice in this game has a consequence or a certain outcome, it just offers an idea of what to expect.
print("You get through ten minutes of your show, before you here a noise upstairs")
while True:
    question_2= raw_input('Ignore the noise or Investigate the noise?')
    if question_2=='Ignore the noise':
        print('You decide to ignore the noise, but it seems to get louder and louder. So, you decide to investigate after all')
        break
#The character will have to investigate no matter what, since if they didn't this would be a very short level
    elif question_2=='Investigate the noise':
        print('You decided to investigate the noise. As you got closer to the stairs, you start to distinct footsteps upstairs.')
        break
#this next set of questions will open up a little sub option that can help the player later on in the game, but if they decide not to grab anything right now, the items will still be there for them later on
print('You stop in the hallway near your front door, your stairs are right there, but you feel nervous. You wonder if you should grab something to defend yourself or just keep going.')
item_Keys = False
item_Spray = False
#this allows me to make sure the code remembers that the players pick up the items
item_scene = True
while item_scene == True:
    question_3= raw_input('Should you Grab Something or Keep Going?')
    if question_3=='Grab Something':
        print('You decided to grab something, you see your keys and your pepper spray on the hallway table.')
        while True:
            question_3a= raw_input('Do you Grab your Keys or Grab your Spray?' )
            if question_3a=='Grab your Keys':
                print('You grabbed the Keys and left the Spray behind')
                item_Keys = True
                item_scene = False
                break
            elif question_3a=='Grab your Spray':
                print('You grabbed the Spray and left the Keys behind')
                item_Spray = True
                item_scene = False
                break
#the player will be able to pick up items at this point, but if they use the items, they will not be able to use it later in the game
#Items are only supposed to be used once
    elif question_3=="Keep Going":
        print('You decided to keep going. ')
        item_scene = False
        break

print('You made it to the foot of your stairs and you look at the top of the steps. You see a figure standing at the top.')
attacker_scene = True
while attacker_scene == True:
    question_4= raw_input('Turn on the Lights or Run?')
    if question_4=='Turn on the Lights':
        print('You turn on the lights and you see a man at the top of the stairs. He is concealing his face, but you have a feeling that you know him. Should you yell at him, attempting to scare him away, or run towards the front door')
        while attacker_scene == True:
            question_4a= raw_input('Yell or Run?')
            if question_4a=='Yell':
                print('You yelled at the man, screaming at him to get out of your house. The man did not move, your threat meant nothing. So, you decided to run afterall. The man jumped down the stairs and chased after you. But you are able to see your path clearly since the light is on, so thankfully you do not trip.')
                #I know this takes away from the whole consequence thing, but I didn't know what else to do here to get the story going....
                #besides in horror movies, yelling doesn't really stop killers from doing what they're going to do
                attacker_scene = False
                break
            elif question_4a=='Run':
                print('You ran for the door, but the man jumped down the stairs and chased after you. But, you are able to see your path clearly since the light is on, so thankfully you do not trip.')
                attacker_scene = False
                break
    elif question_4=='Run':
        print('You ran for the door, but the man jumped down the stairs and chased after you. However, since you left the lights off, you are unable to see where you are going. You end up tripping on something as you are trying to rush out of the house. The figure is getting closer and is about to jump on you to stop you from getting up.')
        while attacker_scene == True:
            question_4b=raw_input('Get up or Roll away?')
            if question_4b =='Get up':
                print('You tried to get up quickly, but were not fast enough. The figure was able to tackle you before you could.Your attacker puts all their weight on you, and you cannot breathe. You have to act fast!')
                while attacker_scene == True:
                    if item_Keys:
                        question_4ba=raw_input('Scream, Knee your Attacker, or Use your Keys?')
                    elif item_Spray:
                        question_4ba=raw_input('Scream, Knee your Attacker, or Use your Spray?')
                    else:
                        question_4ba=raw_input('Scream or Knee your Attacker?')
                    if question_4ba=='Scream':
                        print('Screaming does nothing and you eventually pass out from the lack of air.')
                        attacker_scene = False
                        exit("You lost consciousness. End of Level 1")
                        #this allows me to end the game at this point and shows that the player made the wrong choice
                        break
                #Level 1 will end if you choose this option
                #makes of for the consequences that yelling didn't have if you turned on the lights
                    elif question_4ba=='Knee your Attacker':
                        print('You are able to lift your knee up hard. Your attacker wheezes in pain and rolls off of you. You are able to get up, and run to the door.')
                        attacker_scene = False
                        break
                        #In self defense classes, they said to always use your elbow or knee when going against your attackers
                        #I was going to do elbow since that is the strongest joint, but this seemed more like a natural to get out of this situation
                    elif item_Keys and question_4ba == 'Use your Keys':
                        print('You used your keys and stabbed your attacker. Your attacker screamed in pain, using his pain to your advantage, you push him off of you. In the struggle, you ended up dropping your keys. But, you were able to get up, and run to the door.')
                        attacker_scene = False
                        break
                    elif item_Spray and question_4ba == 'Use your Spray':
                        print('You used your spray. You sprayed your spray in your attackers face. Your attacker screamed in pain, using his pain to your advantage, you push him off of you. In the struggle, you ended up dropping your spray. But, you were able to get up, and run to the door.')
                        attacker_scene = False
                        break
                    #If I did this correctly, the code will remembered that you picked up one of the items and gives you the chance to use it here.
            elif question_4b=='Roll away':
                print('Your attacker attempts to tackle you, but you are able to roll the other way as they fall to the floor. You are able to get up faster than your attacker, so you head towards the door again.')
                attacker_scene = False
                break

print('You were able to get to the door and pull the door open. You ran outside in the pitch black. Your neighbors right next door are friendly and always leave their back door unlock in case their kids get locked out. But, your car is closer.')
final_scene = True
while final_scene == True:
    question_5= raw_input('Do you Run to your Neighbors or Run to your Car?')
    if question_5=='Run to your Neighbors':
        print('You run to your neighbor, your hear your attacker exiting your house. You start to run a little faster. You get to the back door and it is locked. You forgot that they went out of town for the weekend. You turn to run away, but it’s too late. While you were trying to open the door, your attacker came up behind you. All you saw was him moving his arm down and the moon shining in his eyes. Then, everything goes dark. ')
        final_scene = False
        exit("You lost consciousness. End of Level 1")
        break
    elif question_5=='Run to your Car':
        if item_Keys:
            print('You run to your car, you hear your attacker exiting your house. You got to your door and tried to open the door. Your car is locked. However, you picked up your keys earlier. You quickly unlock the door, get in, and locked the door before your attacker could get you. You attacker bangs on the window, but then turns around and heads back into the house. You have to think fast.')
            question_5a = raw_input('Turn your Car on or Hide in your Car?')
            if question_5a == 'Turn your Car on':
                print('You put your keys in the ignition and started your car. At least you tried to. Your engine starts to stall. You keep trying. You see your attacker approaching your car. He has the baseball bat that you keep in your bedroom. You keep trying. He starts to swing the bat at your side window. The glass breaks completely. Your attacker grabs you by the hair and drags you out of the car. You look up and see your attacker bring the bat down. Everything goes dark.')
                final_scene = False
                exit("You lost consciousness. End of Level 1")
                break
                #Again, if I did this right, you'll be able to access these side choices if the character picked up the keys at the begining and didn't use them earlier
            elif question_5a == 'Hide in your Car':
                print('You decided to hide and wait for help. You maneuvered yourself to the backseat, to hid. You wait and listen. You hear footsteps and see your attacker at the driver side window. He has the bat you keep in your bedroom. He swings at the window. The window breaks and he unlocks the doors. He opens the backseats doors and drags you out by your feet. You fall to the ground and look up. You see your attacker bringing the bad down. Everything goes dark.')
                final_scene = False
                exit("You lost consciousness. End of Level 1")
                break
                #I know this doesn't seem realistic, but sometimes is stressful situations like this, some people just think its smart to hide out
                #I will probably end up changing this eventually, but for now it is fine.
        print('You run to your car, you hear your attacker exiting your house. You got to your door and tried to open the door. But you cannot get it opened. Your car is locked. Your attacker comes up behind you, you see him through the reflection of your window. You try to move away, but he grabs the back of your head. Then everything goes dark. ')
        final_scene = False
        exit("You lost consciousness. End of Level 1")
        break
#End of Level One, and hopefully there will be a level 2 one day.
