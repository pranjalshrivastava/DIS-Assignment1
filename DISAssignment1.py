#Name: Pranjal Shrivastava
#UNumber : U68149220

##Question1
#n – number of lines for the pattern, integer (int)
# summary   : This method prints number pattern of integers using recursion
# For example n = 5 will display the output as: 
# 54321
# 4321
# 321
# 21
# 1
# returns      : N/A
# return type  : void

#MethodName : PrintPattern(n) - This method takes a single parameter(n - number of lines) and uses nested for loops to print
#the required output.

def PrintPattern(n):    
    #Using a for loop to print a reverse range from n to 0 with difference of 1
    for i in range(n, 0, -1):
        num = ""
        #Using a for loop to print the next line
        for j in range(i, 0, -1):
            num = str(num) + str(j)
        print(num)
    return 0

#used nested for loops instead of recursion as recursion is not very efficient here.
#Code with Recursion is commented below:
#def PrintPattern(n):
#   i=0
#   for i in range(n,-1,-1):
#       if i > 0:
#           print(i,end="")
#           if i == 1:
#               print("\n", end="")
#       else:
#            break
#    PrintPattern(n-1)
    

#Question2
#n2 – number of terms of the series, integer (int)
# This method prints the following series till n terms: 1, 3, 6, 10, 15, 21……
# For example, if n2 = 6, output will be
# 1,3,6,10,15,21
# Returns : N/A
# Return type: void
# Hint: Series is 1,1+2=3,1+2+3=6,1+2+3+4=10,1+2+3+4+5=15, 1+2+3+4+5+6=21……



def PrintSeries(n):
    j = 0
    series = ""
    for i in range(1, n + 1):
        j = j + i
        k = str(j) + ","
        series = series + str(k)
    series = series[:-1]
    print(series)
    return 0


#Question3
#On planet “USF” which is similar to that of Earth follows different clock
# where instead of hours they have U , instead of minutes they have S , instead
# of seconds they have F. Similar to earth where each day has 24 hours, each hour
# has 60 minutes and each minute has 60 seconds , USF planet’s day has 36 U , each
# U has 60 S and each S has 45 F. 
# Your task is to write a method usfTime which takes 12HR  format and return string 
# representing input time in USF time format.
# Input format: A string s with time in 12 hour clock format (i.e. hh:mm:ssAM or hh:mm:ssPM) where 01<= hh<=12, 00<=mm,ss,<=60
# Output format: a string with converted time in USF clock format (i.e. UU:SS:FF ) 
# where 01<= UU<=36, 00<=SS<=59,00<=FF<=45 
# Sample Input : 09:15:35PM
# Sample Output: 28:20:35 
# returns      : String
# return type  : string 
# Hint: One way of doing this is by calculating total number of seconds in Input time
# and dividing those seconds according to USF time.

#MethodName: UsfTime(date)
#Created a method UsfTime(date) with parameters as date. UsfTime(date) will extract the date considering the 1st two inputted value
#as the hours, next 2 inputted values as the minutes, last 2 values as the meridiem(AM/PM - Incase of "PM" we add +12 as its 24 hour 
#clock)
#2 values before the last 2 inputted values are seconds.
def UsfTime(date):
    if type(date) == str:
        hours = date[0:2]
        minutes = date[3:5]
        seconds= date[-4:-2]
        meridiem = date[-2:]

        if meridiem == "PM":
            hours = int(hours) + 12
        #calculating the total time in seconds
        total_time = int(hours) * 3600 + int(minutes)*60 + int(seconds)
        #Calculating USF hours, USF minutes, USF Seconds, USF Time (Using previously calculate USF time)
        USF_hours = int(total_time/(60*45))
        USF_minutes = int((total_time - USF_hours * 60 * 45)/45)
        USF_seconds = total_time  - USF_hours * 60 * 45 - USF_minutes * 45
        USF_time = str(USF_hours) + ":" + str(USF_minutes) + ":" + str(USF_seconds)
    else:
        USF_time = "Invalid Input"
    print(USF_time)    
    return USF_time

#Question4
#n- total number of integers( 110 )
# k-number of numbers per line ( 11)
# USF Numbers : This method prints the numbers 1 to 110, 11 numbers per line.
# The method shall print 'U' in place of numbers which are multiple of 3,"S" for 
# multiples of 5,"F" for multiples of 7, 'US' in place of numbers which are multiple 
# of 3 and 5,'SF' in place of numbers which are multiple of 5 and 7 and so on. 
# The output shall look like 
# 1 2 U 4 S U F 8 U S 11 
# U 13 F US 16 17 U 19 S UF 22
# 23 U S 26 U F 29 US 31 32 U....
# 
# returns      : N/A
# return type  : void

#MethodName : UsfNumbers(n, k) - This method is called by passing 2 parameters (n - total number of integers and 
# k- numbers per line)
# This method uses a for loop to read the numbers one by one and a nested if else to check if the number is a multiple
# of 3,5,7. 

def UsfNumbers(n, k):    
    num = ""
    for i in range(1, n+1 ,1):
        if (((i%3) == 0) and ((i%7) == 0) and ((i%5) == 0)):
            num = str(num) + " "  + "USF"
        elif (((i%3) == 0) and ((i%5) == 0)):
            num = str(num) + " " + "US"
        elif (((i%3) == 0) and ((i%7) == 0)):
            num = str(num) + " "  + "UF"
        elif (((i%5) == 0) and ((i%7) == 0)):
            num = str(num) + " "  + "SF"
        elif (i%3) == 0:
            num = str(num) + " "  + "U"
        elif (i%5) == 0:
            num = str(num) + " "  + "S"
        elif (i%7) == 0:
            num = str(num) + " "  + "F"
        else:
            num = str(num) + " " + str(i)
        if (i % k) == 0:
            num = str(num) + "\n"
    print(num)    
    return 0

#Question5
#You are given a list of unique words, the task is to find all the pairs of 
# distinct indices (i,j) in the given list such that, the concatenation of two words i.e. words[i]+words[j] is a palindrome.
#Example:
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example:
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]
# returns      : N/A
# return type  : void

#Method Name : PalindromePairs(array1) - prints a array of palindrome pairs by comparing the values in the input array1

def PalindromePairs(array1):
    
    solution = []
    length = len(array1)
    for i in range(0, length, 1):
        word1 = ""
        for j in range(0, length, 1):
            word1 = array1[i] + array1[j]
            if word1 == word1[::-1]:
                solution.append([i,j])
    print(solution)
    return 0

#Question6
# You are playing a stone game with one of your friends. There are N number of 
# stones in a bag, each time one of you take turns to take out 1 to 3 stones. 
# The player who takes out the last stone will be the winner. In this case you
# will be the first player to remove the stone(s)(Player 1).
# 
# Write a method to determine whether you can win the game given the number of 
# stones in the bag. Print false if you cannot win the game, otherwise print any
# one set of moves where you are winning the game. Array should contain moves by both the players.
#Input: 4
# Output: false
# Explanation: As there are 4 stones in the bag, you will never win the game. 
# No matter 1,2 or 3 stones you take out, the last stone will always be removed by   * your friend.
# Input: 5
#  Output: [1,1,3]   or [1,2,2] or [1,3,1]
# Player 1 picks up 1 stone then player 2 picks up 1 or 2 or 3 stones and the remaining stones are picked up by player 1.
# Explanation: As there are 5 stones in the bag, you take out one stone.
# As there are 4 stones in the bag and it’s your friend’s turn. He will never win the game because no matter 1,2 or 3 stones 
# he takes out, you will the one to take out the last stone. 
#returns      : N/A
# return type  : void


#This is a Nim game problem where the player 1(the one who picks the stones first) will definately lose the game if 
#number of stones is multiple of 4.
#In order to win the game, player 1 has to pick n%4 stones in first turn, and should make sure that he/she chooses 
# 4-(number of stones picked by 2nd player) in following turns.

#Method Name : MovesArray(n) - Prints 3 sets where player 1 wins the game.
#Method Name : Stones(n) - Checks if player 1 or player 2 will win the game.



Moves = []
    
def MovesArray(n):
    if(n%4 == 0):
        MyArray = []
        #MyArray.clear()
        for i in range(1,4): #this loop will iterate from 1 to 3 to create combinations of (1,3),(2,2),(3,1) which adds upto 4.
            MyArray.append(i) 
            MyArray.append(4-i)
            MyArray1 = MyArray * int(n/4) #in order to print the set
            FinalMoves = Moves + MyArray1 #concatenating array which stores the 1st move and array which consists of following moves
            print(FinalMoves)
            MyArray.clear()  #to clear the MyArray so that new values can be appended to Moves  
        
    elif(n%4 == 1):
        n=n-1
        Moves.append(1)
        MovesArray(n)
    elif(n%4 == 2):
        n=n-2
        Moves.append(2)
        MovesArray(n)
    elif(n%4 == 3):
        n=n-3
        Moves.append(3)
        MovesArray(n)
    else:
        print("not valid")

def Stones(n): 
    if(n%4 == 0):
        print("false")
    else:
        MovesArray(n)
    #print(FinalMoves)
    return 0


try:
    PrintPattern(5)
except:
    print("Exception occurred while computing PrintPattern")

try:
    PrintSeries(5)
except:
    print("Exception occurred while computing PrintSeries")

try:
    UsfTime("09:15:35PM")
except:
    print("Exception occurred while computing UsfTime")

try:
    UsfNumbers(50,11)
except:
    print("Exception occurred while computing UsfNumbers")

try:
    PalindromePairs(["abcd","dcba","lls","s","sssll"])
except:
    print("Exception occurred while computing PalindromePairs")

try:
    Stones(5)
except:
    print("Exception occurred while computing Stones")

