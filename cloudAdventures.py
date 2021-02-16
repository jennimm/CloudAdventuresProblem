fileChosen = "first_adventure.in"

providers = []
providerCountryInfo = []
array = []
countryInfo = []
newProvider = True
count = 0
providerCount = 0

slovak = []
greece = []
italy = []
swede = []
bulgaria = []

sectionCount = 0
fileData  = open(fileChosen,'r')
V, S, C, P = (int(x) for x in fileData.readline().split())
print(C)
serviceNames = fileData.readline().split()
countries = fileData.readline().split()
for line in fileData:
    line = str(line)
    if sectionCount == 0:
        line = line.rstrip("\n")
        if newProvider == True:
            if len(providers)+1 == V:
                sectionCount += 1
            providers.append(line[:-2])
            noRegions = line[len(line)-1] #
            newProvider = False
        else: 
            count += 1
            if count == 3:
                array.append(line)
                countryInfo.append(array)
                array = []
                count = 0
                if len(countryInfo) == int(noRegions):
                    providerCountryInfo.append(countryInfo)
                    countryInfo = []
                    newProvider = True
            else:
                array.append(line)
    else:
        line = line.rstrip("\n")

        if "Greece" in line:
            greece.append(line)
        if "Slovakia" in line:
            slovak.append(line)
        if "Italy" in line:
            italy.append(line)
        if "Sweden" in line:
            swede.append(line)
        if "Bulgaria" in line:
            bulgaria.append(line)

data=greece[0].split()

def solutionFinder(price, out, data, index, totalUnits, providerCountryInfo):
    for j in range(len(providerCountryInfo)):
        provider=providers[j]
        for k in range(len(providerCountryInfo[j])):
            value=providerCountryInfo[j][k][1].split()
            if float(value[1]) < price and int(value[2]) != 0:
                price=float(value[1])
                unitsav=int(value[2])
                index = k
        if index != None:
            out.append([j, index, unitsav])
            totalUnits += unitsav
            array = providerCountryInfo[j][index][1].split()
            array[2] = '0'
            string = " "
            providerCountryInfo[j][index][1] = string.join(array)
        if totalUnits >= unitsneeded:
            return out
        else:
            price = 9999
        if totalUnits < unitsneeded and j == len(providerCountryInfo)-1:
            return solutionFinder(price, out, data, None, totalUnits, providerCountryInfo)

##for the first service of the first project
unitsneeded=int(data[2])
out = solutionFinder(9999, [], data, None, 0, providerCountryInfo)
print(out)
