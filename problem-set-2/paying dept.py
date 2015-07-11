j=0
while True:
    b = balance
    min_monthly_pay = j*10
    for i in range(1,13):
        b = (b-min_monthly_pay)*(1+annualInterestRate/12)
    if b<=0:
        break
    j+=1

print "Lowest Payment: {}".format(min_monthly_pay)
