class car:
    def __init__(self,color,price,model):
        self.mycolor = color
        self.myprice = price
        self.mymodel = model
    def mycar(self):
        if self.mymodel >= 2018:
            self.myprice += 50
            print(f'new model {self.myprice}')
        else:
            self.myprice -= 50
            print(f'new model {self.myprice}')
BMW = car('resd', 5000, 2018)
Ford = car('white',4000,2017)
BMW.mycar()
Ford.mycar()

