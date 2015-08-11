# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
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

class TitleTrigger(WordTrigger):            
    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getTitle())
        
# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, other):
        self.other = other
    def evaluate(self, story):
        return not self.other.evaluate(story) 
    
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def evaluate(self, story):
        return self.first.evaluate(story) and self.second.evaluate(story)


# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def evaluate(self, story):
        return self.first.evaluate(story) or self.second.evaluate(story)
