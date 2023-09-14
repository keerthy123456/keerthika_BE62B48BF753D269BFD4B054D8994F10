# Implement a recursive function to calculate the factorial of a given number.
"""
1! = 1 * 1
2! = 2 * 1! --->2 * 1
3! = 3 * 2! --->3 * 2 * 1
"""
def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number = int(input("Enter a value :"))
res = fact_rec(number)

print("The factorial of {} is {} .".format(number,res))




# Leap Year

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""
def isLeapYear(year):
  if (year % 4==0 and year % 100 != 0) or year % 400 ==0:
    return True
  else:
    return False

year = int(input("Enter a year : "))

if isLeapYear(year):
  print('{} is a leap year .'.format(year))
else:
  print('{} is not a leap year.'.format(year))
  