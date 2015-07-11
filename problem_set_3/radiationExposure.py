def createSubRange(start, stop, step):
    if step >= stop-start:
        return [start,stop]
    else:
        return [start] + createSubRange(start+step, stop,step)
        
def getArea(f, I):
    if len(I)<3:
        return (I[1]-I[0])*f(I[0])
    else:
        return (I[1]-I[0])*f(I[0]) + getArea(f, I[1:])

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    I = createSubRange(start, stop, step)
    return getArea(f, I)
