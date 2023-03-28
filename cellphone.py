class cellphone:
    def __init__(self, model, year, price):
        self.model = model 
        self.year = year
        self.price = price
    #arguements here are model, year and rating

    def calculate_depreciation(self): #
        depreciation_rate = 0.67
        years_old = 2
        depreciation_factor = (1- depreciation_rate) * years_old
        depreciation_value = self.price * depreciation_factor
        return depreciation_value
    
    def display_data(self):
        depreciation=self.calculate_depreciation()
        print (self.model, "is a", self.year, "model with a cost of", self.price,"which has a depreciation price of", depreciation, "after 2 years" )

Sony_alpha=cellphone(model="Sony Alpha", year="2022", price=3_849_00)
Canon= cellphone(model="Canon", year="2022", price=4_369_00)
Sony_alpha.display_data()
Canon.display_data()


    
