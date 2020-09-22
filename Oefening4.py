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