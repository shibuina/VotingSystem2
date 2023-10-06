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
    def MainDisplay(self):
        print("Number of Divisions: ", self.divisions_num)
        print("Number of Days: ", self.days_num)
    def ProceedingDays (self,days_num):
        for i in range(days_num):
            print("Day: ", i+1)
        for i in range(self.divisions_num):
            print("Division: ", i+1)

main = Main()


# democrats = Party("Democrats", "Joe Biden", [], [])
# republicans = Party("Republicans", "Donald Trump", [], [])
# libertarian = Party("Libertarian", "Ron Paul", [], [])
# democrats.PartyDisplay()
# republicans.PartyDisplay()
# GLBW = Issue(10)
# print(GLBW.approach)
# Issue.IncreaseApproach(GLBW)
# print(GLBW.approach)
# GJ = Participants("Gary Johnson")
# GJ.ParticipantsDisplay()
# GJ.PopularityIncrease()
# GJ.ParticipantsDisplay()