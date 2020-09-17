from UIelements import UI as ui
from random import randint as randomNum
from time import sleep as wait

class Combat:
  damage = 0
  def player_take_damage(character, enemy, power, type_of_attack):
    x = randomNum(75, 100)
    x *= 0.01
    if type_of_attack == 'physical':
      damage = ((((3 * enemy.level) // 5) + 2) * (power * enemy.attack/character.defense)) // 15 * x
    elif type_of_attack == 'spell':
      damage = ((((3 * enemy.level) // 5) + 2) * (power * enemy.attack/character.defense)) // 15 * x
    damage = round(damage)
    character.health -= damage
    print("The {} did {} damage to you, leaving you at {} health!".format(enemy.name, damage, character.health))
    wait(2)
    ui.restartPage()
    if character.health <= 0:
      ui.restartPage()
      print("GAME OVER")
      wait(3)
      exit()

  def take_damage(target, power, modifier, character, type_of_attack):
    global damage
    x = randomNum(75, 100)
    x *= 0.01
    modifier *= x
    if type_of_attack == "physical":
      damage = ((((3 * character.level) // 5) + 2) * (power * character.attack/target.defense)) // 15 * modifier
      damage = round(damage)
    elif type_of_attack == "spell":
      damage = ((((2 * character.level) // 5) + 2) * (power * character.spell/target.defense)) // 15 * modifier
      damage = round(damage)
    if type(target) == list:
      for enemy in target:
        enemy.health -= damage
        print("\nYou did {0} damage to the {1.name}! Leaving him at {1.health} health!".format(damage, enemy))
        wait(2)
        if enemy.health <= 0:
          print("The {} has died!".format(enemy.name))
          enemy_list.remove(target)
      if len(target) == 0:
        print("You've killed all of your targets!")
        enemy_list.remove(target)
    else:
      target.health -= damage
      print("\nYou did {0} damage to the {1.name}! Leaving him at {1.health} health!".format(damage, target))
      wait(2)
      if target.health <= 0:
        print("The {} has died!".format(target.name))
        enemy_list.remove(target)
        wait(2)
      ui.restartPage()

  def check_for_status(target):
    if target.status == 'none':
      return True
    elif target.status == "stun":
      print("The {} is stunned! He is unable to move this turn!".format(target.name))
      target.status == 'none'
      return False
    elif target.status == "sleepy":
      num = randomNum(1, 3)
      if num == 1:
        wait(1)
        target.status == 'none'
        print("The {} woke up!".format(target.name))
        wait(1)
        return True
      else:
        return False
    else:
      damage = target.health * (1 / 16)
      target.health -= damage
      if target.status == "poisoned":
        print("The {} took {} poison damage".format(target.name, damage))
      elif target.status == "burn":
        print("The {} took {} burn damage".format(target.name, damage))
      return False

  def give_status(target, status):
    ui.restartPage()
    target.status = str(status).lower()
    print("You gave the {} the status {}!".format(target.name, status))
    wait(2)

  def lower_defense(target):
    target.attack -= (target.spell * 1/6)
    print("You lowered the defense of the {}".format(target.name))
    wait(2)

  def lower_attack(target):
    target.attack -= (target.spell * 1/6)
    print("You lowered the attack of the {}".format(target.name))
    wait(2)

  def lower_spell(target):
    target.spell -= (target.spell * 1/6)
    print("You lowered the power of the {}'s spell".format(target.name))
    wait(2)

  def use_item(selected_item, character, melee_weapon, spells, items, enemies):
    current_status = character.status
    if selected_item.remove_status != 'none':
      if selected_item.remove_status == current_status:
        select = input("Would you like to use this item to clear the status {}? Y/N ".format(current_status))
        select = select.lower()
        while select not in ['y', 'n']:
          print("\nINVALID INPUT")
          select = input("")
        if select == 'n':
          Combat.player_turn(character, melee_weapon, spells, items, enemies)
        else:
          print(str(selected_item.use_text) + ", and...")
          wait(2)
          print("You cleared the status {}!".format(character.status))
          character.status = 'none'
          items.remove(selected_item)
      else:
        print("You cannot use this item right now because you don't have the status {}!".format(selected_item.remove_status))
        wait(3)
        Combat.player_turn(character, melee_weapon, spells, items, enemies)
    
  def player_turn(character, melee_weapon, spells, items, enemies):
    global enemy_list
    ui.restartPage()
    if len(enemy_list) == 1:
      ui.UIelement_1(character, (enemy_list[0].maxHealth, enemy_list[0].health), enemy_list)
    elif len(enemy_list) == 2:
      ui.UIelement_1(character, (enemy_list[0].maxHealth, enemy_list[0].health, enemy_list[1].maxHealth, enemy_list[1].health), enemy_list)
    elif len(enemy_list) == 3:
      ui.UIelement_1(character, (enemy_list[0].maxHealth, enemy_list[0].health, enemy_list[1].maxHealth, enemy_list[1].health, enemy_list[2].maxHealth, enemy_list[2].health), enemy_list)
    select = input("What would you like to do? Enter a letter indicated by the []: ")
    select.lower()
    while select not in ["m", "s", "i", "e"]:
      print("\nINVALID INPUT")
      select = input("What would you like to do? Enter a letter indicated by the []: ")
      select.lower()
    while select == "m":
      if melee_weapon:
        for enemy in enemy_list:
          ui.restartPage();
          print("This {} has {} health and a {} {}.".format(enemy.name, enemy.health, enemy.weapon.material, enemy.weapon.category));
          cont = input("\nWould you like to hit this enemy? Y/N: ").lower();
          while cont not in ["y", "n"]:
            print("\nINVALID INPUT");
            cont = input("Would you like to hit this enemy? Y/N: ");
            cont = cont.lower();
          if cont == "n":
            continue;
          elif cont == "y":
            target = enemy
            Combat.take_damage(target, melee_weapon.power, 1, character, "physical");
            melee_weapon.endurance -= 1;
            if melee_weapon.edurance == 0:
              print("Your melee weapon broke!");
              del melee_weapon
            else:
              print(f"Your melee weapon has {melee_weapon.endurance} endurane remaining!")
            try:
              del target
            except NameError:
              pass
          break
      else:
        print("Your melee weapon is broken!")
        select = input("What would you like to do? Enter a letter indicated by the []: ")
        select.lower()
        while select not in ["m", "s", "i", "e"]:
          print("\nINVALID INPUT")
          select = input("What would you like to do? Enter a letter indicated by the []: ")
          select.lower()
      try:
        if target:
          continue
        else:
          return
      except UnboundLocalError:
        return
    while select == "s":
      counter = 1
      if len(spells) > 1:
        for spell in spells:
          print("({0}) {1}\n".format(counter, spell.name))
          counter += 1
        cont = input("Select the number of the spell you'd like to use (or type back to exit): ")
        cont = cont.lower()
        if cont == 'back':
          select = input("What would you like to do? Enter a letter indicated by the []: ")
          select.lower()
          while select not in ["m", "s", "i", "e"]:
            print("\nINVALID INPUT")
            select = input("What would you like to do? Enter a letter indicated by the []: ")
            select.lower()
        while cont.isdigit() == False or cont.isdigit() == True and int(cont) <= 0 or cont.isdigit() == True and int(cont) > len(spells):
          print("\nINVALID INPUT")
          cont = input("Select the number of the spell you'd like to use (or type back to exit): ")
          cont = cont.lower()
          if cont == 'back':
            select = input("What would you like to do? Enter a letter indicated by the []: ")
            select.lower()
            while select not in ["m", "s", "i", "e"]:
              print("\nINVALID INPUT")
              select = input("What would you like to do? Enter a letter indicated by the []: ")
              select.lower()
      else:
        cont = 1
      cont = int(cont) - 1
      selected_spell = spells[cont]
      for enemy in enemy_list:
        ui.restartPage()
        try:
          print("This {0.name} has a {0.weapon.material} {0.weapon.category}, and {0.health} health.".format(enemy))
        except AttributeError:
          print("This {0.name} uses {0.weapon.name}, and has {0.health} health".format(enemy))
        cont = input("\nWould you like to hit this enemy? (If you've selected a multihit spell, this choice is irrelevant) Y/N: ")
        cont = cont.lower()
        while cont not in ["y", "n"]:
          print("\nINVALID INPUT")
          cont = input("Would you like to hit this enemy? Y/N: ")
          cont = cont.lower()
        if cont == "n":
          continue
        else:
          target = enemy
          if enemy.type == selected_spell.strengths[0] or enemy.type == selected_spell.strengths[1]:
            modifier = 2
          elif enemy.type == selected_spell.weaknesses[0] or enemy.type == selected_spell.weaknesses[1]:
            modifier = 0.5
          else:
            modifier = 1
          if selected_spell.multiple_hits == False:
            if selected_spell.status_cause == 'none' and selected_spell.stat_lower == 'none':
              if selected_spell.name == 'Combustiion Trifecta':
                Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
                Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
                Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
                return
              else:
                Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
              return
            elif selected_spell.stat_lower != 'none' and selected_spell.power > 0:
              Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
              x = randomNum(selected_spell.stat_lower_chance, 100)
              if x >= selected_spell.stat_lower_chance:
                if selected_spell.stat_lower == 'defense':
                  Combat.lower_defense(target)
                elif selected_spell.stat_lower == 'attack':
                  Combat.lower_attack(target)
                elif selected_spell.stat_lower == 'spell':
                  Combat.lower_spell(target)
              return
            elif selected_spell.status_cause != 'none' and selected_spell.power > 0:
              Combat.take_damage(target, selected_spell.power, modifier, character, 'spell')
              x = randomNum(selected_spell.status_cause_chance, 100)
              if x >= selected_spell.status_cause_chance:
                Combat.give_status(target, selected_spell.status_cause)
              return
          else:
            Combat.take_damage(enemy_list, selected_spell.power, modifier, character, 'spell')
            return
    while select == "i":
      if len(items) == 0:
        print("You don't have any items!")
        wait(2)
        ui.restartPage()
        Combat.player_turn(character, melee_weapon, spells, items, enemies)
      else:
        counter = 1
        for item in items:
          print("\n({}) {}".format(counter, item.name))
        cont = input("\nSelect the number of the item you would like to use (or type back to exit): ")
        cont = cont.lower()
        if cont == 'back':
          Combat.player_turn(character, melee_weapon, spells, items, enemies)
        while cont.isdigit() == False or int(cont) > len(items) or int(cont) <= 0:
          print("\nINVALID INPUT")
          cont = input("Select the number of the item you would like to use (or type back to exit): ")
          cont = cont.lower()
          if cont == 'back':
            Combat.player_turn(character, melee_weapon, spells, items, enemies)
          continue
        cont = int(cont) - 1
        selected_item = items[cont]
        ui.item(selected_item.name, selected_item.description)
        select = input("Would you like to use this item? Y/N ")
        select = select.lower()
        while select not in ['y', 'n']:
          print("\nINVALID INPUT")
          select = input("Would you like to use this item? Y/N")
        if select == 'n':
          Combat.player_turn(character, melee_weapon, spells, items, enemies)
        else:
          Combat.use_item(selected_item, character, melee_weapon, spells, items, enemies)
      return
    while select == "e":
      print("You've ended your turn.")
      return
    
  def enemy_turn(enemy, character):
    while enemy.health > 0:
      ui.restartPage()
      print("This {0} is going to hit you with a(n) {2} {1}!".format(enemy.name, enemy.weapon.category, enemy.weapon.material))
      wait(2.5)
      if enemy.weapon.category == "Bronze" or enemy.weapon.category == "Iron" or enemy.weapon.category == "Silver" or enemy.weapon.category == "Gold":
        type_of_attack = 'physical'
      else:
        type_of_attack = 'spell'
      Combat.player_take_damage(character, enemy, enemy.weapon.power, type_of_attack)
      return

  def main_fight(character, melee_weapon, spells, enemies, items):
    global enemy_list
    enemy_list = []
    ui.restartPage()
    for enemy in enemies:
      enemy_list.append(enemy)
      print("You've encountered {}".format(enemy.name))
    wait(3)
    ui.restartPage()
    while len(enemy_list) != 0:
      x = Combat.check_for_status(character)
      if x == False:
        print("You were prevented from going due to your status!")
      else:
        Combat.player_turn(character, melee_weapon, spells, items, enemies)
      for enemy in enemy_list:
        if enemy.health > 0 :
          x = Combat.check_for_status(enemy)
          if x == False:
            print("This {} couldn't go due their status".format(enemy.name))
          else:
            Combat.enemy_turn(enemy, character)
          continue
    else:
      ui.restartPage()
      print("You've won!")


  def choose_melee(total_weapons):
    ui.restartPage()
    for weapon in total_weapons:
      print(weapon)
      select = input("Would you like to use this weapon? Y/N: ")
      select = select.lower()
      while select not in ["y", "n"]:
        print("\nINVALID INPUT")
        select = input("Would you like to use this weapon? Y/N: ")
      if select == "y":
        print("You've equipped the {}.".format(weapon.category))
        return weapon
    else:
      Combat.choose_melee(total_weapons)
    try:
      if weapon:
        return weapon
    except UnboundLocalError:
      Combat.choose_melee(total_weapons)