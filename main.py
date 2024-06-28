import random as rm

n = rm.randint(0,100)
a = -1
guesses = 0

while (a != n):
  guesses +=1
  a = int(input("Guess The Num : "))
  
  if (a<n):
    print("Higher Num Please")
  else:
      print("Lower Num Please")  
      
print(f"You Have Guess the num {n} correctly in {guesses} attempt")  
  