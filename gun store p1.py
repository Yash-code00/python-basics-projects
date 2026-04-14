class gun:
    def __init__(self,skin,ROF,catories):
        self.skin = skin
        self.ROF = ROF
        self.catories= catories
    
    def descriptio(self):
        return f"The camo is: {self.skin} | The rate of fire is: {self.ROF} | The catories is: {self.catories}"
AK47 = gun("blood camo",44.00,"assult rifle")
print(AK47.descriptio())