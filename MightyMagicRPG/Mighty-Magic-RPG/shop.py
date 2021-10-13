from weapons import Weapons, Items
import time

class Shop():

  def __init__(self):
    global all_weapons
    self.all_weapons = all_weapons

  bronze_shortsword = Weapons("shortsword", "bronze")
  iron_shortsword = Weapons("shortsword", "bron")
  silver_shortsword = Weapons("shortsword", "silver")
  gold_shortsword = Weapons("shortsword", "gold")
  bronze_axe = Weapons("axe", "bronze")
  iron_axe = Weapons("axe", "iron")
  silver_axe = Weapons("axe", "silver")
  gold_axe = Weapons("axe", "gold")
  bronze_lance = Weapons("lance", "bronze")
  iron_lance = Weapons("lance", "iron")
  silver_lance = Weapons("lance", "silver")
  gold_lance = Weapons("lance", "gold")
  bronze_bow = Weapons("bow", "bronze")
  iron_bow = Weapons("bow", "iron")
  silver_bow = Weapons("bow", "silver")
  gold_bow = Weapons("bow", "gold")

  all_weapons = [bronze_shortsword, iron_shortsword, silver_shortsword, gold_shortsword, bronze_axe, iron_axe, silver_axe, gold_axe, bronze_lance, iron_lance, silver_lance, gold_lance, bronze_bow, iron_bow, silver_bow, gold_bow]

  def weapons_shop(character, currency):
    global all_weapons
    global unlocked_weapons
    unlocked_weapons = []
    counter = 1
    ui.restartPage()
    print(Style.RESET_ALL + "Welcome to the shop, {}\n".format(character.name) + "|" + "─" * 50)
    print(" _͟ _")
    print("╱___╲")
    print("│=|=│\n" + "-" * 50)
    time.sleep(2)
    for i in all_weapons:
      if character.level >= i.required_level:
        print("|({1})  {0.material} {0.category} ".format(i, counter) + Fore.YELLOW + "({0.price} coins)".format(i) + Style.RESET_ALL + "\n" + "|" + "─" * 50)
        counter += 1
        unlocked_weapons.append(i)
      elif character.level < i.required_level:
        print("|" + Fore.RED + "You have not unlocked this yet!\n" + Style.RESET_ALL + "|" + "─" * 50)
    select = input("Select the number of the weapon you would like to purchase: ")
    while select.isdigit() == False:
      print("\nINVALID INPUT\n")
      select = input("Select the number of the weapon you would like to purchase: ")
    select = int(select) - 1
    while select < 0 or select > len(unlocked_weapons):
      print("\nINVALID INPUT")
      select = input("Select the number of the weapon you would like to purchase: ")
      while select.isdigit() == False:
        print("\nINVALID INPUT\n")
        select = input("Select the number of the weapon you would like to purchase: ")
      select = int(select) - 1
    selected_weapon = unlocked_weapons[select]
    cont = input("So would you like to purchase the {0.material} {0.category}? It costs ".format(selected_weapon) + Fore.YELLOW + "{0.price} coins.".format(selected_weapon) + Style.RESET_ALL + " Y/N: ")
    cont = cont.lower()
    while cont not in ["y", "n"]:
      print("\nINVALID INPUT")
      cont = input("So would you like to purchase the {0.material} {0.category}? It costs ".format(selected_weapon) + Fore.YELLOW + "{0.price} coins.".format(selected_weapon) + Style.RESET_ALL + " Y/N: ")
      cont = cont.lower()
    if cont == "n":
      # ui.restartPage()
      # Shop.shop(character, currency)
      pass
    else:
      return selected_weapon

  pillow = Items(40, 'none', 'none', 5, "Pillow", "The pillow restores your energy so you can take on the enemies...\n  and it's also very soft.", "You had a relaxing nap")
  Items = [pillow]