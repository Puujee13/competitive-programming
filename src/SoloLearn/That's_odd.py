#Author is A.Purevsuren.
# That's odd...
  # You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers.

  #Task:
  #Find the sum of all even intengers in a list of numbers.

  #Input Format:
  #The first input denotes the length of the list (N).
    #denotes - ilerhiileh, haruulah
  #The next N lines contain the list elements as intengers.

  #Output Format:
  #An intenger that represents the sum of only the even numbers in the list.

  #Sample Input:
  #9
  
  #1
  #2
  #3
  #4
  #5
  #6
  #7
  #8
  #9

  #Sample Output:
  #20

  #Explanation:
  #If you add together 2, 4, 6, and 8 from the list, you get a sum of 20

  #That's my solution:

numberLength = int(input()) #input is 9 or any intenger number
counter = 0

for i in range(0, numberLength):
  number = int(input())
  if number % 2 == 0: # this is even number
    counter += number
print(counter)
  