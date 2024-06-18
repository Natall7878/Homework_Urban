import random
def one():
  key_1 = [i for i in range(3, 21)]
  key = random.choice(key_1)
  return key

result = []

n = int(one())
print (n)

for i in range(1, n):
  
  for j in range (i+1, n):
   
    if n % (int(i)+int(j)) == 0:  
        result.append(i)
        result.append(j)

print(*result)  
