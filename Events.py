import random
class Events:
    def __init__(self):
        self.happening = random.randint(1,100)
        self.type = random.randint(1,4)
    def DebateEvent(self,FirstPartyP,FirstPartyT,SecondPartyP,SecondPartyT,ThirdPartyP,ThirdPartyT):
        score = [0,0,0]
        score[0] = 0.5*FirstPartyP.Popularity + 0.6*FirstPartyP.CritReasoning + 0.6*FirstPartyP.Persuasion + 0.8*FirstPartyP.Debating + 0.4*FirstPartyT.preparation + 0.3*FirstPartyT.creativity
        score[1] = 0.5*SecondPartyP.Popularity + 0.6*SecondPartyP.CritReasoning + 0.6*SecondPartyP.Persuasion + 0.8*SecondPartyP.Debating + 0.4*SecondPartyT.preparation + 0.3*SecondPartyT.creativity
        score[2] = 0.5*ThirdPartyP.Popularity + 0.6*ThirdPartyP.CritReasoning + 0.6*ThirdPartyP.Persuasion + 0.8*ThirdPartyP.Debating + 0.4*ThirdPartyT.preparation + 0.3*ThirdPartyT.creativity
        if score[0] > score[1] and score[0] > score[2]:
            return 1
        elif score[1] > score[0] and score[1] > score[2]:
            return 2
        elif score[2] > score[0] and score[2] > score[1]:
            return 3
        else:
            return 0
    def CanRelEvent (self,candidates):
        results = [0,0,0]
        threshold = random.randint(1,100)
        for i in range (len(candidates)):
            if candidates[i].ProblemSovling >= threshold:
                results[i] = 1
        return results
    def LeadRelEvent (self,leaders):
        results = [0,0,0]
        threshold = random.randint(1,100)
        for i in range (len(leaders)):
            if leaders[i].Persuasion >= threshold:
                results[i] = 1
        return results
    def PosIssueRelEvent (self,issues):
        results = [0]*len(issues) 
        threshold = random.randint(1,100)
        for i in range (len(issues)):
            if threshold >= 51:
                results[i] = 1
        return results
    def NegIssueRelEvent (self,issues):
        results = [0]*len(issues)        
        threshold = random.randint(1,100)
        for i in range (len(issues)):
            if threshold >= 51:
                results[i] = 1
        return results
