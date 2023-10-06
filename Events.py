import select
from Divisions import *
from Party import *
import random
class Events:
    def __init__(self):
        self.happening = random.randint(1,100)
        self.type = random.randint(1,4)
        self.subtype = random.randint(1,2)
        self.corresponding_participants = random.randint(1,3)
        self.corresponding_issues = random.randint(1,5)
    def DebateEvent(self,parties,division):
        score = [0,0,0]
        score[0] = 0.5*division.participants[0].Popularity + 0.6*division.participants[0].CritReasoning + 0.6*division.participants[0].Persuasion + 0.8*division.participants[0].Debating + 0.4*parties[0].team.preparation + 0.3*parties[0].team.creativity
        score[1] = 0.5*division.participants[1].Popularity + 0.6*division.participants[1].CritReasoning + 0.6*division.participants[1].Persuasion + 0.8*division.participants[1].Debating + 0.4*parties[1].team.preparation + 0.3*parties[1].team.creativity
        score[2] = 0.5*division.participants[2].Popularity + 0.6*division.participants[2].CritReasoning + 0.6*division.participants[2].Persuasion + 0.8*division.participants[2].Debating + 0.4*parties[2].team.preparation + 0.3*parties[2].team.creativity
        if score[0] > score[1] and score[0] > score[2]:
            return 1
        elif score[1] > score[0] and score[1] > score[2]:
            return 2
        elif score[2] > score[0] and score[2] > score[1]:
            return 3
        else:
            return 0
    def CanRelEvent (self,parties,division):
        if self.subtype == 1:
            return 1
        else:
            return -1
    def LeadRelEvent (self,parties,division):
        if self.subtype == 1:
            return 1
        else:
            return -1
    def IssueRelEvent (self,parties,division):
        if self.subtype == 1:
            return 1
        else:
            return -1
    def EventHappening(self,parties,division):
        if self.happening >= 51:
            if self.type == 1:
                print(f"There is a debate today in division {division.division_no}!")
                if self.DebateEvent(parties,division) == 1:
                    print("The Democratic Party won the debate!")
                    division.participants[0].PopularityIncrease()
                    division.participants[1].PopularityDecrease()
                    division.participants[2].PopularityDecrease()
                elif self.DebateEvent(parties,division) == 2:
                    print("The Republican Party won the debate!")
                    division.participants[1].PopularityIncrease()
                    division.participants[0].PopularityDecrease()
                    division.participants[2].PopularityDecrease()
                elif self.DebateEvent(parties,division) == 3:
                    print("The Libertarian Party won the debate!")
                    division.participants[2].PopularityIncrease()
                    division.participants[0].PopularityDecrease()
                    division.participants[1].PopularityDecrease()
                else:
                    print("No one won the debate!")
                print("--------------------")
            elif self.type == 2:
                print(f"There is an Event today in division {division.division_no}!")
                if self.CanRelEvent(parties,division) == -1:
                    if self.corresponding_participants == 1:
                        print("The candidate ", division.participants[0].name, " from the Democratic Party was caught in a scandal!")
                        division.participants[0].PopularityDecrease()
                    elif self.corresponding_participants == 2:
                        print("The candidate ", division.participants[1].name, " from the Republican Party was caught in a scandal!")
                        division.participants[0].PopularityDecrease()
                    else:
                        print("The candidate ", division.participants[2].name, " from the Libertarian Party was caught in a scandal!")
                        division.participants[0].PopularityDecrease()
                else: 
                    if self.corresponding_participants == 1:
                        print("The candidate ", division.participants[0].name, " from the Democratic Party contributed to the community!")
                        division.participants[0].PopularityIncrease()
                    elif self.corresponding_participants == 2:
                        print("The candidate ", division.participants[1].name, " from the Republican Party contributed to the community!")
                        division.participants[0].PopularityIncrease()
                    else:
                        print("The candidate ", division.participants[2].name, " from the Libertarian Party contributed to the community!")
                        division.participants[0].PopularityIncrease()
                print("--------------------")
            elif self.type == 3:
                print(f"There is an Event today in division {division.division_no}!")
                if self.LeadRelEvent(parties,division) == -1:
                    if self.corresponding_participants == 1:
                        print("The leader from the Democratic Party was caught in a scandal!")
                        parties[0].leader.PopularityDecrease()
                    elif self.corresponding_participants == 2:
                        print("The leader from the Republican Party was caught in a scandal!")
                        parties[1].leader.PopularityDecrease()
                    else:
                        print("The leader from the Libertarian Party was caught in a scandal!")
                        parties[2].leader.PopularityDecrease()
                else:
                    if self.corresponding_participants == 1:
                        print("The leader from the Democratic Party contributed to the community!")
                        parties[0].leader.PopularityIncrease()
                    elif self.corresponding_participants == 2:
                        print("The leader from the Republican Party contributed to the community!")
                        parties[1].leader.PopularityIncrease()
                    else:
                        print("The leader from the Libertarian Party contributed to the community!")
                        parties[2].leader.PopularityIncrease()
                print("--------------------")
            else:
                print("There is an Event today in division ", division.division_no)
                if self.IssueRelEvent(parties,division) == 1:
                    if self.corresponding_issues == 1:
                        print("The issue Global Warming approach has been changed!")
                        division.issues[0].IncreaseApproach()
                    elif self.corresponding_issues == 2:
                        print("The issue Education approach has been changed!")
                        division.issues[1].IncreaseApproach()
                    elif self.corresponding_issues == 3:
                        print("The issue Army approach has been changed!")
                        division.issues[2].IncreaseApproach()
                    elif self.corresponding_issues == 4:
                        print("The issue Economics approach has been changed!")
                        division.issues[3].IncreaseApproach()
                    else:  
                        print("The issue Globalization approach has been changed!")
                        division.issues[4].IncreaseApproach()
                else:
                    if self.corresponding_issues == 1:
                        print("The issue Global Warming approach has been changed!")
                        division.issues[0].DecreaseApproach()
                    elif self.corresponding_issues == 2:
                        print("The issue Education approach has been changed!")
                        division.issues[1].DecreaseApproach()
                    elif self.corresponding_issues == 3:
                        print("The issue Army approach has been changed!")
                        division.issues[2].DecreaseApproach()
                    elif self.corresponding_issues == 4:
                        print("The issue Economics approach has been changed!")
                        division.issues[3].DecreaseApproach()
                    else:  
                        print("The issue Globalization approach has been changed!")
                        division.issues[4].DecreaseApproach()
                print("--------------------")
        else:
            print("There is no event today!")
            print("--------------------")
