joke.py

print("Do you want to hear a joke?")
def joke(jokeOption):
  #jokeOption = int(input("Select a number: 1,2,3,4 or 5: "))

  if (jokeOption==1):
    print("Why did the scarecrow win an award? ... because he was outstanding in his field")
  elif(jokeOption==2):
    print("Did you hear about the restaurant on the moon? ... great food, no atmosphere.")
  elif(jokeOption==3):
    print("How do you make a tissue dance? ... put a little boogie in it")
  elif(jokeOption==4):
    print("just had an opperation on my funny bone. Doctor said i will be in stitches for 2 weeks.")
  elif(jokeOption==5):
    print("what do you get when you cross a snowman with a vampire? ... frostbite")
  
jokeOption = int(input("Select a number: 1,2,3,4 or 5: "))
joke(jokeOption)

print("Hope i made you smile")
