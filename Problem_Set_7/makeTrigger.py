# Enter your code for makeTrigger in this box
def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    string=""
    triggerType= triggerType.lower().capitalize()
    if triggerType == "Title":
        trigger = TitleTrigger(params[0])
        triggerMap[name] = trigger
    elif triggerType == "Subject":
        trigger = SubjectTrigger(params[0])
        triggerMap[name] = trigger
    elif triggerType == "Summary":
        trigger = SummaryTrigger(params[0])
        triggerMap[name] = trigger
    elif triggerType == "Not":
        trigger = NotTrigger(triggerMap[params[0]])
        triggerMap[name] = trigger
    elif triggerType == "And":
        trigger = AndTrigger(triggerMap[params[0]],triggerMap[params[1]])
        triggerMap[name] = trigger
    elif triggerType == "Or":
        trigger = OrTrigger(triggerMap[params[0]],triggerMap[params[1]])
        triggerMap[name] = trigger
    elif triggerType == "Phrase":
        for item in params:
            string += item+" "
        trigger = PhraseTrigger(string[0:-1])
        triggerMap[name] = trigger
    return trigger
