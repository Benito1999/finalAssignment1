def standaardprijs(afstandKM):

    prijs= 0
    kmPrijs= 0.8
    maxAfstand= 50
    vastBedrag= 15
    kmPrijsKorting= 0.6


    if afstandKM > maxAfstand:
       prijs += vastBedrag
       prijs += afstandKM*kmPrijsKorting
    else:
        prijs+=afstandKM*kmPrijs

    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):

    prijs = standaardprijs(afstandKM)
    kind = 12
    ouder = 65
    leeftijdWeekKorting = 0.7
    leeftijdWeekendKorting = 0.65
    weekendKorting = 0.6

    if leeftijd < kind or leeftijd >= ouder:
        if weekendrit:
            prijs = prijs * leeftijdWeekendKorting
        else:
            prijs = prijs * leeftijdWeekKorting
    else:
        if weekendrit:
            prijs = prijs * weekendKorting

    return round(prijs, 2)

leeftijden = [11, 12, 64, 65]
afstanden = [12, 40, 60]

for leeftijd in leeftijden:
    for afstand in afstanden:
        print(str(leeftijd) + " Jaar oud | " + str(afstand) + "KM | Weekend |  €" + str(ritprijs(leeftijd, True, afstand)) )

        print(str(leeftijd) + " Jaar oud | " + str(afstand) + "KM | Week |  €" + str(ritprijs(leeftijd, False, afstand)))