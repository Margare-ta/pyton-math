import math
price = int(input("Mennyi az átlagos havi villanyszámlád?"))

year = price*12
kWh = year/39
piece = math.ceil((kWh*0.85)/310)
roof = piece*1.7

print("Éves energia költség:", year, 
"\n éves villamos energia fogyasztás értéke:", kWh, "kWh",
"\nNapemelek száma:", piece,
"\ntetőfelület minimális mérete:", roof,"m2" )

