class basketball:
    def __init__ (self, name,goals,games):
        self.name = name #self.name is now an attribute of the basketball class
        self.goals = goals
        self.games = games

    
    def speak(self):
        print(self.name, "scored", self.goals,"goals in", self.games, "games and her average number goals per game were", display_average)

Jeana = basketball("Jeana", 10, 20)
Jessie = basketball("Jessie", 5, 10)


Jeana.speak() #print "jeana"
Jessie.speak() #print "jessie"