


i = 0

while i < 6:
    print(i)
    i += 1


# break condition helps to get out of loop even if the condition is true
i = 1
while i < 6: 
  print(i)
  if i == 3:
    break
  i += 1


#if the continue statement occurs it will stop current iteration and start for a new one 

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#if the else statement writes it will execute code if condition is no longer true

  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


