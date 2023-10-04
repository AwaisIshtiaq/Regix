import re
# findall
user = input("Enter something! ")
x= re.findall("in",user)
print(x)

# search
user2 = input("enter a name :")
x = re.search('this',user2)
x.start()

# split
user3 = input("Enter something!")
a = re.split("a",user3)
print(a)

# sub
user4 = input("enter a some thing!")
b = re.sub("a","10",user4,2)
print(b)

# Special Sequences
# \A
user5 = input("enter a smoething!")

x = re.findall("\AThe" , user5)
print(x)

# \b
user6 = input("Enter something!")

x = re.findall(r"\bin",user6)
print(x)
# \B
user7 = input("enter a something!")
x =re.findall(r"\Bhis",user7)
print(x)

# \D
user8 = input("enter a something!")
a = re.findall("\D",user8)
print(a)

# \S
user9 = input("enter a something!")
x = re.findall("\S",user9)
print(x)

# \w
user10 = input("enter a something!")
x = re.findall("\w",user10)
print(x)

# \Z
user11 = input("enter a somthing!")
x = re.findall("\W",user11)
print(x)
