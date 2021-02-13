data= open('first_adventure.in','r')
firstline=data.readline()
flist=firstline.split()
secondline=data.readlines()[1:2]
countries=secondline[0]
slist=countries.split()
print(slist)