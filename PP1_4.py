'''
  Lesson: Input and F Strings
  Author: Mikah Ho
  Date Created: Sept 19, 2024
  Date Last Modified: Sept 19, 2024
'''

def q1():
  #Write Assignment code here
  word = input("Input a word: ")
  print(word)

def q2():
  #Write Assignment code here
  firstName = input("Input your first name: ")
  print("Hello " + firstName)

def q3():
  #Write Assignment code here
  firstName = input("Input your first name: ")
  lastName = input("Input your last name: ")
  fullName = f"{lastName} {firstName}"
  print(fullName)

def q4():
  #Write Assignment code here
  student1 = input("Input a student: ")
  student2 = input("Input another student: ")
  students = f"Your students are {student1} and {student2}"
  print(students)

#Comment Out the go below when you run your test cases.
#Do not comment it out when you want to run your code normally

# q1()
# q2()
# q3()
# q4()
