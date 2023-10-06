import random
class Participants:
    def __init__(self,name):
        self.name = name
        self.Popularity = random.randint(50,80)
        self.CritReasoning = random.randint(50,80)
        self.Persuasion = random.randint(50,80)
        self.Debating = random.randint(50,80)
        self.ProblemSovling = random.randint(50,80)
        self.stance = []
        for i in range (5):
            self.stance.append(random.randint(0,9))
    def ParticipantsDisplay(self):
        print("Participant Name: ", self.name)
        print("Participant Popularity: ", self.Popularity)
        print("Participant Critical Reasoning: ", self.CritReasoning)
        print("Participant Persuasion: ", self.Persuasion)
        print("Participant Debating: ", self.Debating)
        print("Participant Problem Solving: ", self.ProblemSovling)
        print("Participant Stance: ", *self.stance)
    def PopularityIncrease(self):
        if self.Popularity >= 90:
            self.Popularity = 100
        else:
            self.Popularity += random.randint(1,10)
    def PopularityDecrease(self):
        if self.Popularity <= 10:
            self.Popularity = 0
        else:
            self.Popularity -= random.randint(1,10)
