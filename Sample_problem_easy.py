option1=10000+1000 ## bonus added
option2=10000
year=0 
print("Year Option 1 Option 2")
while option2<option1:
    print(str(year)+" "+str(option1)+" "+str(option2))
    option1=option1+0.1*option1
    power=12*(year+1)
    print(power)
    monthlyrate=10/1200
    multiplier=(1+(monthlyrate))**float(power) # '**' is the operation for the power ('^') symbol
    option2=10000*multiplier
    year=year+1

print(str(year)+" "+str(option1)+" "+str(option2))

# this question uses compound interest formula
# the formula for the monthly compound interest is : A=P(1+r/12)^12t where t is years and r is the annual rate
# these formulas will be given to you during the competition
