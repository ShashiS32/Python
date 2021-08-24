name = input("Whats your name ")

print(len(name))

a = input("a:")

b = input("b:")

c = a

a = b

b = c

print(("a = " + a))

print("b = " + b)

print(len("35452089"))
print("Hello"[4])


a = float(123)
print(type(a))
print(150 + float(a))


two_digit_number = input("Type a 2 digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print("result is " + str(result))

print("bmi clac")
height = input("enter your height in meters ")
weight = input("enter your weight in KG ")
BMI = (float(weight) / (float(height)**2))
bmi = round(BMI)
print(bmi)
