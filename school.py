class School:

  def __init__(self, name, level, numberOfStudents):
    self.name = name 
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return "The school named " + self.name + " is a " + self.level + " school with " + str(self.numberOfStudents) + " students."


class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'Primary School', numberOfStudents)
    self.pickupPolicy = pickupPolicy


  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentrepr = super().__repr__()
    return parentrepr + " The pickup policy is: " + str(self.get_pickupPolicy())

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportTeams):
    super().__init__(name, 'HighSchool', numberOfStudents)
    self.sportTeams = sportTeams

  def get_sportTeams(self):
    return self.sportTeams

  def __repr__(self):
    parentrepr = super().__repr__()
    return parentrepr + " We have different sportTeams at our school like " + str(self.get_sportTeams())

dalåsen = PrimarySchool('Dalåsen skole', 46, 1630) 
print(dalåsen)

lunken = School('Lunken Skole', 'High School', 334)
print (lunken)
print (lunken.get_name())
print (lunken.get_level())
lunken.set_numberOfStudents(45)
print (lunken.get_numberOfStudents())

fiken = HighSchool ("Fiken", 572, ['basketball', 'fotball', 'svømming', 'dans', 'klatring'])
print (fiken)

















