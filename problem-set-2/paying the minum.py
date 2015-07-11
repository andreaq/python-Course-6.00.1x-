paid=[]

for i in range(1,13):
    print "Month {}:".format(i)
    min_monthly_pay = balance*monthlyPaymentRate
    paid.append(min_monthly_pay)
    balance = balance*(1-monthlyPaymentRate)*(1+annualInterestRate/12)
    print "Minimum monthly payment: {}".format(round(min_monthly_pay,2))
    print "Remaining balance: {}".format(round(balance,2))
    print " "

print "Total paid: {}".format(round(sum(paid),2))
print "Remaining balance: {}".format(round(balance,2))
