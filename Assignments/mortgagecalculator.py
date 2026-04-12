principal =float(input("Enter any amount:"))
print(principal)

rate = float(input("Enter intrest rate:"))
print(rate)

duration= float(input("Enter the period of time:"))
print(duration)

rate_1 = (rate/100) / 12
result = principal*(1 + rate_1)**duration
print(result)
