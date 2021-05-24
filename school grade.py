school grade.py

import time
for i in range(0,100):
  grade=float(input("what is your grade?:"))
  if grade >=90:
    print("you got an A*, thats amazing, its over 90%")
  elif 80<=grade<90:
    print("you got a A, great work, thats over 80%")
  elif 70<=grade<80:
    print("you got a B, you should feel so proud, thats over 70%")
  elif 60<=grade<70:
    print("you got a C, great work, thats over 60%")
  elif 50<=grade<60:
    print("you got a D, good try thats over 50%")
  else: 
    print("you need to try harder")
  time.sleep(1)
  break