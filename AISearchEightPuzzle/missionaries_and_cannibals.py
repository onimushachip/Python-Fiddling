from search import *

class MissionariesandCannibalsState(ProblemState):
    boatLegal = None
    def __init__(self, missionariesLeft, cannibalsLeft, boat, missionariesRight, cannibalsRight):
        self.missionariesLeft = missionariesLeft
        self.missionariesRight = missionariesRight
        self.boat = boat
        self.cannibalsLeft = cannibalsLeft
        self.cannibalsRight = cannibalsRight
    def __str__(self):
        return "("+str(self.missionariesLeft)+", "+str(self.cannibalsLeft)+ ", "+str(self.boat)+ ", "+str(self.missionariesRight)+ ", "+str(self.missionariesRight)+")"
    def illegal(self):
        if self.cannibalsLeft > self.missionariesLeft: return True
        if self.cannibalsRight > self.missionariesRight: return True
        if self.cannibalsLeft < 0: return True
        if self.cannibalsRight < 0: return True
        if self.missionariesLeft < 0: return  True
        if self.missionariesRight < 0: return  True
        if self.boatLegal == False: return True
        return False
    def equals(self, state):
        return (self.missionariesRight == state.missionariesRight
                and self.missionariesLeft == state.missionariesLeft
                and self.boat == state.boat
                and self.cannibalsRight == state.cannibalsRight
                and self.cannibalsLeft == state.cannibalsLeft)
    def twoMleft(self):
        if (self.boat == "L"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft - 2,
                                                 self.cannibalsLeft,
                                                 "R",
                                                 self.missionariesRight + 2,
                                                 self.cannibalsRight)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "L",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneMleft(self):
        if (self.boat == "L"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft - 1,
                                                 self.cannibalsLeft,
                                                 "R",
                                                 self.missionariesRight + 1,
                                                 self.cannibalsRight)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "L",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneMoneCleft(self):
        if (self.boat == "L"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft - 1,
                                                 self.cannibalsLeft - 1,
                                                 "R",
                                                 self.missionariesRight + 1,
                                                 self.cannibalsRight + 1)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "L",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def twoCleft(self):
        if (self.boat == "L"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft,
                                                 self.cannibalsLeft - 2,
                                                 "R",
                                                 self.missionariesRight,
                                                 self.cannibalsRight + 2)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "L",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneCleft(self):
        if (self.boat == "L"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft,
                                                 self.cannibalsLeft - 1,
                                                 "R",
                                                 self.missionariesRight,
                                                 self.cannibalsRight + 1)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "L",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def twoMright(self):
        if (self.boat == "R"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft + 2,
                                                 self.cannibalsLeft,
                                                 "L",
                                                 self.missionariesRight - 2,
                                                 self.cannibalsRight)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "R",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneMright(self):
        if (self.boat == "R"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft + 1,
                                                 self.cannibalsLeft,
                                                 "L",
                                                 self.missionariesRight - 1,
                                                 self.cannibalsRight)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "R",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneMoneCright(self):
        if (self.boat == "R"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft + 1,
                                                 self.cannibalsLeft + 1,
                                                 "L",
                                                 self.missionariesRight - 1,
                                                 self.cannibalsRight - 1)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "R",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def twoCright(self):
        if (self.boat == "R"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft,
                                                 self.cannibalsLeft + 2,
                                                 "L",
                                                 self.missionariesRight,
                                                 self.cannibalsRight - 2)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "R",
                                             self.missionariesRight,
                                             self.cannibalsRight)
    def oneCright(self):
        if (self.boat == "R"):
            self.boatLegal = True
            return MissionariesandCannibalsState(self.missionariesLeft,
                                                 self.cannibalsLeft + 1,
                                                 "L",
                                                 self.missionariesRight,
                                                 self.cannibalsRight - 1)
        self.boatLegal = False
        return MissionariesandCannibalsState(self.missionariesLeft,
                                             self.cannibalsLeft,
                                             "R",
                                             self.missionariesRight,
                                             self.cannibalsRight)

    def operatorNames(self):
        return ["2M-Left",
                "1M-Left",
                "1M-1C-Left",
                "2C-Left",
                "1C-Left",
                "2M-Right",
                "1M-Right",
                "1M-1C-Right",
                "2C-Right",
                "1C-Right"]
    def applyOperators(self):
        return [self.twoMleft(),
                self.oneMleft(),
                self.oneMoneCleft(),
                self.twoCleft(),
                self.oneCleft(),
                self.twoMright(),
                self.oneMright(),
                self.oneMoneCright(),
                self.twoCright(),
                self.oneCright()]

# Search (MissionariesandCannibalsState(0,0,"R",3,3), MissionariesandCannibalsState(0,0,"R",3,3))
Search (MissionariesandCannibalsState(3,3,"L",0,0), MissionariesandCannibalsState(0,0,"R",3,3))




