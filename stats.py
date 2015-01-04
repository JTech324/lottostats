#Open file and create list of strings
database=open('lottohistory.txt')
db=database.read()
substr=db.split()

#Make a list of strings that are only the winning numbers
count=1
arrayList=[]
while count<1906:
    arrayList=arrayList+[substr[count]]
    count=count+3

#alternate arrayList using a list of lists
altCount=1
altArrayList=[]
while altCount<1906:
    altArrayList=altArrayList+[[substr[altCount]]]
    altCount=altCount+3
#alternate xlist using list of lists containing integers, not strings
altXList=[]
for i in range(len(altArrayList)):
    altXList=altXList+[altArrayList[i][0].split("-")]
for i in range(len(altXList)):
    for j in range(len(altXList[i])):
        altXList[i][j]=int(altXList[i][j])


#xlist is a list of all numbers ever drawn as strings
xlist=[]
for i in range(len(arrayList)):
    xlist=xlist+arrayList[i].split("-")
#print (xlist)

#create list of possible numbers
onetonine=['01','02','03','04','05','06','07','08','09']
digiList=[['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09']]
for i in range(10,76):
    digiList=digiList+[[str(i)]]
#print(digiList)

#Append number of times that number has been drawn to its list tuple
#For 1-9, must check for '01' etc as well since the format changed
for i in range(0,9):
    digiList[i]=digiList[i]+[xlist.count(onetonine[i])]
for i in range(9,75):
    digiList[i]=digiList[i]+[xlist.count(str(i+1))]
for i in range(1,10):
    digiList[i][1]=digiList[i][1]+xlist.count(str(i))
#print list vertically
#for i in range(len(digiList)):
#    print(str(digiList[i]))
"""
total=0
for i in range(0,75):
    total=total+digiList[i][1]
print(total)
"""
