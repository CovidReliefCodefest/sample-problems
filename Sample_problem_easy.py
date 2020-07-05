option1=11000
option2=10000
year=0
print("Year\t\t\tOption 1\t\t\tOption 2")
while option2<option1:
    print(str(year)+"\t\t\t"+str(option1)+"\t\t\t"+str(option2))
    option1=option1+0.1*option1
    power=12*(year+1)
    print(power)
    monthlyrate=10/1200
    multiplier=(1+(monthlyrate))**float(power)
    option2=10000*multiplier
    year=year+1

p
rint(str(year)+"\t\t\t"+str(option1)+"\t\t\t"+str(option2))



