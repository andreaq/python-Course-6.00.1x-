# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        self.word = self.word.lower()
        punctuation = list(string.punctuation)
        sentence = ""
        for char in text:
            if char in punctuation:
                char = " "
            sentence += char 
        words = sentence.split()  
        for item in words:
            item = item.lower()      
            if item == self.word:     
                return True
        return False


# TODO: TitleTrigger
class TitleTrigger(WordTrigger):            
    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getTitle())

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    
    def isWordIn(self, text):
        self.word = self.word.lower()
        punctuation = list(string.punctuation)
        sentence = ""
        for char in text:
            if char in punctuation:
                char = " "
            sentence += char 
        words = sentence.split()  
        for item in words:
            item = item.lower()      
            if item == self.word:     
                return True
        return False


# TODO: TitleTrigger
class TitleTrigger(WordTrigger):            
    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getTitle())
        
        
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):       
    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getSubject())
        
        
# TODO: SummaryTrigger 
class SummaryTrigger(WordTrigger):          
    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getSummary())        

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self, story):
        if self.phrase in story.getTitle():
            return True
        if self.phrase in story.getSubject():
            return True
        if self.phrase in story.getSummary():
            return True
        return False
        

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    storyList = []
    for trigger in triggerlist:
        for story in stories:
            if trigger.evaluate(story):
                if story not in storyList:
                    storyList.append(story)
    return storyList
