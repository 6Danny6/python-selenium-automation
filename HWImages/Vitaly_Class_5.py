def factorial(n):   #talk to dad for beter explaniation
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
result = factorial(number)
print(result)


#if we say 5 then it execute 5 times for example 5*4*3*2*1
# technically (n) which equals to 5 during this example.

#________________________________________________________________________________________________________________________________________________

#Sum of 3 digit number examples

def sum_of_three(n):
    result = 0
    while n != 0:
        result = result + (n % 10)
        n = n // 10 #257/10 = 25
    return result

number = 257
result = sum_of_three(number)
print(result)

#___________________________________________________________________________________________________________________________________________________
#Leap year code

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year}is a leap year')
        else:
            print(f'{year}is not a leap year')
    else:
        print(f'{year}is not a leap year')


#2017 is not a leap year
#1900 is not a learp year
#2012 is a leap year
#2000 is a leap year

is_leap_year(2017)
is_leap_year(1900)
is_leap_year(2012)
is_leap_year(2000)