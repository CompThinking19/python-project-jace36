#Intro screen
print("Welcome to Survive the Night");
#I'm not exactly sure if this is how you create a choose your own adventure game, but a model I saw online had a similiar looking code, so hopefully they did it right?? And I didn't type out all of this for nothing

#Starter Screen
starting_question_1=input('Ready to play?: ')
if starting_question_1=='yes':
    print('Let us begin')
#After saying yes, players get to create their character and has to choose between male or female
#Yet, if the player tries to pick male, it won't work, so they have no choice but to pick female
#I have no idea how to do that yet though, I think I just use a typeError, but not a hundred percent sure yet
name=input('Enter a female name for your character: ')
#after naming their character, the game starts

#Level 1
print("It was just your average Thursday night. You got out of work an hour ago and you were able to pick up some groceries for the weekend. After putting your groceries away, you settle on the couch and turn on the TV. However, you don't know what you want to watch.")
question_1=input('Should you watch a Comedy or a Thriller?')
if question_1=='Comedy':
    print('You put on Brooklyn Nine Nine')
elif question_1=='Thriller':
    print('You put on Stranger Things')
#This section just gives players an idea of what the game is going to be like from here on out.
#Although this won't show that every choice in this game has a consequence or a certain outcome, it just offers an idea of what to expect.
print("You get through ten minutes of your show, before you here a noise upstairs")
question_2=input('Ignore the noise or Investigate the noise?')
if question_2=='Ignore the noise':
    print('You decide to ignore the noise, but it seems to get louder and louder. So, you decide to investigate after all')
#The character will have to investigate no matter what, so I need to figure out a way to link the investigating steps to the ignore step after the last line is printed
elif question_2=='Investigate the noise':
    print('You decided to investigate the noise. As you got closer to the stairs, you start to distinct footsteps upstairs.')
#this will open up a little sub option that can help the player later on in the game, but if they decide not to grab anything to defend right now, the items  will still be there for them later on
print('You stop in the hallway near your front door, your stairs are right there, but you feel nervous. You wonder if you should grab something to defend yourself or just keep going.')
question_3=input('Should you grab something or keep going?')
if question_3=='Grab Something':
    print('You decided to grab something, should you grab your car keys you left on your hallway table or the baseball bat you keep near the door?')
        if question_3a=='Grab Keys':
            print('You grabbed the Keys and left the Bat behind')
        elif question_3a=='Grab Bat':
            print('You grabbed the Bat and left the Keys behind')
#I need to figure out how to link this to keep going after making the choice of bringing something along. I'm not sure if I have to create a whole new option in order to ensure that the player has the item they grabbed or just link it to the keep going and the code will just remember that you have an item
#Both of these choices will affect the character latter on, but they can never pick up the other item later on in the game
#However, if the player didn't pick them when they could, they'll have another chance to grab one of them later on
elif question_3=="Keep Going":
    print('You decided to keep going. ')
print('You made it to the foot of your stairs and you look at the top of the steps. You see a figure standing at the top. Do you turn on the lights or run?')
question_4=input('Turn on the Lights or Run?')
if question_4=='Turn on the Lights':
    print('You turn on the lights and you see a man at the top of the stairs. He is concealing his face, but you have a feeling that you know him. Should you yell at him, attempting to scare him away, or run towards the front door?')
        question_4a=input('Yell or Run?')
        if question_4a=='Yell':
            print('You yelled at the man, screaming at him to get out of your house. The man did not move, your threat meant nothing')
        elif question_4a=='Run':
            print('You ran for the door, but the man jump down the stairs and chased after you.')
