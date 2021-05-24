print("""\
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
       *
        *
        """)

print ("Hello")
print ("What is your favourite meal, is it a roast or a pizza?")
while True:
   a = input("roast or pizza : ")
   if a == "roast":
       print("mine too!")
       break
   elif a == "pizza":
       print("I dont mind this but it is not my favourite!")
       break

