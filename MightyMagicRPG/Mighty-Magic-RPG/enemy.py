class Enemies():

  def __init__(self, name, type_of_enemy, weapon, health, attack, defense, spell, level):

    self.name = name
    self.weapon = weapon
    self.health = health
    self.attack = attack
    self.defense = defense
    self.spell = spell
    self.type = type_of_enemy
    self.status = 'none'
    self.level = level
    self.maxHealth = health

  def __str__(self):
    try:
      return "This enemy is a(n) {0.name}, has a {0.weapon.material} {0.weapon.category}, and has {0.health} health.".format(self)
    except AttributeError:
      return "This enemy is a(n} {0.name}, uses {0.weapon.name}, and has {0.health} health"