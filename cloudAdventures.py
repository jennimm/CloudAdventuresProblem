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

price=999999
out=[]
data=greece[0].split()
for i in range(len(data)):
    unitsneeded=int(data[i+2])
    
    for j in range (len(providerCountryInfo)):
        provider=providers[j]
        for k in range (len(providerCountryInfo[j])):
            value=providerCountryInfo[j][k][1].split()
            if value[1]<price:
                price=int(value[1])
                unitsav=int(value[2])










print(serviceNames)
print(countries)
print(providers)
print(providerCountryInfo)
print(greece)
