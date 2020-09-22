import math as m
import random as r

'''
#Oefening 1

a = int(input("Geef een getal "))
b = int(input("Geef een getal "))

print(a+b)
print(int(a/b))
print(a%b)
a += 1
b +=1
print(a + b)
'''

'''
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
'''

'''
#oefening 3

zin1 = "The quick brown fox "
zin2 = "jumps over the lazy dog"

volzin = zin1 + zin2

print(volzin)

print(volzin.replace("fox","cat"))

#oefening 3 challenge

tekst = "The ‘Python library’ contains several different kinds of components.It  contains  data  types  that  would  normally  be  considered  part  of  the  ‘core’  of  a language, such as numbers and lists. For these types, the Python language core defines  the  form  of  literals  and  places  some  constraints  on  their  semantics,  but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)"

print(tekst.count("core"))
'''

'''
#Oefening 4

thislist = [1,2,3]
print(thislist)
thislist[1] = 23
print(thislist)
thislist[2] = 1.5  #dit lukt
print(thislist)

#oefening 4 challenge

namen = ["aaron", "steve", "yaira", "bernard", "robin"]
aantal = 0

naam = input("Welke naam wilt u zoeken? ")
for x in namen:
    if x == naam:
        aantal +=1
print(aantal)
'''

'''
#extra oefening

students = ["John","Karl","Olaf","Zacharia","Elke","Jean-luc","Jean-jean","Kevin","Sidney"]

aantal_groepen = m.floor(len(students) / 4)

print(aantal_groepen)

aantal_uit_groep = len(students)%4

print(aantal_uit_groep)

groep2 = students[4:8]

print(groep2)

#extra oefening challenge

r.seed()
vrijwilliger = r.randint(0,8)
print(students[vrijwilliger])
'''