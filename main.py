from random import *
Deck = []
def create_deck(Deck):
  for i in range(0,4):
    a = 1
    b = 11
    while a < b:
      if a == 10:
        for i in range (0,3):
          Deck.append(a)
      a = a+1
      Deck.append(a)
create_deck(Deck)
spades = Deck[]
#need to sperate "Deck" list into the 4 suits
diamonds =
clubs =
hearts =

print(Deck)
print(len(Deck))
game = input("Would you like to play a game of black jack with me? ").lower()
score = 1000
while score > 0:
  if game == "yes":
    card_1 = choice(Deck)
    card_2 = choice(Deck)
    Player_cards = (card_1, card_2)
   
    card_3 = choice(Deck)
    card_4 = choice(Deck)
    Used_cards = (card_1, card_2)
    Computer_cards = (card_3, card_4)
  elif game == "no":
    print("Ok, Bye!")
    break
  elif game != "yes" or "no":
    print("Invalid Syntaxt please tyoe 'yes' or 'no'")
    game = input("Would you like to play a game of black jack with me? ").lower()
  
  

  
  

