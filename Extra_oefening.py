import math as m
import random as r
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