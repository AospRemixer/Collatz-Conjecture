# Import a Exit Function
from sys import exit

# Number at which the conjecture starts at
print("Input Start Number: ")
s = int(input())

# The number it should compute to
print("Input End Number: ")
c = int(input())

# Cur Num          
#n = 0
u = 0

# Function to check if number ends up at 1
# Return True if Num Works in the Conjecture
def numWorks(num):
    global u
    u = 0
    for x in range(9000000):
        if (num % 2 == 0):
            num = num/2
            u+=1
            if (num == 1):
                return True
                break
        elif (num % 2 != 0):
            num = (3*num) + 1
            u+=1
            if (num == 1):
                return True
                break
        else:
            return False
    

for i in range(s, c + 1):
    if (numWorks(i)):
        print(f"Check: {i} = WORKS ({u})")
    else:
        print(f"Check: {i} = DOESN'T WORK ({u})")
        exit(0)