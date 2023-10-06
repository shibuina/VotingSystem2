from Party import Party
from Divisions import Division
from Participants import Participants
from Events import Events
from Teams import Teams
from Leader import Leader
from Issues import Issue
class Main:
    def __init__(self):
        self.divisions_num = int(input("Enter the number of divisions: "))
        self.days_num = int(input("Enter the number of days: "))
    def Setup(self):
        #Setup for the parties and their Participants and Team
        DemocratsT = Teams()
        RepublicansT = Teams()
        LibertarianT = Teams()
        parties = []
        parties.append(Party("Democrats", "Joe Biden", [], DemocratsT))
        parties.append(Party("Republicans", "Donald Trump", [], RepublicansT))
        parties.append(Party("Libertarian", "Ron Paul", [], LibertarianT))
        with open("Democrats.txt", "r") as f:
            i = 0
            for line in f:
                if i < self.divisions_num:
                    candidate = Participants(line.strip())
                    parties[0].candidates.append(candidate)
                    i+=1
                else:
                    break
        with open("Republicans.txt", "r") as f:
            i = 0
            for line in f:
                if i < self.divisions_num:
                    candidate = Participants(line.strip())
                    parties[1].candidates.append(candidate)
                    i+=1
                else:
                    break
        with open("Libertarians.txt", "r") as f:
            i = 0
            for line in f:
                if i < self.divisions_num:
                    candidate = Participants(line.strip())
                    parties[2].candidates.append(candidate)
                    i+=1
                else:
                    break
        #Setup for the divisions
        divisions = []
        for i in range(self.divisions_num):
            divisions.append(Division(i+1,[],[]))
        for i in range(self.divisions_num):
            divisions[i].issues.append(Issue(0))
            for j in range(3):
                divisions[i].participants.append(parties[j].candidates[i])
        return parties
    def IssueSetup (self):
        issues = []
        for i in range(self.divisions_num):
            issues.append(Issue(0))
        return issues
    def ProceedingDays (self,days_num):
        for i in range(days_num):
            print("Day: ", i+1)
        for i in range(self.divisions_num):
            print("Division: ", i+1)

main = Main()
parties = main.Setup()
for party in parties:
    party.PartyDisplay()