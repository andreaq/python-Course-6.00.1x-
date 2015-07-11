low = balance/12
high = (balance*(1+annualInterestRate/12)**12)/12.0
ans = (low+high)/2

b = balance
while abs(b)>=0.01:
    b = balance
    for i in range(1,13):
        b = (b-ans)*(1+annualInterestRate/12)
    if b>0:
        low = ans
    if b<0:
        high=ans
    ans = (low+high)/2
    
print "Lowest Payment: {}".format(round(ans,2))
