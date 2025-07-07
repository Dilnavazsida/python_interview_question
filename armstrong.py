def fun(n):

    sum = 0
    temp = n  
    while n>0:
        r = n%10
        sum+= r*r*r
        n = n//10

    if temp == sum:
        return "number is armstrong "
    else:
        return "number is not armstrong "

n = int(input("Enter number "))


print(fun(n))