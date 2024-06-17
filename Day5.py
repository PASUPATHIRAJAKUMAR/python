#Average Height

student_heights = input("Enter a students height:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for heights in student_heights:
  total_height+= heights
print(f"total height = {total_height}")

number_of_students = 0
for num_students in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

#Highest Score
students_score = input("Enter a students score:").split()
for n in range(0, len( students_score)):
  students_score[n] = int( students_score[n])

highest_score = 0
for score in students_score:
  if score>highest_score:
    highest_score = score
print(f"The Highest score is =  {highest_score}")

# Add Even Number
target = int(input("Enter a target:"))
even = 0
for number in range(2,target+1,2):
    even+=number
print(even)

#Fizz Buzz
target = 100
for num in range(1,target+1):
  if num%3== 0 and num%5==0:
    print("FizzBuzz")
  elif num%3==0:
    print("Fizz")
  elif num%5==0:
    print("Buzz")
  else:
    print(num)

#Random Password Generator
import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
"p","q","r","s","t","u","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","$","#","5","&","*"]
print("Welcome to Password Generator")
nr_letters = int(input("How many letters do you want?"))
nr_numbers = int(input("How many numbers do you want?"))
nr_symbols = int(input("How many symbols do you want?"))

#Easy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list+=random.choice(letters)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")