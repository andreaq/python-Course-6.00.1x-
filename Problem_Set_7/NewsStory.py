# Enter your code for NewsStory in this box
class NewsStory(object):
    def __init__(self, myGuid, myTitle, mySubject, mySummary, myLink):
        self.myGuid = myGuid
        self.myTitle = myTitle
        self.mySubject = mySubject
        self.mySummary = mySummary
        self.myLink = myLink
    
    def getGuid(self):
        return self.myGuid
    def getTitle(self):
        return self.myTitle
    def getSubject(self):
        return self.mySubject
    def getSummary(self):
        return self.mySummary
    def getLink(self):
        return self.myLink
    
