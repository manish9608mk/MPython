# ex - 1
n = 3

while n > 0:
  print(n)
  n = n - 1

print('Go!\n')




'''
Interview Tip: 
Jab bhi while loop dekho, apne aap se ye 3 questions pucho:

1. Condition kya hai?

while n != 1

2. Condition ko false kaun banayega?

n = n // 2
n = n * 3 + 1

3. Kya guarantee hai ki condition ek din false hogi?

Agar answer "yes" hai → finite loop.
Agar answer "no" ya "unknown" hai → infinite loop ka risk hai.
'''
