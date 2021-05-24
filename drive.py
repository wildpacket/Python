drive.py

#if and else statement

print(" So you want to drive, you have to be old enough first.")
age = int(input("what is your age?"))

if (age > 17 and age < 60):
  print("you are old enough to drive, go for it.")
else:
  print("hold your horses, your not old enough to drive yet!")