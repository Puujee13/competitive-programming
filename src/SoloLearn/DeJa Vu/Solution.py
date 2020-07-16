letters = input()
isUnique = 1
for i in range(0, len(letters)):
  for j in range(0, len(letters)):
    if i != j:
      if letters[i] == letters[j]:
        isUnique = 0
if isUnique == 0:
  print('Deja Vu')
else:
  print('Unique')