class basketball:
    def __init__ (self, name,goals,games):
        self.name = name #self.name is now an attribute of the basketball class
        self.goals = goals
        self.games = games
#arugements here: name, games and goals

    def calculate_average(self): #function to create average gaoals per game
        if self.games == 0:
            return 0.0
        return self.goals / self.games

    def display_average(self):#displays the average goals per game
        avg_goals = self.calculate_average()
        print(self.name, "scored", self.goals,"goals in", self.games, "games and her average number goals per game were", avg_goals)

Jeana = basketball("Jeana", 10, 20)
Jessie = basketball("Jessie", 5, 10)
Jeana.display_average()
Jessie.display_average()
