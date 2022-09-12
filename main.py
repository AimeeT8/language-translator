import csv

def intro():
  print('Welcome to the Spanish and French translator app.\nPlease enter an English word and press the "Enter" key.')
  print('\nType "done" at any time to exit')

translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")

  for line in reader: 
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish, french]
    

done = False

intro()

def exit():
  print('\nThanks for using the translator app. Have a great day!')

while not done:
    word = input("\ntype an English word to translate:")
    word = word.lower()

    if word == "done":
        
        done = True
        exit()

    elif word in translations:
        print(f'\nSPANISH: {translations[word][0]}')
        print(f'\nFRENCH: {translations[word][1]}')

    else:
        print(
            "\nsorry this word is not in the translations dictionary. Please try again. "
        )


