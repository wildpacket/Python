palendrome.py

# a word that is spelt the same forwards as backwards is a palendrome

print("can you think of a palendrome?")
my_str = input("Enter a word: ")

my_str = my_str.casefold()
  
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
      print("The String is a palendrome.")
else:
      print("The string is not a palendrome.")