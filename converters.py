class Convert:

    def __init__(self, weight):
        self.weight = weight

    def Kgs(self):
        return self.weight * 0.45
    
    def Lbs(self):
        return self.weight / 0.45