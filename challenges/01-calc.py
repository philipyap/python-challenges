# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

def cal():
         ques=input("what cal you like ? (add, sub, mul, div)")
         num3=input("what is your number 1 ")
         num4=input("what is your number 2 ")
         if ques == "add" :
             result =  int(num3) + int(num4)
         elif ques == "sub" :
             result =  int(num3) - int(num4)
         elif ques == "mul":
             result = int(num3) * int(num4)
         elif ques == "div":
             result =  int(num3) / int(num4)
         return result
print(cal())