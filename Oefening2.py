import math as m
#oefening 2

straal = int(input("Geef de staal van een cirkel: "))

omtrek =  2 * 3.141592 * straal
oppervlakte = straal * straal * 3.141592

print("De omtrek is: " + str(omtrek))
print("De oppervlakte is: " + str(oppervlakte))


#oefening 2 challenge

straal = int(input("Geef de staal van een cirkel: "))

omtrek =  2 * m.pi * straal
oppervlakte = straal * m.pi * 3.141592

print("De omtrek is: " + str(omtrek))
print("De oppervlakte is: " + str(oppervlakte))