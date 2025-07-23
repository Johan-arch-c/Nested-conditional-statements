driving_concent=input("are you alowed to drive y or n")
age=int(input("enter your age:"))


if driving_concent=='y':
  print("you are allowed")
else:
 if age>=16:
  print("allowed")
 else:
  print("not allowed")