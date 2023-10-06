class Division:
    def __init__(self, division_no, issues, participants):
        self.division_no = division_no
        self.issues = issues
        self.participants = participants
    def DivisionDisplay(self):
        print("Division Number: ", self.division_no)
        print("Division Issues: ", end=" ")
        for i in range(len(self.issues)):
            if i == len(self.issues)-1:
                print(self.issues[i].name,  self.issues[i].approach, end=" ")
            else:
                print(self.issues[i].name, self.issues[i].approach, end=", ")
        print("\nDivision Participants: ", end=" ")
        for i in range(len(self.participants)):
            if i == len(self.participants)-1:
                print(self.participants[i].name, end=" ")
            else:
                print(self.participants[i].name, end=", ")
        print("\n --------------------")
# Division 1
