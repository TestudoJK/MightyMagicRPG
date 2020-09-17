from weapons import Spells as spells
class Character():
  global all_spells

  def __init__(self, name, age):
    global stats
    global healths

    self.name = name
    self.age = age
    self.level = 1
    self.xp = 0
    self.status = 'none'
    self.attack = 20
    self.defense = 20
    self.spell = 20
    self.health = 40
    self.maxHealth = 40

    stats = [self.attack, self.defense, self.spell]

  def __str__(self):

    return "Your name is {0.name}, you're {0.age} years old, you're level {0.level}, and you have {0.xp} experience points".format(self)

  def level_up(self, enemy_defeated, money):
    global stats
    global healths
    new_xp = 0
    new_money = 0
    for enemy in enemy_defeated:
      new_xp += 0.75 * enemy.level * 500
      new_money += 0.25 * enemy.level * 250
    self.xp += new_xp
    money += new_money
    print("You got {} xp, giving you a total of {}. You also recieved {} coins, giving you a total of {} coins".format(new_xp, self.xp, new_money, money))
    level2 = [1000, 3000, 2, 10]
    level3 = [3000, 7500, 3, 11]
    level4 = [7500, 12000, 4, 12]
    level5 = [12000, 17500, 5, 13]
    level6 = [17500, 22000, 6, 14]
    level7 = [22000, 30000, 7, 15]
    level8 = [30000, 37500, 8, 16]
    level9 = [37500, 45000, 9, 17]
    level10 = [45000, 52500, 10, 18]
    level11 = [52500, 60000, 11, 19]
    level12 = [60000, 70000, 12, 20]
    level13 = [70000, 85000, 13, 21]
    level14 = [85000, 125000, 14, 22]
    level15 = [125000, 1503000, 15, 23]
    levels = [level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12, level13, level14, level15]
    for level in levels:
      if self.xp >= level[0] and self.xp < level[1]:
        if self.level == level[2]:
          return
        print("Crongratulations, you're now level {}".format(level[2]))
        self.level = level[2]
        print("Your stats improved!")
        for stat in stats:
          stat += level[3]
        self.maxHealth += 2
        self.health = self.maxHealth
        print("Your max health improved by 2, and you healed completely!")

  def set_up_character():
    print("Let's set up your character!")
    cont = ""
    while cont != "y":
      name = input("\nPlease, tell me your name (Max. 8 characters): ")
      while len(name) > 8 or name.isdigit() == True:
        print("\nINVALID INPUT")
        name = input("Please, tell me your name (Max. 8 characters): ")
      name = name.lower()
      name = name.capitalize()
      cont = input("So, you're name is {}? Y/N: ".format(name))
      cont = cont.lower()
      while cont not in ["y", "n"]:
        print("\nINVALID INPUT")
        cont = input("So, you're name is {}? Y/N: ".format(name))
        cont = cont.lower()
    cont = ""
    while cont != "y":
      age = input("\nPlease, tell me your age. (You should be no older than 25): ")
      while age.isdigit() == False:
        print("\nINVALID INPUT")
        age = input("\nPlease, tell me your age: ")
      age = int(age)
      while age > 25 or age <= 0:
        age = input("\nPlease, tell me your age. (You should be no older than 25): ")
        while age.isdigit() == False:
          print("\nINVALID INPUT")
          age = input("\nPlease, tell me your age: ")
        age = int(age)
      cont = input("So, you're {} years old? Y/N: ".format(age))
      cont = cont.lower()
      while cont not in ["y", "n"]:
        print("\nINVALID INPUT")
        cont = input("So, you're {} years old? Y/N: ".format(age))
        cont = cont.lower()
    protagonist = Character(name, age)
    return protagonist 

  bubble_blast = spells("Bubble Blast", 40, "Water", ("Fire", "Nature"), 1)
  boiling_stream = spells("Boiling Stream", 55, "Water", ("Fire", "Nature"), 5, status_cause='burn', status_cause_chance=30)
  aquatic_storm = spells("Aquatic Storm", 75, "Water", ("Fire", "Nature"), 10, multiple_hits=True)
  aqua_blast = spells('Aqua Blast', 90, 'Water', ("Fire", "Nature"), 15)
  fireball = spells('Fireball', 45, 'Fire', ("Nature", "Water"), 1)
  explosive_flame = spells('Max Inferno', 55, 'Fire', ("Nature", "Water"), 5)
  flame_pillar = spells('Flame Pillar', 75, 'Fire', ("Nature", "Water"), 10, stat_lower='attack', stat_lower_chance=20)
  combustion_trifecta = spells('Combustion Trifecta', 30, 'Fire', ("Nature", "Water"), 15)
  pollen_rush = spells('Pollen Rush', 40, 'Nature', ('Water', 'Fire'), 1, status_cause='sleepy', status_cause_chance=20)
  flower_power = spells('Flower Power', 55, 'Nature', ('Water', 'Fire'), 5, multiple_hits=True)
  deep_roots = spells('Deep Roots', 80, 'Nature', ('Water', 'Fire'), 10)
  solar_flare = spells('Solar Flare', 110, 'Nature', ('Water', 'Fire'), 20, status_cause='stun', status_cause_chance=30)
  arrow_of_light = spells('Arrow of Light', 45, 'Light', ('Dark', 'Dark'), 3, stat_lower='defense', stat_lower_chance=45)
  angelic_wings = spells('Angelic Wings', 70, 'Light', ('Dark', 'Dark'), 7)
  stunning_flash = spells('Stunning Flash', 85, 'Light', ('Dark', 'Dark'), 15, status_cause='stun', status_cause_chance=60)
  thoron_blast = spells('Thoron Blast', 110, 'Light', ('Dark', 'Dark'), 20, multiple_hits=True)
  poisonous_bite = spells('Poisonous Bite', 35, 'Dark', ('Light', 'Light'), 3, status_cause='poison', status_cause_chance=100)
  darkness_void = spells('Darkness Void', 55, 'Dark', ('Light', 'Light'), 7, multiple_hits=True)
  shadow_beam = spells('Shadow Beam', 85, 'Dark', ('Light', 'Light'), 15, stat_lower='spell', stat_lower_chance=35)
  retaliation_punch = spells('Retaliation Punch', 120, 'Dark', ('Light', 'Light'), 20)

  all_spells = [bubble_blast, boiling_stream, aquatic_storm, aqua_blast, fireball, explosive_flame, flame_pillar, combustion_trifecta, pollen_rush, flower_power, deep_roots, solar_flare, arrow_of_light, angelic_wings, stunning_flash, thoron_blast, poisonous_bite, darkness_void, shadow_beam, retaliation_punch]

  def spell_by_level(character):
    chosen_spells = []

    for spell in all_spells:
      if spell.required_level <= character.level:
        print("\n" + str(spell))
        select = input("Would you like to use this spell? Y/N: ").lower()
        while select not in ["y", "n"]:
          print("\nINVALID INPUT")
          print("\n" + str(spell))
          select = input("Would you like to use this spell? Y/N: ").lower()
        if select == 'n':
          continue
        else:
          chosen_spells.append(spell)
    if len(chosen_spells) == 0:
      print("You must select at least one spell")
      Character.spell_by_level()
    else:
      return chosen_spells

# public class Main{

#    public static void main(String[] args){
#     System.out.println("Hello, World!");
#    }// end void main

# }// end class Main