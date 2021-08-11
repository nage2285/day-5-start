#For Loop with Lists
#fruits = ["Apple", "Peach", "Pear"]

# Assigning of variable name
# Since there are three items in the list, for loop will run 3 times
#for fruit in fruits:
 # print(fruit)
  #print(fruit + " Pie" )
  #print(fruit + " chaat")
  #print(fruits)

#This will not be part of the for loop
#print(fruits)

#Using for loop with range function

# Range Function (shows 1-9). Here 2 is the stepsize

#for number in range(1, 11, 2):
#  print(number)

# Gauss adding first 100 numbers 
total = 0
for number in range(1,101):
  total = total + number
  #print(total)
print(total)

#adding even numbers in first 100 

#Remember variable has to be defined intially
total = 0
for number in range(1, 101):
  if (number % 2 == 0):
    total = total + number
print(total)

