import random
class Leader:
    def __init__(self,name):
        self.name = name
        self.popularity = random.randint(50,80)
        self.persuasion = random.randint(50,80)
        self.leadership = random.randint(50,80)
    def LeaderDisplay(self):
        print("Leader Name: ", self.name)
        print("Leader Popularity: ", self.popularity)
        print("Leader Persuasion: ", self.persuasion)
        print("Leader Leadership: ", self.leadership)
    def PopularityIncrease(self):
        if self.popularity >= 90:
            self.popularity = 100
        else:
            self.popularity += random.randint(1,10)
    def PopularityDecrease(self):
        if self.popularity <= 10:
            self.popularity = 0
        else:
            self.popularity -= random.randint(1,10)