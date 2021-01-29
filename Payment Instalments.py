payment = float(input("Total payment: "))
months = int(input("Total months: "))
instalment = payment*0.05
total = instalment+payment
permonth = total/months
print("Payment: %s Months: %s Instalment: %s Total payment: %s Each months, you have to pay: %s"
      % (payment,months,instalment,total,permonth))