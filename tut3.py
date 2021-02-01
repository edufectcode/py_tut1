#Code Exercise 1
name = input("Enter name ")
course = input("Enter course ")
s1 = name+", Good morning. Welcome to the "+course+" course."
print(s1)

#Code Exercise 2
name = input("Enter name ")
name = name.replace("  "," ")
spLoc = name.find(" ")
firstName = name[0:spLoc]
lastName = name[(spLoc+1):]
print("Firstname =",firstName)
print("Lastname =",lastName)
initials = firstName[0]+lastName[0]
print("Initials =",initials)

#Code Exercise 3

s1 = input("Enter the expression : ")
s1 = s1.replace(" ","")
print(s1)
plus = s1.find("+")
num1 = int(s1[0:plus])
num2 = int(s1[(plus+1):])
sum = num1+num2
print("Number 1 =",num1)
print("Number 2 =",num2)
print("Sum =",sum)
