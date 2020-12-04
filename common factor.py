

def common(a,b):
    count = 0
    min = a if a< b else b
    for i in range(1,min+1):
        if a % i == 0 and b % i == 0:
            count = count + 1

    return count

no = list(map(int,input().split()))
number1 = no[0]
number2 = no[1]
print(common(number1, number2))