class country:
    def __init__(self, name, continent, population ):
        self.name =name 
        self.continent = continent
        self.population = population
    #arguements here arename, continent and rating

    def display_data(self):
        print (self.name, "is in", self.continent, "with a population of", self.population)

USA= country("USA", "North America", 328_200_000)
India= country("India", "Asia", 1_416_977_769)

USA.display_data()
India.display_data()

    
