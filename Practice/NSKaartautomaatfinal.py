stationnen = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "s-Hertogenbosch", "Eindhoven", "Weert",
"Roermond", "Sittard", "Maastricht"]

def vraagStation(stationnen, vraag):
    stationInLijst = False

    while not stationInLijst:
        station = input(vraag)

        stationInLijst = station in stationnen

        if not stationInLijst:
            print('Deze trein komt niet langs' + station + '.')

def inlezen_beginstation(stationnen):
    beginstationIsNietEindstation = False

    while not beginstationIsNietEindstation:
        beginstation = vraagStation(stationnen,'Wat is uw beginstation?: ')
        beginstationIsNietEindstation = stationnen.index(beginstation) != len(stationnen) - 1

        if not beginstationIsNietEindstation:
            print(beginstation + ' is het eindstation.')

        print(beginstation)


def inlezen_eindstation(stations, beginstation):
    eindstationNaBeginstation = False

    while not eindstationNaBeginstation:
        eindstation = vraagStation(stations, 'Wat is uw beginstation?: ')
        eindstationNaBeginstation = stationnen.index(eindstation) > stations.index(beginstation)
        if not eindstationNaBeginstation:
            print('De trein is al geweest in' + eindstation + 'als je opstapt in ' + beginstation)
        return eindstation

    indexBeginstation = stationnen.index(beginstation)
    indexEindstation = stationnen.index(eindstation)
    tussenStops = indexEindstation - indexBeginstation
    prijsPerStation = 5
    totaalPrijs = prijsPerStation * tussenStops

    def omroepenReis(stationnen, beginstation, eindstation):
        print('Het beginstation' + beginstation + ' is het ' + str(indexBeginstation + 1) + 'e station.' )
        print('Het eindstation ' + eindstation + ' is het ' + str(indexEindstation + 1) +'e station' )
        print('De prijs van het kaartje is ' + str(totaalPrijs) + ' Euro.')

        print('\nJij stapt in trein' + beginstation)

        ritHeeftTussenStations = tussenStops > 1

        if ritHeeftTussenStations:
            for station in range(indexBeginstation + 1, indexEindstation):
                print('\t-' + stationnen[station])

        print('Uw bestemming is' + eindstation)

beginstation = inlezen_beginstation(stationnen)
eindstation = inlezen_eindstation(stationnen, beginstation)
omroepenReis(stationnen, beginstation, eindstation)