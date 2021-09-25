import math
width = int(input("Mekkora a szoba szélessége méterben?"))
height = int(input("Mekkore a szoba magassága méterben?"))

cmw = width*100
cmh = height*100
tile = 20*1,1

area = cmw*cmh
end = area/tile

print("Ennyi csempe kell:", area)
#Is it hell?