class App():
    def __init__(self):
        self.var1 = 15
        self.var2 = 16
        self.var3 = 17
        self.var4 = 18
        self.var5 = 19

    def calculate(self):
        self.result = self.var1 * 4 + 2

    def retrieve(self):
        return self.result

    def calculate2(self):
        self.result2 = self.var2 * 4 - 2
        
    def retrieve2(self):
        return self.result2
    
    def calculate3(self):
        self.result3 = self.var3 * 4 + 4
        
    def retrieve3(self):
        return self.result3
    
    def calculate4(self):
        self.result4 = self.var4 * 4 - 4
        
    def retrieve4(self):
        return self.result4
    
    def calculate5(self):
        self.result5 = self.var5 * 4 - 3
        
    def retrieve5(self):
        return self.result5
    
if __name__ == "__main__":
    app = App()
    app.calculate()
    print(app.retrieve)
    
    app.calculate2()
    print(app.retrieve2)
    
    app.calculate3()
    print(app.retrieve3)

    app.calculate4()
    print(app.retrieve4)

    app.calculate5()
    print(app.retrieve5)
