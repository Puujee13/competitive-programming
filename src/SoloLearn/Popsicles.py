#Auther is A.Purevsuren
#Popsicles -> Mohooldos
  #You have a box of popsicles and you want to give them all away to a group of brothers and sisters. If you
  #have enough left in the box to give them each an even amount you should go for it! If not, they will fight
  #over them, and you should eat them yourself later.

#Task
#Given the number of siblings that you are giving popsicles to, determine if you can give them each an even amount or
  #siblings - ah, duus
#if you shoudn't mention the popsicles at all.

#Input Pormat
#Two intenger values, the first one represents the number og siblings, and the second one represents the number of
#popsicles that you have left in the box

#Output Format 
#A String that says 'give away' if you are giving them away, or 'eat them yourself'
#if yo will be eating them yourself.

#Sample Input 
# 3 9

#Sample Output
#give away

#Explanation
  #You can give the popsicles to the brothers and sisters because they would each get the same amount 3.

# That's my solution
siblings = int(input())
popsicles = int(input())
if popsicles % siblings == 0:
  print('give away')
else:
  print('eat them yoursel')
