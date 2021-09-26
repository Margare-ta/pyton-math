price = int(input("Mennyibe kerül az ingatlan?"))

plus1 = price*0.75
plus2 = price*0.15
plus3 = price*0.04
plus4 = 40000
plus5 = 6600

print("Ingatlan ára:", price, "\nIngatlanügynöknek járó felszámolás:",plus1,
"\nÜgyvéd díjja:", plus2, "\nIngatlan illeték:", plus3,
"\nEnergetikai tanúsítvány:", plus4, "\nföldhivatal ára:", plus5,
"\nösszesen együtt:", plus5+plus3+plus1+plus2+plus4)