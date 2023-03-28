class movie:
    def __init__(self, title, genre, expenses, revenue):
        self.title = title 
        self.genre = genre
        self.expenses = expenses
        self.revenue = revenue
    #arguements here are title, genre and rating

    def calculate_net_profit(self): #new function to calculate net profit
        if self.revenue == 0:
            return 0.0
        return self.revenue - self.expenses #expenses/revenue=net profit
    
    def display_net_profit(self):
        net_profit=self.calculate_net_profit()
        print (self.title, "is a", self.genre, "movie which has an expenses of", self.expenses, "revenue of", self.revenue, "and their net profit earned is", net_profit)

DDLJ=movie(title="DDLJ", genre="romance", expenses=1000, revenue=50000)
K3G= movie(title="K3G", genre="romcom", expenses=25000, revenue=800000)
DDLJ.display_net_profit()
K3G.display_net_profit()


    
