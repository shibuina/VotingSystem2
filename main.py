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
        parties.append(Party("Democrats", Leader("Joe Biden"), [], DemocratsT))
        parties.append(Party("Republicans", Leader("Donald Trump"), [], RepublicansT))
        parties.append(Party("Libertarian", Leader("Ron Paul"), [], LibertarianT))
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
            divisions.append(Division(i+1,main.IssueSetup(),[]))
        for i in range(self.divisions_num):
            for j in range(3):
                divisions[i].participants.append(parties[j].candidates[i])
        return parties,divisions
    def IssueSetup (self):
        issues = []
        issues.append(Issue("Global Warming",7))
        issues.append(Issue("Education",8))
        issues.append(Issue("Army",5))
        issues.append(Issue("Economics",7))
        issues.append(Issue("Globalization",6))
        return issues
    def ProceedingDays (self,parties,divisions):
        for i in range(self.days_num):
            print("Day: ", i+1)
            for i in range(self.divisions_num):
                event = Events()
                event.EventHappening(parties,divisions[i])
            self.DaysDisplay(parties,divisions)
    def DaysDisplay(self,parties,divisions):
        for i in range(self.days_num):
            print("Day: ", i+1)
            for i in range (3):
                parties[i].PartyDisplay()
            for i in range(self.divisions_num):
                divisions[i].DivisionDisplay()
    def DisplayBeginning(self,parties,divisions):
        for i in range (3):
                parties[i].PartyDisplay()
        for i in range(self.divisions_num):
            divisions[i].DivisionDisplay()
    def StancePoints(self,parties,division):
        points = [0]*3
        for i in range(3):
            for k in range(5):
                points[i] += 0.5*(division.participants[i].stance[k] - division.issues[k].approach)**2
            points[i] += division.participants[i].Popularity*0.2 + parties[i].leader.popularity*0.3
        return points
    def FinalVoting(self,parties,divisions):
        #report
        self.DisplayBeginning(parties,divisions)
        #voting scores
        people_no = self.divisions_num
        parliament_people = [0]*3
        for i in range(self.divisions_num):
            points = main.StancePoints(parties,divisions[i])
            print("Division ", i+1)
            print("Voting Scores: ", points)
            print("The winner is: ", parties[points.index(max(points))].name)
            print("--------------------")
            if points.index(max(points)) == 0:
                parliament_people[0] += 1
            elif points.index(max(points)) == 1:
                parliament_people[1] += 1
            else:
                parliament_people[2] += 1
        for i in range(3):
            if parliament_people[i] > people_no/2:
                print("The winner of the elections is: ", parties[i].name)
                print("the new leader ís: ", parties[i].leader.nam,"!")
                print("--------------------")   
                quit()
        print("A hung parliament should be formed!")
        print("--------------------")   
main = Main()
parties = main.Setup()[0]
divisions = main.Setup()[1]
#Display at the beginning
main.DisplayBeginning(parties,divisions)
main.ProceedingDays(parties,divisions)
main.FinalVoting(parties,divisions)