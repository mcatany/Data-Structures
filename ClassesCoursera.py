# Classes

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name)
        
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)

an = PartyAnimal("Sally")
an.party()
wentz = FootballFan("Carson")
wentz.touchdown()
