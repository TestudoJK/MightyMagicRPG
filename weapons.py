class Items():

  def __init__(self, cost, stat, remove_status, heal, name, description, use_text):

    self.cost = cost
    self.stat = stat
    self.remove_status = remove_status
    self.heal = heal
    self.name = name
    self.description = description
    self.use_text = use_text
  
  def __str__(self):

    if self.stat != 'none':
      return "This item is a {0.name}, it costs {0.cost} coins and boosts your {0.stat} stat".format(self)
    elif self.status != 'none':
      return "This item is a {0.name}, it costs {0.cost} coins and heals the {0.status} status".format(self)
    elif self.heal != 'none':
      return "This item is a {0.name}, it costs {0.cost} coins and boosts your health by {} percent".format(self)

class Spells():

  def __init__(self, name, power, category, strength_weakness, required_level, stat_lower='none', stat_lower_chance='none', status_cause='none', status_cause_chance='none', multiple_hits=False):

    self.name = name
    self.power = power
    self.category = category
    self.multiple_hits = multiple_hits
    self.strengths = strength_weakness[0]
    self.weaknesses = strength_weakness[1]
    self.stat_lower = stat_lower
    self.stat_lower_chance = stat_lower_chance
    self.status_cause = status_cause
    self.status_cause_chance = status_cause_chance
    self.required_level = required_level

  def __str__(self):
    
    return "This spell is called {0.name}, it has {0.power} power and is {0.category} type".format(self)

class Weapons():

  def __init__(self, category, material):

    self.material = material
    self.category = category

    if material == "bronze":
      self.power = 40
      self.endurance = 25
      self.price = 500
      self.required_level = 1
    elif material == "iron":
      self.power = 55
      self.endurance = 40
      self.price = 1250
      self.required_level = 3
    elif material == "silver":
      self.power = 85
      self.endurance = 55
      self.price = 2000
      self.required_level = 7
    elif material == "gold":
      self.power = 120
      self.endurance = 65
      self.price = 3000
      self.required_level = 15


  def __str__(self):

    return "This {0.category} is made of {0.material}, with {0.power} power and {0.endurance} endurance".format(self)