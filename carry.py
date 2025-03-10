

def findCarry(num1, num2):
    carry = 0
    count = 0
    while(num1>0 and num2>0):
        sum = num1%10 + num2%10 +carry
        carry = sum//10
        if(carry == 1):
            count = count+1
        num1 = num1//10
        num2 = num2//10
    print(count)

findCarry(234, 387)
