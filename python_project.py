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
name= raw_input('Enter a female name for your character: ')
#after naming their character, the game starts

#LEvel 1
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
#The character will have to investigate no matter what, so I need to figure out a way to link the investigating steps to the ignore step after the last line is printed
    elif question_2=='Investigate the noise':
        print('You decided to investigate the noise. As you got closer to the stairs, you start to distinct footsteps upstairs.')
        break
#this will open up a little sub option that can help the player later on in the game, but if they decide not to grab anything to defend right now, the items  will still be there for them later on
print('You stop in the hallway near your front door, your stairs are right there, but you feel nervous. You wonder if you should grab something to defend yourself or just keep going.')
while True:
    question_3= raw_input('Should you Grab Something or Keep Going?')
    if question_3=='Grab Something':
        print('You decided to grab something, you see your keys and your pepper spray on the hallway table.')
        while True:
            question_3a= raw_input('Do you Grab your Keys or Grab your Spray?' )
            if question_3a=='Grab your Keys':
                print('You grabbed the Keys and left the Spray behind')
                break
            elif question_3a=='Grab your Spray':
                print('You grabbed the Spray and left the Keys behind')
                break
#I need to figure out how to link this to keep going after making the choice of bringing something along. I'm not sure if I have to create a whole new option in order to ensure that the player has the item they grabbed or just link it to the keep going and the code will just remember that you have an item
#Both of these choices will affect the character latter on, but they can never pick up the other item later on in the game
#However, if the player didn't pick them when they could, they'll have another chance to grab one of them later on...Maybe, haven't decided yet.
    elif question_3=="Keep Going":
        print('You decided to keep going. ')
        break
print('You made it to the foot of your stairs and you look at the top of the steps. You see a figure standing at the top. Do you turn on the lights or run?')
attacker_scene = True
while attacker_scene == True:
    question_4= raw_input('Turn on the Lights or Run?')
    if question_4=='Turn on the Lights':
        print('You turn on the lights and you see a man at the top of the stairs. He is concealing his face, but you have a feeling that you know him. Should you yell at him, attempting to scare him away, or run towards the front door')
        while attacker_scene == True:
            question_4a= raw_input('Yell or Run?')
            if question_4a=='Yell':
                print('You yelled at the man, screaming at him to get out of your house. The man did not move, your threat meant nothing. So, you decided to run afterall. The man jumped down the stairs and chased after you. But you are able to see your path clearly since the light is on, so thankfully you do not trip.')
                attacker_scene== False
                break
            elif question_4a=='Run':
                print('You ran for the door, but the man jumped down the stairs and chased after you. But, you are able to see your path clearly since the light is on, so thankfully you do not trip.')
                attacker_scene== False
                break
    elif question_4=='Run':
        print('You ran for the door, but the man jumped down the stairs and chased after you. However, since you left the lights off, you are unable to see where you are going. You end up tripping on something as you are trying to rush out of the house. The figure is getting closer and is about to jump on you to stop you from getting up.')
        while attacker_scene == True:
            question_4b=raw_input('Get up or Roll away?')
            if question_4b =='Get up':
                print('You tried to get up quickly, but were not fast enough. The figure was able to tackle you before you could.Your attacker puts all their weight on you, and you cannot breathe. You have to act fast!')
                while attacker_scene == True:
                    question_4ba=raw_input('Scream or Knee your Attacker?')
                    if question_4ba=='Scream':
                        print('Screaming does nothing and you eventually pass out from the lack of air.')
                        attacker_scene == False
                        break
                #comeback to this
                #either find a way to get the player to try the question again or end the level right there
                    elif question_4ba=='Knee your Attacker':
                        print('You are able to lift your knee up hard. Your attacker wheezes in pain and rolls off of you. You are able to get up, and run to the door.')
                        attacker_scene == False
                        break
                        #I want to add an option to use the items you grabbed, but I don't know how to do that and how to make the code remember that the player picked out an item or if it will just remember it without me doing anything
            elif question_4b=='Roll away':
                print('Your attacker attempts to tackle you, but you are able to roll the other way as they fall to the floor. You are able to get up faster than your attacker, so you head towards the door again.')
                attacker_scene == False
                break
print('You were able to get to the door and pull the door open. You ran outside in the pitch black. Your neighbors right next door are friendly and always leave their back door unlock in case their kids get locked out. But, your car is closer.')
final_scene = True
while final_scene == True:
    question_5= raw_input('Do you Run to your Neighbors or Run to your Car?')
    if question_5=='Run to your Neighbors':
        print('You run to your neighbor, your hear your attacker exiting your house. You start to run a little faster. You get to the back door and it is locked. You forgot that they went out of town for the weekend. You turn to run away, but it’s too late. While you were trying to open the door, your attacker came up behind you. All you saw was him moving his arm down and the moon shining in his eyes. Then, everything goes dark. ')
        final_scene = False
        break
    elif question_5=='Run to your Car':
        print('You run to your car, you hear your attacker exiting your house. You got to your door and tried to open the door. But you cannot get it opened. Your car is locked. Your attacker comes up behind you, you see him through the reflection of your window. You try to move away, but he grabs the back of your head. Then everything goes dark. ')
        final_scene = False
        break
#There will be an extra option if the player grabbed an item but again I don't know if the code remembers you grabbed an item or not.
#End of Level One
