'''
Date: 12/25/23
Desc: Takes user inputted sentances and correctly translates it into pig latin.
Name: Totally perfect pig latin translator
'''



#Re used to split user inputted string into induvidual words based off of dashes and spaces.
import re
#Introduce the program to the user
print("Welcome to my english to pig latin translator.")

#Set what abc is (this could also be avoided by using isAlpha())
ABC = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"

#Set what numbers are.
Numerals = "0123456789"
while True: # main loop
 
 
  #Reset Punctuation, ensuring that we don't 
  #add characters from previous sentences.
  ToADD = []
  Punctuation = []
  
  #Get user input.
  UserInput = input("\n\nEnter what you want to translate:")


  

  #trying to only "capture" the dash results in an error, so I 
   #wrapped the space in parentheses too.
  splitwords = re.split("( |-)", UserInput)

  #We had to capture the spaces in the list, but we add spaces to he final output later in the-
  #-code, so we need to delete these "extra" spaces in the list.
  
#Used a loop as remove(" ") only removed the first space in the list
  for Things in range(len(splitwords)):
    #Gives error if there is no if statement, so I use one.
    if " " in splitwords:
      splitwords.remove(" ")




  #Get the amount of words in the sentence so we can loop through them.
  WordAmount = len(splitwords)

  

  #We have to use Range() instead of "word in splitwords" because we want 
  #to use splitwords with the "word" var inside the loop.
  #loop through the words
  for word in range(WordAmount):

    #Reset Punctuation so we don't add characters from previous words.
    Punctuation = []
    #Reset noVowels to true at the start of each loop, as by default the 
    #program assumes the word has no vowels until proven otherwise.
    NoVowels = True

    #We have two variables that are the "current" word selected. Origiword 
    #will stay the same, and Newword will be modified throughout the code
    #This is so we can referece the original while still making changes to the current word,
    NewWord = splitwords[word]
    FirstInput = NewWord
    
    if NewWord == "-":
      print(NewWord, end="")
      continue
      
    #if we are on the first letter, our vowels won't include "Y" as it's a constonant.
    vowels = ["a", "e", "i", "o", "u"]
    length = len(FirstInput)
  
  

      
    for NonLetters in range(length):

      if FirstInput[NonLetters] not in ABC and FirstInput[NonLetters] not in Numerals:
       Punctuation += FirstInput[NonLetters]
       NewWord = FirstInput.replace(FirstInput[NonLetters], "")
      

  

    for Letter in range(length):
      


      if Letter < 1 and FirstInput[0].lower() in vowels: #first letter is a vowel   
        NoVowels = False
        if word + 1 < len(splitwords) and splitwords[word + 1] == "-":
          Punctuation = ''.join(Punctuation)
          print(NewWord + "way", end="")
          print(Punctuation, end="")
          break
        else:
          Punctuation = ''.join(Punctuation)
          print(NewWord + "way", end="")
          print(Punctuation, end=" ")

          break
        
     #if the last letter was a q and the current one is a u, 
     #don't include u in the vowel list, as we want it to be moved along with the q.
      if FirstInput[Letter -1] ==  "q" and FirstInput[Letter] == "u":
        vowels = ["a", "e", "i", "o", "y"]
      


        #if the letter is not an actual letter, just print the symbol.
        #(this pretty much only happens if "firstinput" is a single character)
      if FirstInput[Letter] not in ABC or FirstInput[Letter] in Numerals:
        print(FirstInput[Letter], end="")
        NewWord = FirstInput.replace(FirstInput[Letter], "")

        if FirstInput[Letter] in Punctuation:       
          Punctuation.remove(FirstInput[Letter])
        #restart the for loop to go the the next character. 

        continue
        
      else:
        if FirstInput[Letter].lower() not in vowels:

  
          ToADD += FirstInput[Letter]

          #We have both NewWord and Firstinput so we can 
          #manipulate the final translation while still having 
          #an untouched version of the original statement.

          NewWord = NewWord[1:]
    
    
        #Otherwise, have all the vowels work, as y is a vowel  
      #if its not the first letter, and U is a vowel if not preceeded with "q"
          vowels = ["a", "e", "i", "o", "u", "y"]

  
        elif FirstInput[Letter].lower() in vowels: 

          ToADD = ''.join(ToADD)
          Punctuation = ''.join(Punctuation)
          FINAL = NewWord + ToADD
          #Preserve upercase starting letters
          if FirstInput[0].isupper():
            FINAL = FINAL.lower()
            FINAL = FINAL[0].upper() + FINAL[1:]
          ToADD = ""
          print(FINAL, end="")
      
          if word + 1 < len(splitwords) and splitwords[word + 1] == "-":
            print("ay" + Punctuation, end="")
          else:
            print("ay" + Punctuation, end=" ")
          NoVowels = False
          break
    #this is for single symbols or letters or words with only consonants.
    #this system sucks, fix this.
    if NoVowels == True and FirstInput.isalpha():
      print(FirstInput + "ay", end=" ")
    elif NoVowels == True:
      #if it is just a symbol or numeral, add a space to the end
      print(end=" ")
    

        
  
    
    
    
        
    
    
