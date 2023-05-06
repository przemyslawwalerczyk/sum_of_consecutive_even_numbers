n = int(input("Please enter how many consecutive even numbers you want to add: "))

sum = 0
element = 2

for i in range(n):
  sum = sum + element
  element = element + 2

print("The sum of", n, "consecutive even numbers is.", sum)
