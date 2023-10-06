class Party:
    def __init__(self, name, leader, candidates, team):
        self.name = name
        self.leader = leader
        self.candidates = candidates
        self.team = team
    def PartyDisplay(self):
        print("Party Name: ", self.name)
        print("Party Leader: ", self.leader)
        for candidates in self.candidates:
            print("Party Candidates: ", self.candidates)
        print("Party Team: ", self.team)

