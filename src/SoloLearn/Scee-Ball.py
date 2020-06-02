#Skee-Ball
  #You are playing a game at your local arcade, and you receive 1 ticket from the machine for every 12 points that you
  #score. You want to purchase a squirt gun with your tickets. Given your score, and the price of the squirt gun
  #(in tickets) are you able to buy it?
    #local-arcade -> togloomon mashin
    #squirt gun -> usan buu

#Task
#Evalute whether or not you have scored high enough tickets to purchase the squirt gun at the arcade

#Input Format
#The first input is an integer value that represents the points that you scored playing, and the second input is an
#intenger value that represents the cost of the squirt gun (in tickets).

#Output Format
  #A String that say 'Buy it' If you will enough tickets, or a string that says 'Try again' If you will not.

#Sample Input
# 500
# 40

#Sample Output

# Buy it!

#Explanation
  #By scoring 500 points, you will receive 41 tickets, which is enough to buy the squirt gun a at price of 40 tickets

#That's my solution

points = int(input())
cost = int(input())
yourTicket = points // 12

if yourTicket >= cost:
  print('Buy it!')
else:
  print('Try again')