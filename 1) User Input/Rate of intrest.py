#WAP to find total amount
p=float(input("Enter Principle Amount"))
r=float(input("Enter rate of intrest"))
t=int(input("Enter time period"))
amount=p*(1+(r/100))**t
print("Total Amount",str(amount))
