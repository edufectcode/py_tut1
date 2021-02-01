#Code Exercise 1
num1 = input("Number 1 : ")
num2 = input("Number 2 : ")
if num1>num2:
  print("Largest =",num1)
else :
  print("Largest =",num2)

#Code Exercise 2
num1 = input("Number 1 : ")
if num1<0:
  print("Absolute Value =",-1*num1)
else :
  print("Absolute Value =",num1)

#Code Exercise 2
pwd = input("Enter password : ")
len1 = len(pwd)
if len1<5:
  print("Invalid password")
elif len1<8:
  print("Weak password")
else :
  print("Strong password")

#Code Exercise 4

quantity = 10
price = 6
amount = quantity*price

discount = 0
if amount>400:
  discount = 0.15
elif amount>200:
  discount = 0.10
elif amount>100:
  discount=0.05
else:
  discount=0

print("Bill Amount =",amount)
disValue = discount*amount
print("Discount Value =",disValue)
finalAmount = amount-disValue
print("Final Amount =",finalAmount)