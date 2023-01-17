print('--------------------------------------')
print(' Welcome to arithmetic bot ')
print()



def Greeting() :
  name = input('what is your name? ')
  
  return 'Hello ' + name + ', I am Ari.'
  
  
print(Greeting())
def madlib():
  
  print("Fairytale Madlib")
  print("Type a response then click enter")
  
  print("------------------")
        
  
  noun1 = input("noun 1: ")
  print()
  
  name = input("name: ")
  
  print()
  gender = input("male or female: ")
  
  print()
  verb1 = input("action verb without tense: ")
  print()
  gender2 = "his"
  print()
  family_member = input("family member: ")
  print()
  food = input("plural food: ")
  print()
  better_or_worse = input("better or worse: ")
  print()
  male = "male" or "MALE" or "Male" or "Boy" or "BOY"
  if (gender) != (male):
      (gender) = "she"
      (gender2) = "her"
  else:
      (gender) = "he"
      (gender2) = "his"
  
  
  #story
  print("Once upon a time, there lived a miserable " + noun1 + " and " + (gender2) + " name was " + name + ". " + name +" loved to " + verb1 + ". " + name + "'s problem was that " + gender2 + " " + family_member + " hated her. " + "Maybe because " + gender + " was " + better_or_worse + " at magic? " + "One day, " + name + " was eating " + food + ", when " + gender + " heard a loud scream. " + name + " quickly rushed into the kitchen and saw " + gender2 + " " + family_member + " cut their finger. Immediately, " + name + " helped " + gender2 + " " + family_member + " with her magic and the finger was back in place." "The " + family_member + " apoligized for every horrible thing they had done in the past " + "and the 2 lived happily ever after") 
  print()
  print("The end.")
  
  
  
  
  #slot_one = input("name ")
  
  
  #print(slot_one)
  
  #print("little " + (slot_one))
  
  
  
  #story outline
  #Once upon a time there lived  a miserable ?noun?, and his name was ?name?. He loved to ?verb? but he couldn't, because his ?male family member? hated him. One day, something weird happened.(name) was ?verb? on the ?noun1?, when he heard a loud scream across the ?noun1? It seemed like someone was in trouble, so he quickly ran to help. To his surprise, it was his ?male family member?, who had accidentely cut their fingers while chopping (vegetable ) + "s". (name)
  
  '''person = "she"
  noun1 = ("gender: ")
  name = input("enter your name: ")
  print("once upon a time, there lived a miserable "boy + noun1 "and her name was " + name )
  '''
  
    

 
def question():
  Q = input('Would you like to play a madlib? TYPE N for no, or Y for yes ')
  if Q == 'Y' :
    print(madlib())
    print('That was fun!')
  else:
    input('Why not?')
    print('Okay then, until next time!')


print(question())