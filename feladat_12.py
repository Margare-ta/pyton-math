import math
point1= int(input("'A' pont első koordinátája:"))
point12= int(input("'A' pont második koordinátája:"))
point2= int(input("'B' sík első koordinátája:"))
point22= int(input("'B' sík második koordinátája:"))

length = math.sqrt((point2-point1)**2+(point22-point12)**2)

print("Ez a hossza:", length)
