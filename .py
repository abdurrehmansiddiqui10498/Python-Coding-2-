#How do you check if x is a positive or negative even or odd number using nested if-else
a = int(input("enter a number:"))
if a > 0:
  if a % 2 == 0:
    print("This is a positive even number")
  elif a % 3 == 0:
    print("This is a positive odd number")
elif a < 0:
  if a % 2 == 0:
    print("This is a negative even number")
  elif a % 3 == 0:
    print("This is a negitive odd number")
else:
  print("This is zero")

#How do you print "x is a multiple of 3", "x is a multiple of 5", or "x is neither a multiple of 3 nor 5"?
x = int(input("enter a number"))
if x % 3 == 0:
 print ("x is a multiple of 3")
elif x % 5 == 0:
  print("x is a multiple of 5")
else:
  print("x is neither a multiple of 3 nor a multiple of 5")

#How do you check if a person is a child (0-12), teenager (13-19), adult (20-64), or senior (65 and above)?
age = int(input("enter your age"))
if age >= 0 and age <= 12:
  print("you are a child")
elif age >= 13 and age <= 19:
  print("You are a teenager")
elif age >= 20 and age <= 64:
  print("You are an adult")
elif age >= 65:
  print("you are a senior")

#How do you determine the grading of a student based on their score, where scores above 90 are 'A', between 80 and 89 are 'B', between 70 and 79 are 'C', between 60 and 69 are 'D', and below 60 are 'F'?

percentage_scored = int(input("enter a number"))
if percentage_scored >= 90:
 print("congratulations")
 print("your grade is 'A'")
elif percentage_scored <= 89 and percentage_scored>=80:
  print("Your grade is 'B'")
elif percentage_scored <= 79 and percentage_scored >=70:
  print("your grade is 'C'")
elif percentage_scored <= 69 and percentage_scored >= 60:
  print("your grade is 'D'")
elif percentage_scored < 60:
  print("Your grade is 'F'\n better luck next time")

#How do you check if a year is a leap year?

a = int(input("enter a year"))
if a % 4== 0 :
  print("This is a leap year")
else:
    print("this is not a leap year")

#How do you determine the type of a triangle based on its sides' lengths: equilateral, isosceles, or scalene?
a = int(input("enter the first side"))
b = int(input("enter the second side"))
c = int (input("enter the third side"))
if a + b + c == 180:
 print('"Answers"')
 if a != b != c:
   print("This is a scalene triangle")
 elif a <= 90 and b <= 90 and c <= 90:
    print("This is an acute angle triangle")
if a + b + c == 180:
 if a == 60 and b == 60 and c == 60:
   print("This is an equilateral triangle")
 elif a == b != c:
  print("This is an isoscles triangle")
 elif a == c != b:
   print("this is an isoceles triangle")
 elif b == c != c:
   print("this is an isoscles triangle")
