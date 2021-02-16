data= open('first_adventure.in','r')
first = data.readline().split()
print(first)

serviceNames = []
countries = []
providers = []
providerCountryInfo = []
array = []
projects = []
countryInfo = []
#servicesFound = False
#providersSection = False
#providerAdded = False
newProvider = True
count = 0
providerCount = 0

sectionCount = 0
fileData  = open('first_adventure.in','r')
for line in fileData:
    line = str(line)
    if sectionCount == 0:
        sectionCount += 1
    elif sectionCount == 1:
        line = line.rstrip("\n")
        serviceNames.append(line.split(" "))
        #servicesFound = True
        sectionCount += 1
    elif sectionCount == 2:
        line = line.rstrip("\n")
        countries = line.split(" ")
        #servicesFound = False
        #providersSection = True
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
        projects.append(line)
print(serviceNames)
print(countries)
print(providers)
print(providerCountryInfo)
print(projects)
