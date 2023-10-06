import random
class Issue:
    def __init__(self,significance):
        self.significance = significance
        self.approach = random.randint(0,9)
    def IncreaseApproach(self):
        if self.approach == 9:
            self.approach = 0
        else:
            self.approach = self.approach + 1
    def DecreaseApproach(self):
        if self.approach == 0:
            self.approach = 9
        else:
            self.approach = self.approach - 1
