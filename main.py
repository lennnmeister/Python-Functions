def convert(miles):
  return miles * 1.6

print(convert(2))




"""

def f():
  print("ha")
  print("haha")

f()
f()


##


#mapping with input or argument x

def f1(x):
  return 2 * x

a = f1(3)

print(a)


##


#function w multiple input/arguments

def f3(x, y):
  return x + y

a = f3(1, 3)

print(a)


##


def f4(x):
  print(x)
  print("still in this function")
  return 3 * x

f = f4(6)
print(f)
print(f4(8))


##


# without return in function

def f5(some_arg):
  print("weee")
  print(some_arg)

f5(5)


##


# Create a BMI Calculator
n1 = "Keith"
w1 = 60
h1 = 1.7

n2 = "Tim"
w2 = 90
h2 = 1.8

n3 = "JJ"
w3 = 80
h3 = 2

def bmi_calculator(n, height, weight):
  bmi = weight / (height ** 2)
  print("BMI: ")
  print(bmi)
  if bmi <= 25:
    return n + " is not overweight."
  else:
    return n + " is overweight."

r1 = bmi_calculator(n1, h1, w1)
r2 = bmi_calculator(n2, h2, w2)
r3 = bmi_calculator(n3, h3, w3)

print(r1)
print(r2)
print(r3)

"""
