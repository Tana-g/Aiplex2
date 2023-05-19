#WAPP fibonacci series
nth = int(input("enter how many numbers u requied:"))
n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
print(n1, n2)
for i in range(nth-2):
    res = n1+n2
    n1 = n2
    n2 = res
    print(res, end=", ")

#WAPP  multiplication table program
n = int(input("enter you required mul table:"))
for i in range(1, 11):
    print(n,"*",i,"=", n*i)

#2nd method
t = int(input("enter mul table no:"))
for t in range(1, t+1):
    for s in range(1, 11):
        print(t,"*", s, "=", t*s)

#WAPP ArmStrong number program
n = int(input("enter a number:"))
init = 0
temp = n
while temp>0:
    digit = temp%10
    init += digit**3
    temp //= 10
if n == init:
    print(n, "ArmStrong Number")
else:
    print(n, "Not a ArmStrong Number")

#WAPP Prime Numbers Program
n = int(input("enter how many prime numbers u want:"))
i = 2
no_of_primes = 0
flag=True
if n>0 :
    while flag :
        c=0
        for j in range(1,i+1):
            if i%j == 0:
                c += 1
        if c==2:
            print(i)
            no_of_primes += 1
        if no_of_primes != n:
            i += 1
        else:
            flag = False
else:
    print("n value should be greater then zero")


#WAPP length of string
s = input("enter a string:")
count = 0
for i in s:
    count += 1
print(count)

#WAPP find sum of digits and check palindrome
n = int(input("enter a palindrome number:"))
temp = n
sum = 0
while n>0:
    digit = n%10
    sum += digit
    n = n//10
print(sum)
temp = "%s"%temp
if temp == temp[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#WAPP to convert number into charecter
list_10=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN']
n = int(input("enter a number:"))
if n >= 0:
    print(list_10[n])
else:
    print("please enter between 1~10 numbers")

#2nd method print numbers[1~100]
list_20=['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','ELEVEN','TWELE','THIRTEEN','FOURTEEN','FIFTEEN','SIXTEEN','SEVENTEEN','EIGHTEEN','NINTEEN','TWENTY']
list_90=['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY','SEVENTY','EIGHTY','NINTY','ONE-HUNDRED']
output = ''
n = int(input("enter a number:"))
if n <= 0:
    output=(list_20[n])
elif n <= 100:
    output = ((list_90[n//10])+" "+(list_20[n%10]))
else:
    print("please enter valid number")
print(output)

#3rd method
list_10=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
def number_2_word(n):
    if (n == 0):
        return ""
    else:
        small_ans = list_10[n%10]
        ans=number_2_word(int(n//10))+small_ans+" "
    return ans
n = int(input("enter a number:"))
print(number_2_word(n))

#WAPP convert decimal to binary
def decimal_2_binary(n):
    if n >= 1:
        decimal_2_binary(n//2)
        print(n%2,end=" ")
ans = decimal_2_binary(int(input("enter a number:")))

#WAPP binary to decimal number
def binary_2_decimal(num):
    decimal = 0
    power = 1
    while num>0:
        rem = num%10
        num = num//10
        decimal += rem*power
        power = power*2
    return decimal
print(binary_2_decimal(int(input("enter a binary number:"))))

#WAPP check perfect number or not
n = int(input("enter anumber:"))
count = 0
for i in range(1,n):
    if (n%i==0):
        count += i
if n == count :
    print("perfect")
else:
    print("not a perfect number")

#WAPP to print duplicate charecter ina string
s = input("enter a string:")
s1 = ""
for i in s:
    if i in s1:
        print(i)
    else:
        s1 += i