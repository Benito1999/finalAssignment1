bestaandeKluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def toon_aantal_kluizen_vrij():
    bestand = open('kluis.txt', 'r')

    aantalRegels = 0
    for regel in bestand:
        aantalRegels += 1

    return len(bestaandeKluizen) - aantalRegels

def nieuwe_kluis():
    bestand = open('kluis.txt', 'r+')
    beschikbareKluizen = bestaandeKluizen
    regels = bestand.readlines()
    for regel in regels:
        kluis = regel.split(';')
        kluisNummer = int(kluis[0])
        beschikbareKluizen.remove(kluisNummer)
    print(beschikbareKluizen)
    if len(beschikbareKluizen) == 0:
        print('Geen Kluizen Meer Beschikbaar!')
    else:
        wachtWoord = input('Kies Uw Wachtwoord.')
        print('Uw kluis is:'+ str(beschikbareKluizen[0]))
        print('uw wachtwoord is:'+ wachtWoord)
    bestand.write(str(beschikbareKluizen[0])+';'+ wachtWoord + '\n')

def kluis_openen():
    bestand = open('kluis.txt', 'r')
    juisteCombinatie = bestand.readlines()
    deJuisteCombinatie = input('Voer hier uw kluisnummer en wachtwoord in.')
    for juisteCombinatie in bestand:
        print(deJuisteCombinatie)
    if deJuisteCombinatie in juisteCombinatie:
        print('Sesam Open U')

    else:
        print('Zoek je eigen kluis!')



def kluis_teruggeven():
    return
menuKeuze= input('1: Ik wil weten hoeveel kluizen nog vrij zijn, 2: Ik wil een nieuwe kluis, 3: Ik wil even iets uit mijn kluis halen. \r\n')

menuKeuze = int(menuKeuze)
if menuKeuze == 1:
    aantalKluizenVrij = toon_aantal_kluizen_vrij()
    print(str(aantalKluizenVrij))
elif menuKeuze == 2:
    nieuwe_kluis()

elif menuKeuze == 3:
    kluis_openen()


else:
    print("Beter ga je gewoon 1,2 of 3 kiezen!")
