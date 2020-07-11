def revDigits(num) : # function for reversing digits
    rev_num = 0;
    while(num > 0):
        rev_num = rev_num*10 + num%10
        num = num//10 
    return rev_num

biggest=0
num1=0
num2=0
for i in range(100,1000):
    for j in range(100,1000):
        product=i*j
        if product==revDigits(product): # checking palindrome condition
            if product>biggest:
                biggest=product
                num1=i
                num2=j
                
print("Answer is : "+str(biggest))  # 906609

print("From numbers : ", str(num1),str(num2))  # 913, 993

# '%' refers to the modulus(mod) operation and '//' refers to getting the quotient 
