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