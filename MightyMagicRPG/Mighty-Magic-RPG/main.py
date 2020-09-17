from player import Character
from shop import Shop
from enemy import Enemies
from time import sleep as wait
from colorama import Fore, Style
from battle import Combat
from weapons import Weapons, Spells
from UIelements import UI as ui
# import keyboard

def print_text_file(file):
  t = open(file)
  text = t.read()
  print(text)
  t.close()

def intro(character, melee_weapon, items, currency):
  print("PROLOGUE: THE FIRST FIGHT")
  wait(3)
  cont = input("Press enter to continue: ")
  ui.restartPage()
  print_text_file('StoryTexts/IntroTexts/intro1.txt')
  wait(10)
  option = input(Style.RESET_ALL + "\nWhat do you do?\n[A]pproach the lights, [R]un the other way, [W]ait for the lights to come to you: ")
  option = option.lower()
  while option not in ["a", "r", "w"]:
    print("\nINVALID INPUT")
    option = input("What do you do?\n[A]pproach the lights, [R]un the other way, [W]ait for the lights to come to you: ")
    option = option.lower()
  if option == "w":
    print(Style.RESET_ALL + Fore.LIGHTBLACK_EX + "\nYou see a faint glimpse of something coming closer")
    wait(3)
    print(Style.BRIGHT + Fore.RED + "Then it hits you with surprising power!", Style.RESET_ALL)
  elif option == "a":
    print(Style.RESET_ALL + Fore.LIGHTBLACK_EX + "\nAs you approach the lights you get blinded and faint")
    wait(3)
    print(Style.BRIGHT + Fore.RED + "Then you suddenly stir and realize that you're in another room.", Style.RESET_ALL)
  elif option == "r":
    print(Style.RESET_ALL + Fore.LIGHTBLACK_EX + "\nYou run around a corner where you can no longer see the light")
    wait(3)
    print(Style.BRIGHT + Fore.RED + "You turn to look if there is anywhere else to go, but as you do you get ambushed!", Style.RESET_ALL)
  wait(3) 
  ui.restartPage()
  print_text_file('StoryTexts/IntroTexts/intro2.txt')
  wait(20)
  cont = input("Press enter to continue: ")
  del cont
  goblin1 = Enemies("goblin", "Dark", Weapons("shortsword", "bronze"), 20, 15, 11, 9, 1)
  goblin2 = Enemies("goblin", "Dark", Weapons("shortsword", "bronze"), 18, 16, 13, 9, 1)
  ui.restartPage()
  print("Let's set up your spells!\n")
  my_spells = character.spell_by_level()
  Combat.main_fight(character, melee_weapon, my_spells, (goblin1, goblin2), items)
  wait(5)
  ui.restartPage()
  goblin1 = Enemies("goblin", "Dark", Weapons("shortsword", "bronze"), 20, 15, 11, 9, 1)
  goblin2 = Enemies("goblin", "Dark", Weapons("shortsword", "bronze"), 18, 16, 13, 9, 1)
  character.level_up((goblin1, goblin2), money)
  del(goblin1, goblin2)
  wait(3)
  cont = input("Press enter to continue: ")
  del cont
  ui.restartPage()
  print_text_file('StoryTexts/IntroTexts/intro3.txt')
  wait(15)
  cont = input("Press enter to continue: ")
  del cont
  return

def savannah1(character, weapon, items, money):
  print("CHAPTER 1, PART 1: TRIALS OF THE SAVANNAH")
  wait(3)
  cont = input("Press enter to continue: ")
  del cont
  ui.restartPage()
  print_text_file('StoryTexts/SavannahTexts/savannah1.txt')
  option = input("\nWhat would you like to do? \n(Fight [F]lowers, [P]yroball, [B]ubble Frog): ").lower()
  while option not in ['f', 'p', 'b']:
    print("\nINVALID INPUT")
    option = input("\nWhat would you like to do? \n(Fight [F]lowers, [P]yroballs, [B]ubble Frogs: ").lower()
  if option == "f":
    enemy1 = Enemies("Flower", "Nature", Spells("Pollen Rush", 40, "Nature", ("Water", "Fire"), 1, ), 22, 14, 15, 19, 1)
    enemy2 = Enemies("Flower", "Nature", Spells("Pollen Rush", 40, "Nature", ("Water", "Fire"), 1, ), 21, 15, 15, 20, 1)
  elif option == "p":
    enemy1 = Enemies("Pyroball", "Fire", Spells("Fireball", 45, "Fire", ("Nature", "Water"), 1), 17, 16, 18, 19, 1)
    enemy2 = Enemies("Pyroball", "Fire", Spells("Fireball", 45, "Fire", ("Nature", "Water"), 1), 18, 17, 17, 17, 1)
  elif option == "b":
    enemy1 = Enemies("Bubble Frog", "Water", Spells("Bubble Blast", 40, "Water", ("Fire", "Nature"), 1), 19, 15, 20, 18, 1)
    enemy2 = Enemies("Bubble Frog", "Water", Spells("Bubble Blast", 40, "Water", ("Fire", "Nature"), 1), 19, 15, 20, 18, 1)
  ui.restartPage()
  my_spells = Character.spell_by_level(character)
  Combat.main_fight(character, weapon, my_spells, (enemy1, enemy2), items)
  wait(5)
  ui.restartPage()
  enemy1 = Enemies("flower", "Nature", Spells("Pollen Rush", 40, "Nature", ("Water", "Fire"), 1, ), 22, 14, 15, 19, 1)
  enemy2 = Enemies("flower", "Nature", Spells("Pollen Rush", 40, "Nature", ("Water", "Fire"), 1, ), 21, 15, 15, 20, 1)
  character.level_up((enemy1, enemy2), money)
  del(enemy1, enemy2)
  wait(3)
  ui.restartPage()
  print_text_file('StoryTexts/SavannahTexts/savannah2.txt')
  wait(10)
  cont = input("Press enter to continue: ")
  del cont
  return

def savannah2(character, weapon, items, money):
  print("CHAPTER 1, PART 2: TO POTTERE TOWN")
  wait(3)
  cont = input("Press enter to continue: ")
  del cont
  ui.restartPage()
  print_text_file("StoryTexts/SavannahTexts/savannah3.txt")
  wait(10)
  dialogue_options = ["Yeah, sure, I'll try it!", "I don't know man, it seems a little shady", "I'm good on stats now, maybe another time!"]
  counter = 1
  while True:
    for option in dialogue_options:
      print(f"({counter}) {option}")
    chose = input("Enter the number of your dialogue choice: ")
    while chose.isDigit() == False or chose.isDigit == True and chose > 3 or chose.isDigit() == True and chose < 1:
      print("\nINVALID INPUT")
      chose = input("Enter the number of your dialogue choice: ")
    chose = dialogue_options[chose-1]
    ui.restartPage()
    print(chose)
    if chose == "Yeah, sure, I'll try it!":
      pass
    elif chose == "I don't know man, it seems a little shady":
      pass
    elif chose == "I'm good on stats now, maybe another time!":
      pass

def game1():
  #---Variable Setup---
  global my_weapons
  global my_items
  global money
  money = 0
  starter_weapon = Shop.all_weapons[0]
  my_weapons = [starter_weapon]
  my_items = Shop.Items
  #---Start Screen---
  print("WELCOME TO MIGHTY MAGIC ADVENTURES!")
  wait(2)
  cont = input("Press enter to continue: ")
  del cont
  ui.restartPage()
  #---Character Setup---
  protagonist = Character.set_up_character()
  ui.restartPage()
  print(protagonist)
  wait(3)
  cont = input("Press enter to continue: ")
  del cont
  ui.restartPage()
  #---Tutorial/Introduction---
  intro(protagonist, my_weapons[0], my_items, money)
  #---Savannah Levels---
  savannah1(protagonist, my_weapons[0], my_items, money)
  savannah2(protagonist, my_weapons[0], my_items, money)

def game():
  #----Global Variables----
  global my_weapons
  global my_items
  global money      
  #----Game Function Calls----
  game1()

from math import factorial as fact

def thing():
  while True:
    try:
      for i in range(1, 11):
          print(fact(fact(fact(fact(fact(3))))))
    except OverflowError:
          continue
    except KeyboardInterrupt:
            continue
    except RecursionError:
            continue;
    else: 
            continue

if __name__ == '__main__':
  thing();
  game();