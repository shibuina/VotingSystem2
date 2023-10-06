from Teams import *
from Participants import *
class Party:
    def __init__(self, name, leader, candidates, team):
        self.name = name
        self.leader = leader
        self.candidates = candidates
        self.team = team
    def PartyDisplay(self):
        print("Party Name: ", self.name)
        self.leader.LeaderDisplay()
        for candidates in self.candidates:
            candidates.ParticipantsDisplay()
        print(f"Party Team Preparation: {self.team.preparation}, Party Team Preparation: {self.team.creativity}")
        print("--------------------")

