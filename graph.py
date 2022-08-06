# Importing Matplotlib for a graph
import matplotlib.pyplot as plt

# Number at which the conjecture starts at
print("Input Start Number: ")
s = int(input())

# Number of times the 2 rules for the conjecture repeat
#print("Input # of Iteration")
n = 0

# f, a x value num
f = 1

# Found or Not Bool
notFound = True

# Current Number
c = s

# Values to plot
y = list()

# If Number is Positive --->
# Check if number is odd or even and apply to proper rule.
if s > 0:
    while(notFound):
        if c%2==0:
            #print(f"{c} / 2 = {c / 2}")
            c = c / 2
            y.append(c)
            if (c == 1):
                notFound = False
            f+=1
        else:
            #print(f"(3 * {c}) + 1 = {(3 * c) + 1}")
            c = (3 * c) + 1
            y.append(c)
            if (c == 1):
                notFound = False
            f+=1
else:
    print("Enter a Positive Number!")

# Values for the X axis
x = list(range(1, f))

# plotting the points 
plt.plot(x, y) 

# naming the x axis
plt.xlabel('# of iterations')
# naming the y axis
plt.ylabel('value')
  
# giving a title to my graph
plt.title(f"Collatz Conjecture starting at {s}")
  
# function to show the plot
plt.show()