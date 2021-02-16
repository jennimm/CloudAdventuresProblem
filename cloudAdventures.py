fileChosen = "first_adventure.in"
data= open(fileChosen,'r')
first = data.readline().split()
data.close()
print(first)

serviceNames = []
countries = []
providers = []
providerCountryInfo = []
array = []
projects = []
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
for line in fileData:
    line = str(line)
    if sectionCount == 0:
        sectionCount += 1
    elif sectionCount == 1:
        line = line.rstrip("\n")
        serviceNames.append(line.split(" "))
        sectionCount += 1
    elif sectionCount == 2:
        line = line.rstrip("\n")
        countries = line.split(" ")
        sectionCount+= 1
    elif sectionCount == 3:
        line = line.rstrip("\n")
        if newProvider == True:
            if len(providers)+1 == int(first[0]):
                sectionCount += 1
            providers.append(line[:-2])
            noCountries = line[len(line)-1:]
            newProvider = False
        else: 
            count += 1
            if count == 3:
                array.append(line)
                countryInfo.append(array)
                array = []
                count = 0
                if len(countryInfo) == int(noCountries):
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


print(serviceNames)
print(countries)
print(providers)
print(providerCountryInfo)
print(greece)
