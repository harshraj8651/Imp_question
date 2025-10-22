# To implement Simple AI techniques - Water Jug Problem.

x = 0 
y = 0 
m = 4
n = 3
print("Initial state = (0,0)")
print("Capacities = (4,3)")
print("Goal state = (2,y)")
while x != 2:
  r = int(input("Enter rule"))
  if(r == 1):
    x = m
  elif(r == 2):
    y = n
  elif(r == 3):
    x = 0
  elif(r == 4):
    y = 0
  elif(r == 5):
    t = n - y
    y = n
    x -= t
  elif(r == 6):
    t = m - x
    x = m
    y -= t
  elif(r == 7):
    y += x
    x = 0
  elif(r == 8):
    x += y
    y = 0
  print (x, y)



# OUTPUT:
# Initial state = (0,0)
# Capacities = (4,3)
# Goal state = (2,y)
# Enter rule2
# 0 3
# Enter rule8
# 3 0
# Enter rule2
# 3 3
# Enter rule6
# 4 2
# Enter rule3
# 0 2
# Enter rule8
# 2 0